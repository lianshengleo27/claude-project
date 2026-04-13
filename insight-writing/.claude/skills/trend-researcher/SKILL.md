---
name: trend-researcher
description: Researches current trends of specific topics and formats findings into concise, ready-to-use PowerPoint slides with logical storytelling structure. This skill should be used when users need up-to-date trend analysis for presentations, reports, or strategy planning.
---

# Trend Researcher

## Overview

This skill enables Claude to research current trends on any given topic and format the findings into ready-to-use PowerPoint slides. The output follows a logical storytelling structure with concise explanations under clear headings, making it directly copy-pasteable into presentation software.

## When to Use This Skill

- User requests current trends analysis for a specific topic (technology, business, social, etc.)
- User needs presentation-ready content formatted for PowerPoint slides
- User wants up-to-date information with logical narrative flow
- User requests "research the current trend of [topic]" or similar phrasing

## Workflow: From Research to Presentation Slides

### 1. Understanding the Request
- Identify the specific topic and scope from user's request
- Determine if user wants broad trends or specific subtopics
- Clarify any preferences: time frame (e.g., 2024-2025 trends), geographic focus, industry context

### 2. Conducting Research
- Use WebSearch tool with current year (2026) for up-to-date information
- Search pattern: "[Topic] trends 2026" OR "[Topic] current developments 2026" OR "[Topic] emerging trends"
- Include authoritative sources: industry reports, research firms, news publications
- Gather 5-8 key trends with supporting data points

### 3. Structuring the Narrative
Organize findings into a logical storytelling flow:

```
Introduction → Current Landscape → Key Drivers → Emerging Trends → Impact/Implications → Future Outlook
```

Alternative narrative structures:
- **Problem-Solution**: Challenge → Current solutions → Emerging innovations
- **Evolutionary**: Past → Present → Future trajectory  
- **Layered Analysis**: Macro trends → Industry impact → Organizational implications

### 4. Formatting for PowerPoint Slides

Each slide should follow this format:

```
### [Heading: Clear, Action-Oriented Title]

[Concise explanation: 2-3 sentences maximum]
- Bullet point 1: Key statistic or data point
- Bullet point 2: Example or case study
- Bullet point 3: Implication or recommendation
```

**Visual formatting tips:**
- Headings use Title Case
- Keep explanations under 50 words per slide
- Use bullet points, not paragraphs
- Include actionable insights
- Add data points where available (%, $, numbers)

### 5. Including Sources
- Always include "Sources:" section at the end
- List URLs as markdown hyperlinks: [Source Title](URL)
- Include publication dates when available
- Prioritize recent sources (2025-2026)

## Example Output Structure

**User request:** "Research current trends in artificial intelligence"

**Expected output format:**

```
### AI Democratization: Tools for Everyone

Generative AI tools have become accessible to non-technical users through intuitive interfaces. This shift empowers business users to leverage AI without coding expertise.

- 72% of enterprises now provide AI tools to non-technical staff
- No-code AI platforms grew 300% in 2025
- Enables faster prototyping and innovation across departments

### Multimodal AI: Beyond Text

AI systems now process and generate across text, images, audio, and video simultaneously. This creates more natural human-computer interactions.

- GPT-5 demonstrates strong cross-modal understanding
- Video generation tools reduce production costs by 60%
- Enriches customer experiences through multiple channels

### Edge AI: Processing at the Source

AI inference moves from cloud to edge devices, enabling real-time processing with lower latency and enhanced privacy.

- Edge AI chip market projected to reach $45B by 2027
- Reduces cloud dependency and bandwidth costs
- Critical for autonomous vehicles and IoT applications

[Continue with 3-5 more trends...]

Sources:
- [Gartner Top 10 Strategic Technology Trends for 2026](https://www.gartner.com/trends)
- [McKinsey AI Trends Report 2025](https://www.mckinsey.com/ai-trends)
- [Forrester Emerging Tech 2026](https://www.forrester.com/tech-trends)
```

## Best Practices

### Research Quality
- Verify information across multiple sources
- Include quantitative data when available
- Balance optimism with realistic challenges
- Note conflicting perspectives if they exist

### Presentation Readiness
- Each slide should stand alone if printed separately
- Avoid jargon or explain technical terms
- Use consistent tense (present tense for current trends)
- Include transition phrases between slides when presenting verbally

## Common Topic Categories

### Technology Trends
- Artificial Intelligence & Machine Learning
- Cybersecurity advancements  
- Quantum computing developments
- Web3 & blockchain innovations
- 5G/6G and connectivity

### Business & Industry
- Remote/hybrid work evolution
- Sustainability and ESG initiatives
- Supply chain digitization
- Customer experience transformation
- Fintech and digital payments

### Social & Consumer
- Gen Z/Millennial behavior shifts
- Health and wellness movements
- Digital entertainment consumption
- Sustainability purchasing habits
- Social media platform migrations
