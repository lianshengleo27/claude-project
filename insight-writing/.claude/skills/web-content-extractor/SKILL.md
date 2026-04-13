---
name: web-content-extractor
description: Automatically crawl content from websites, preserve original text without modification or translation, and summarize it in structured markdown format using the original language. Use this skill whenever the user wants to get content from a given URL, needs to extract information from web pages with original content preservation, or wants to summarize online articles in their original language. This skill is especially useful for research, content analysis, or gathering information from multiple web sources while maintaining content authenticity.
compatibility: Requires WebFetch tool access
---

# Web Content Extractor

This skill enables you to crawl website content, preserve original text without modification or translation, and present it in well-structured markdown format with summarization in the original language. It's designed for research, content analysis, and information gathering tasks where maintaining content authenticity is important.

## When to Use This Skill

Use this skill when:
- The user provides a URL and wants the content extracted
- The user needs a summary of a web article or blog post
- Research requires gathering information from multiple web sources
- The user mentions "crawl", "scrape", "extract content", or "get text from website"
- You need to analyze web content for information retrieval

## Workflow Overview

1. **URL Validation**: Check if the URL is valid and accessible
2. **Content Fetching**: Use WebFetch to retrieve and convert the webpage to markdown
3. **Original Content Preservation**: Preserve WebFetch output without modification or translation
4. **Summarization in Original Language**: Create summary using the same language as original content
5. **Output Formatting**: Present results in the required structured format

## Detailed Instructions

### Step 1: URL Analysis
- Verify the URL format and accessibility
- If the URL is not valid or accessible, inform the user and suggest alternatives
- Consider potential redirects or authentication requirements

### Step 2: Content Retrieval
Use the WebFetch tool with an appropriate prompt:
```
Extract the main textual content from this webpage, removing navigation, ads, scripts, and other non-content elements. Focus on the primary article or information content.
```

The WebFetch tool converts HTML to markdown and performs initial content extraction. Preserve the WebFetch output as-is without additional processing or translation.

### Step 3: Original Content Preservation
After obtaining content from WebFetch:

1. **Preserve original content**:
   - DO NOT modify, clean, or translate the content
   - Keep the content in its original language
   - Preserve the exact formatting and structure as returned by WebFetch
   - Include any markdown conversion done by WebFetch as-is

2. **Extract metadata** (when available):
   - Page title (use title from WebFetch or webpage)
   - Publication date (if identifiable)
   - Author information (if available)
   - Content type identification based on URL and content

### Step 4: Summarization Strategy (In Original Language)
Create a summary in the same language as the original content:

1. **Executive Summary**: 2-3 sentence overview of the entire content (in original language)
2. **Key Points**: Bulleted list of main arguments, findings, or information (in original language)
3. **Important Details**: Notable statistics, quotes, or specific data points (in original language)
4. **Content Analysis**: Objective assessment of content characteristics

The summary should be approximately 20-30% of the original content length, but adjust based on complexity and user needs. DO NOT translate the summary - keep it in the original language of the content.

### Step 5: Output Format
ALWAYS present results in this exact structure:

```markdown
# Web Content Extraction: [Page Title]

## Source Information
- **URL**: [Full URL]
- **Title**: [Page Title]
- **Extraction Date**: [Current Date]
- **Content Type**: [Article/Blog Post/Documentation/News/etc.]

## Original Content
[Full original content from WebFetch without modification or translation]

## Summary

### Executive Summary
[Brief 2-3 sentence overview in the original language]

### Key Points
- [First key point in original language]
- [Second key point in original language]
- [Third key point in original language]

### Important Details
- [Notable statistic or fact in original language]
- [Key quote or statement in original language]
- [Critical information in original language]

### Content Analysis
- **Length**: Approximately [word count] words
- **Primary Topics**: [Topic 1], [Topic 2], [Topic 3]
- **Tone**: [Informational/Opinion/Technical/etc.]
- **Usefulness**: [Assessment for user's stated or implied needs]
```

## Special Considerations

### Handling Different Content Types
- **Articles/Blog Posts**: Focus on main arguments, evidence, conclusions
- **Documentation**: Preserve code examples, API references, technical details
- **News Articles**: Highlight who, what, when, where, why, how
- **Product Pages**: Extract specifications, features, pricing
- **Academic Papers**: Note methodology, findings, limitations

### Error Handling
- If WebFetch fails, try alternative approaches or inform the user
- For paywalled or login-required content, note the limitation
- If content is primarily non-text (videos, images), adapt your approach
- Handle rate limiting and respect robots.txt implicitly

### Privacy and Ethics
- Only access publicly available content
- Respect website terms of service
- Use extracted content for legitimate purposes
- Attribute sources when appropriate

## Examples

### Example 1: Technical Documentation
**Input**: "Get the content from https://docs.example.com/api-reference"
**Output**: Original documentation content with preserved code blocks and structure, plus summary in original language.

### Example 2: News Article  
**Input**: "Summarize this news article: https://news.example.com/breaking-story"
**Output**: Original news article text without modification, with summary in the article's original language.

### Example 3: Research Blog Post
**Input**: "Extract the main points from this blog post about AI safety"
**Output**: Original blog post content, with summary and analysis in the original language.

## Tips for Better Results

1. **Language Preservation**: Always keep content and summary in the original language - do not translate
2. **Context Awareness**: Consider why the user wants this content and tailor the summary accordingly
3. **Multi-page Content**: For paginated content, consider fetching multiple pages if needed
4. **Comparative Analysis**: When multiple URLs are provided, compare and contrast the content
5. **Follow-up Questions**: Ask clarifying questions if the URL or purpose is unclear
6. **Quality Assessment**: Note content quality, bias, or reliability issues when apparent

Remember: The goal is to provide original, unmodified content with accurate summarization in the original language, maintaining content authenticity while saving user time.