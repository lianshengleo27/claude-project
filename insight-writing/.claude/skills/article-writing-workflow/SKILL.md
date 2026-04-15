---
name: article-writing-workflow
description: Structured article writing workflow based on existing frameworks with iterative review and polishing. Use this skill when the user wants to write content based on an existing article framework or outline, needs help developing complete articles section by section with thorough review cycles, or wants to maintain consistent writing style by referencing past work. This skill is especially useful for blog posts, technical articles, reports, and any structured writing that requires logical coherence and reader-friendly presentation.
---

# Article Writing Workflow

A structured, iterative approach to writing articles based on existing frameworks. This skill guides you through a methodical process of developing content section by section, with rigorous review cycles to ensure quality, coherence, and alignment with the user's writing style.

## Core Principles

1. **Language consistency**: Output language matches the language of the input framework. If the framework is in Chinese, write in Chinese; if in English, write in English.
2. **Style imitation**: Study the user's past writing samples in the `reference/` folder to understand and mimic their writing style, tone, and vocabulary.
3. **Iterative refinement**: Each section undergoes multiple review cycles before moving to the next section.
4. **User control**: Pause after each section for user approval before proceeding.

## Workflow Overview

The workflow follows a strict sequence for each section:

1. **Analyze** framework and reference materials
2. **Rewrite** section titles based on framework
3. **Write** content for current section
4. **Review** with two-level critique
5. **Polish** based on review findings
6. **Repeat** review-polish until no issues remain
7. **Request permission** to proceed to next section

## Detailed Instructions

### Phase 1: Preparation

**Before starting writing:**

1. **Examine the framework**: Read the provided framework carefully. Understand its structure, main arguments, and intended message.
2. **Analyze reference articles**: If a `reference/` folder exists, read 2-3 representative articles to understand:
   - Sentence structure and length
   - Vocabulary and terminology preferences  
   - Tone (formal, conversational, technical, etc.)
   - Paragraph organization
   - Use of examples, anecdotes, or data
   - How conclusions are drawn
3. **Note language detection**: Determine the language of the framework. All output must be in this same language.

### Phase 2: Section Development

For each section of the article:

#### Step 1: Rewrite Section Titles

Based on the framework content, create appropriate, engaging section titles that:
- Accurately reflect the section's content
- Are consistent with the article's tone
- Create logical flow between sections
- Are compelling for readers

Present the revised titles to the user for confirmation before proceeding.

#### Step 2: Write Section Content

Write complete content for the current section only. Do NOT proceed to the next section yet.

**Writing guidelines:**
- Match the language of the framework exactly
- Imitate the writing style from reference articles
- Develop clear arguments with supporting evidence
- Use appropriate examples or data
- Maintain logical flow within the section
- Consider the target audience's knowledge level

#### Step 3: Two-Level Review Cycle

After writing the section, conduct two rounds of review. For each round, list ALL identified issues clearly before moving to polishing.

**Round 1: Logical Review**
- Does each argument have matching evidence or examples?
- Are there logical gaps or jumps that readers might struggle to follow?
- Is the reasoning sound and well-supported?
- Does the section build toward a clear conclusion?

**Round 2: Reader Perspective Review**
Put yourself in the target reader's shoes:
- After reading this section, what questions would you have?
- Are there parts that are too abstract without concrete content?
- Are there sections that feel redundant or unnecessarily verbose?
- Is the content engaging and valuable for the intended audience?
- Would you need additional explanations or examples?

#### Step 4: Polishing Iterations

1. **List all issues** identified in both review rounds
2. **Revise the content** to address each issue systematically
3. **Re-run the review cycles** on the revised content
4. **Repeat** until no new issues are identified in either review round

**Important**: Each polishing iteration should address ALL identified issues from the previous review. Track which issues have been resolved.

#### Step 5: User Approval

When the section passes review with no remaining issues:
1. Present the polished section to the user
2. Explicitly request permission to proceed to the next section
3. Wait for explicit user confirmation before continuing

### Phase 3: Completion

After all sections are complete:
1. Review the entire article for overall coherence
2. Check transitions between sections
3. Ensure consistent tone and style throughout
4. Present the complete article to the user

## Output Format

**For each section iteration, present:**
```
## [Section Title]

### Draft Content
[Your draft text]

### Review Findings
**Logical Issues:**
1. [Issue 1]
2. [Issue 2]

**Reader Perspective Issues:**
1. [Issue 1]
2. [Issue 2]

### Revised Content (After Polishing)
[Polished text]

### Status
[Ready for next section / Needs further polishing]
```

**For final article:**
```
# [Article Title]

[Complete article with all sections]

## Summary
[Brief overview of the writing process and key improvements made]
```

## Common Pitfalls to Avoid

1. **Don't rush to next section**: Complete full review-polish cycles for each section before moving on.
2. **Don't ignore reference style**: Actively mimic the user's writing style from reference articles.
3. **Don't skip review rounds**: Both logical and reader perspective reviews are essential.
4. **Don't assume language**: Explicitly check and match the framework's language.
5. **Don't proceed without permission**: Always wait for user approval between sections.

## Adapting to Different Content Types

- **Technical articles**: Focus on accuracy, clear explanations, and appropriate detail level
- **Blog posts**: Emphasize engagement, readability, and personal voice
- **Reports**: Prioritize structure, data presentation, and executive summary
- **Tutorials**: Ensure step-by-step clarity, examples, and troubleshooting tips

Remember: The goal is to produce high-quality content that reflects the user's style, maintains logical coherence, and serves the reader's needs effectively.