#!/usr/bin/env python3
"""
Web Content Extractor - Python script version
Extract original content from web pages and generate structured markdown summaries in original language
Based on Claude Code's web-content-extractor skill

Usage:
  python web_content_extractor.py <URL>
  or
  python web_content_extractor.py
    then enter URL when prompted
"""

import sys
import os
import argparse
from datetime import datetime
import re

# 尝试设置标准输出编码以避免Windows控制台编码问题
try:
    # Python 3.7+
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    # 旧版本Python
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# 尝试导入所需库，如果失败则提示安装
try:
    import requests
except ImportError:
    print("Error: requests library required. Run: pip install requests")
    sys.exit(1)

try:
    import html2text
except ImportError:
    print("Error: html2text library required. Run: pip install html2text")
    sys.exit(1)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Warning: BeautifulSoup4 not installed, content extraction may be less accurate. Recommended: pip install beautifulsoup4")
    BeautifulSoup = None

try:
    from newspaper import Article
except ImportError:
    print("Info: newspaper3k not installed, using alternative extraction methods. For better article extraction, run: pip install newspaper3k")
    Article = None

def fetch_webpage(url):
    """获取网页内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        # 检测编码
        if response.encoding is None:
            response.encoding = 'utf-8'

        return response.text, response.url
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch webpage: {e}")
        return None, None

def extract_main_content(html, url):
    """Extract main content and convert to markdown"""
    # First try newspaper3k for article extraction
    if Article:
        try:
            article = Article(url)
            article.download(input_html=html)
            article.parse()

            if article.text and len(article.text) > 500:  # Reasonable content length
                # Use article text as markdown (simple conversion)
                content = article.text
                # Convert to markdown-like format (preserve paragraphs)
                markdown_content = content.replace('\n\n', '\n\n')
                return markdown_content.strip()
        except Exception as e:
            print(f"Info: Newspaper3k extraction failed, using fallback: {e}")

    # Fallback to html2text with BeautifulSoup filtering
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True  # Ignore images to get pure text
    h.ignore_emphasis = False
    h.body_width = 0  # No wrap
    h.unicode_snob = True

    # If BeautifulSoup is available, try to extract main content area
    if BeautifulSoup:
        try:
            soup = BeautifulSoup(html, 'html.parser')

            # Remove script, style, navigation, footer, header tags
            for script in soup(["script", "style", "nav", "footer", "header", "aside", "form"]):
                script.decompose()

            # Try to find article content using multiple selectors
            article = None
            selectors = [
                'article',
                'main',
                '.post-content',
                '.article-content',
                '.entry-content',
                '#content',
                '.content',
                '.post',
                '.blog-post',
                '.article-body',
                '.story-content'
            ]

            for selector in selectors:
                elements = soup.select(selector)
                if elements:
                    # Find the element with most text
                    best_element = max(elements, key=lambda el: len(el.get_text(strip=True)))
                    if len(best_element.get_text(strip=True)) > 200:  # Enough text
                        article = best_element
                        break

            if article:
                # Use the processed HTML for conversion
                html = str(article)
        except Exception as e:
            print(f"Warning: Error using BeautifulSoup for content extraction: {e}")
            # Continue with original HTML

    markdown_content = h.handle(html)

    # Clean excessive newlines
    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)

    # Clean the extracted content to remove recommendations and unrelated sections
    markdown_content = clean_content_text(markdown_content)

    return markdown_content.strip()

def clean_content_text(text):
    """Clean extracted content to remove recommendations, ads, and unrelated sections"""
    import re

    # Split into lines for processing
    lines = text.split('\n')
    cleaned_lines = []

    # Keywords that indicate recommendation sections (Japanese and English)
    # Expanded list with more variations
    recommendation_keywords = [
        # Japanese keywords
        'あわせて読みたい', '関連記事', 'おすすめ記事', 'おすすめ', '推薦記事',
        'こちらもおすすめ', '関連する記事', '同じカテゴリの記事', '人気記事',
        '新着記事', '過去の記事', '次の記事', '前の記事','参考文献',
        # English keywords
        'Recommended', 'Read also', 'You may also like', 'Related articles',
        'Similar posts', 'More from', 'Continue reading', 'Popular posts',
        'Featured posts', 'You might also like', 'Don\'t miss', 'Recommended'
    ]

    # Find the line where recommendation section starts
    recommendation_start_index = -1
    for i, line in enumerate(lines):
        line_stripped = line.strip().lower()  # Use lowercase for case-insensitive matching
        for keyword in recommendation_keywords:
            if keyword.lower() in line_stripped:
                recommendation_start_index = i
                break
        if recommendation_start_index != -1:
            break

    # If recommendation section found, keep only lines before it
    if recommendation_start_index != -1:
        # Keep lines up to (but not including) the recommendation start
        cleaned_lines = lines[:recommendation_start_index]

        # Also remove any trailing "読んでみてはいかがでしょうか" or similar lines
        # that might appear right before recommendations
        if cleaned_lines:
            # Check last few lines for other recommendation indicators
            last_few_lines = cleaned_lines[-3:] if len(cleaned_lines) >= 3 else cleaned_lines
            for j, line in enumerate(reversed(last_few_lines)):
                line_lower = line.strip().lower()
                if any(indicator in line_lower for indicator in ['いかがでしょうか', '参考に', 'チェック', 'click', 'link']):
                    # Remove this line and any after it
                    remove_from = len(cleaned_lines) - (j + 1)
                    cleaned_lines = cleaned_lines[:remove_from]
                    break
    else:
        # No recommendation section found, keep all lines
        cleaned_lines = lines

    # Join lines back
    cleaned_text = '\n'.join(cleaned_lines)

    # Remove image references that might still be there
    cleaned_text = re.sub(r'!\[.*?\]\(.*?\)', '', cleaned_text)
    cleaned_text = re.sub(r'\[\!\[.*?\]\(.*?\)\]\(.*?\)', '', cleaned_text)

    # Remove base64 image data
    cleaned_text = re.sub(r'data:image/[^;]+;base64,[a-zA-Z0-9+/=]+', '', cleaned_text)

    # Remove standalone links that are likely image links
    cleaned_text = re.sub(r'\[\]\(https?://[^)]+\.(jpg|jpeg|png|gif|svg|webp)[^)]*\)', '', cleaned_text)

    # Remove markdown link definitions (reference-style links)
    cleaned_text = re.sub(r'^\[.*?\]:\s*.+$', '', cleaned_text, flags=re.MULTILINE)

    # Remove excessive whitespace and clean up formatting
    cleaned_text = re.sub(r'\n{3,}', '\n\n', cleaned_text)
    cleaned_text = re.sub(r'[ \t]{2,}', ' ', cleaned_text)

    # Remove lines that are just punctuation or symbols
    cleaned_lines = cleaned_text.split('\n')
    cleaned_lines = [line for line in cleaned_lines if line.strip() and not re.match(r'^[\s\*\-\.\_]*$', line.strip())]
    cleaned_text = '\n'.join(cleaned_lines)

    return cleaned_text.strip()

def extract_title(html):
    """从HTML提取标题"""
    if BeautifulSoup:
        try:
            soup = BeautifulSoup(html, 'html.parser')
            title_tag = soup.find('title')
            if title_tag:
                return title_tag.text.strip()
        except:
            pass

    # 简单正则匹配
    title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    if title_match:
        title = re.sub(r'\s+', ' ', title_match.group(1)).strip()
        return title

    return "Unknown Title"

def estimate_word_count(text):
    """估算字数"""
    # 简单空格分割
    words = text.split()
    return len(words)

def generate_summary(text, original_language="中文"):
    """Generate summary (in original language)"""
    # Clean text: remove markdown images and base64 data
    import re

    # Remove markdown images ![alt](src)
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    # Remove base64 images data:image
    text = re.sub(r'data:image/[^;]+;base64,[a-zA-Z0-9+/=]+', '', text)
    # Remove standalone image tags
    text = re.sub(r'!\[\]\(.*?\)', '', text)
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)

    # Simple summarization algorithm: extract first few paragraphs and key sentences
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]

    # Filter very short paragraphs and remove those that are mostly non-text
    paragraphs = [p for p in paragraphs if len(p) > 50 and not re.search(r'^[#\*\-\d\.\s]+$', p)]

    if not paragraphs:
        # If no good paragraphs, use the entire cleaned text
        paragraphs = [text]

    # Use first 2-3 paragraphs for summary
    summary_paragraphs = paragraphs[:2]  # Use fewer paragraphs for cleaner summary
    summary_text = "\n\n".join(summary_paragraphs)

    # Limit summary length to 20-30% of original
    word_count = estimate_word_count(text)
    target_word_count = max(100, min(300, int(word_count * 0.25)))  # Cap at 300 words

    # If summary is too long, truncate
    if estimate_word_count(summary_text) > target_word_count:
        # Take first paragraph or first 500 chars
        summary_text = paragraphs[0] if paragraphs else text[:500]
        summary_text = summary_text[:500]  # Additional safety truncation

    return summary_text.strip()

def extract_key_points(text, max_points=5):
    """Extract key points (simple implementation)"""
    # Clean text first
    import re

    # Remove markdown images and base64 data
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'data:image/[^;]+;base64,[a-zA-Z0-9+/=]+', '', text)
    text = re.sub(r'!\[\]\(.*?\)', '', text)
    text = re.sub(r'\s+', ' ', text)

    # Split into sentences (Japanese/Chinese punctuation included)
    sentences = re.split(r'[。！？!?\.\n]', text)
    sentences = [s.strip() for s in sentences if s.strip() and len(s.strip()) > 10]

    # Define keywords (Japanese and English)
    keywords = ['重要', '关键', '主要', '总结', '結論', '因此', '所以', 'つまり',
                'important', 'key', 'main', 'conclusion', 'therefore', 'essential']

    key_sentences = []
    for sentence in sentences:
        # Check sentence length and keywords
        if len(sentence) > 20 and any(keyword in sentence for keyword in keywords):
            key_sentences.append(sentence)
            if len(key_sentences) >= max_points:
                break

    # If no key sentences found, use first few substantial sentences
    if not key_sentences and sentences:
        key_sentences = sentences[:min(max_points, len(sentences))]

    return key_sentences

def identify_content_type(url, title, content):
    """识别内容类型"""
    url_lower = url.lower()
    title_lower = title.lower()
    content_lower = content.lower()

    if any(word in url_lower or word in title_lower for word in ['blog', 'post', '博客']):
        return "Blog Post"
    elif any(word in url_lower or word in title_lower for word in ['news', '新闻', '报道']):
        return "News Article"
    elif any(word in url_lower or word in title_lower for word in ['docs', 'documentation', 'api', '文档']):
        return "Technical Documentation"
    elif any(word in url_lower or word in title_lower for word in ['product', '产品', 'shop', '商品']):
        return "Product Page"
    elif any(word in url_lower or word in title_lower for word in ['paper', '研究', '学术', '论文']):
        return "Academic Paper"
    elif any(word in url_lower or word in title_lower for word in ['wiki', 'wikipedia', '百科']):
        return "Wiki Entry"
    else:
        # 基于内容分析
        if len(content) < 500:
            return "Short Article/Introduction"
        elif len(content) > 2000:
            return "Long Article"
        else:
            return "Web Page Content"

def create_markdown_output(url, final_url, title, original_content, extraction_date):
    """Create markdown output (original content only, no summary)"""
    # Identify content type
    content_type = identify_content_type(url, title, original_content)

    # Estimate word count
    word_count = estimate_word_count(original_content)

    # Build markdown (only source info and original content)
    markdown = f"""# Web Content Extraction: {title}

## Source Information
- **URL**: {url}
- **Final URL**: {final_url}
- **Title**: {title}
- **Extraction Date**: {extraction_date}
- **Content Type**: {content_type}
- **Estimated Word Count**: {word_count} words

## Original Content

{original_content}
"""

    return markdown

def main():
    parser = argparse.ArgumentParser(description='Extract content from web pages and generate structured markdown summaries')
    parser.add_argument('url', nargs='?', help='URL of the web page to extract content from')
    args = parser.parse_args()

    # 获取URL
    url = args.url
    if not url:
        url = input("Enter webpage URL: ").strip()

    if not url:
        print("Error: URL must be provided")
        sys.exit(1)

    print(f"Extracting: {url}")

    # 获取网页
    html, final_url = fetch_webpage(url)
    if not html:
        print("Failed to retrieve webpage content")
        sys.exit(1)

    # 提取标题
    title = extract_title(html)
    print(f"Title: {title}")

    # 提取主要内容
    print("Extracting main content...")
    original_content = extract_main_content(html, url)

    if not original_content or len(original_content) < 50:
        print("Warning: Extracted content may be incomplete or empty")

    print(f"Extracted approximately {estimate_word_count(original_content)} words")

    # 创建输出
    extraction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    markdown_output = create_markdown_output(url, final_url, title, original_content, extraction_date)

    # 保存到文件
    output_filename = "output-content.md"
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(markdown_output)

    print(f"Content saved to: {output_filename}")
    print(f"File size: {len(markdown_output)} characters")

    return 0

if __name__ == "__main__":
    sys.exit(main())