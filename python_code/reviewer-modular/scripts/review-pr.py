#!/usr/bin/env python3
"""
AI PR Reviewer using OpenAI ChatGPT API
Automatically reviews pull requests and posts feedback as comments
"""

import os
import sys
from datetime import datetime
from openai import OpenAI
from github import Github

# ==================== Configuration ====================

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
PR_NUMBER = int(os.environ.get('PR_NUMBER', 0))
PR_TITLE = os.environ.get('PR_TITLE', '')
PR_AUTHOR = os.environ.get('PR_AUTHOR', '')
REPO_OWNER = os.environ.get('REPO_OWNER', '')
REPO_NAME = os.environ.get('REPO_NAME', '')

# Model configuration
GPT_MODEL = 'gpt-4o'  # Options: 'gpt-4o', 'gpt-4-turbo', 'gpt-3.5-turbo'
MAX_DIFF_SIZE = 100000  # Maximum characters in diff
MAX_TOKENS = 2500  # Maximum tokens for response
TEMPERATURE = 0.3  # Lower = more focused, Higher = more creative

# ==================== Main Function ====================

def main():
    """Main execution function"""
    try:
        print('🤖 Starting ChatGPT PR Review...')
        print(f'📝 PR #{PR_NUMBER}: {PR_TITLE}')
        print(f'👤 Author: @{PR_AUTHOR}')
        print(f'🏢 Repository: {REPO_OWNER}/{REPO_NAME}')
        print(f'🤖 Model: {GPT_MODEL}')
        print('-' * 50)
        
        # Validate environment variables
        validate_environment()
        
        # Read PR diff
        diff = read_diff()
        
        # Validate diff
        if not diff.strip():
            post_comment('ℹ️ **No changes detected** in this pull request.')
            print('ℹ️ No changes to review')
            return
        
        # Check diff size
        if len(diff) > MAX_DIFF_SIZE:
            handle_large_diff(len(diff))
            return
        
        print(f'📊 Analyzing {len(diff):,} characters of code changes...')
        
        # Read PR description
        pr_description = read_pr_description()
        
        # Get AI review
        review = get_ai_review(diff, pr_description)
        
        # Post review
        post_comment(review)
        
        print('✅ ChatGPT Review posted successfully!')
        print(f'🔗 View PR: https://github.com/{REPO_OWNER}/{REPO_NAME}/pull/{PR_NUMBER}')
        
    except Exception as e:
        print(f'❌ Error during PR review: {e}')
        handle_error(e)
        sys.exit(1)

# ==================== Validation ====================

def validate_environment():
    """Validate required environment variables"""
    required_vars = {
        'OPENAI_API_KEY': OPENAI_API_KEY,
        'GITHUB_TOKEN': GITHUB_TOKEN,
        'PR_NUMBER': PR_NUMBER,
        'REPO_OWNER': REPO_OWNER,
        'REPO_NAME': REPO_NAME,
    }
    
    missing = [key for key, value in required_vars.items() if not value]
    
    if missing:
        raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
    
    print('✓ Environment variables validated')

# ==================== File Reading ====================

def read_diff():
    """Read the PR diff from file"""
    try:
        with open('pr-diff.txt', 'r', encoding='utf-8') as f:
            diff = f.read()
        print(f'✓ Read diff file ({len(diff):,} characters)')
        return diff
    except FileNotFoundError:
        raise FileNotFoundError('pr-diff.txt not found. Ensure workflow generates this file.')
    except Exception as e:
        raise Exception(f'Error reading diff file: {e}')

def read_pr_description():
    """Read the PR description from file"""
    try:
        with open('pr-description.txt', 'r', encoding='utf-8') as f:
            description = f.read().strip()
        if description and description != 'null':
            print(f'✓ Read PR description ({len(description)} characters)')
            return description
        return 'No description provided'
    except FileNotFoundError:
        return 'No description provided'
    except Exception:
        return 'No description provided'

# ==================== AI Review ====================

def get_ai_review(diff, pr_description):
    """Get AI code review from OpenAI"""
    print(f'🧠 Requesting ChatGPT analysis using model: {GPT_MODEL}...')
    
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        system_prompt = create_system_prompt()
        user_prompt = create_user_prompt(diff, pr_description)
        
        # Make API call
        completion = client.chat.completions.create(
            model=GPT_MODEL,
            messages=[
                {
                    'role': 'system',
                    'content': system_prompt,
                },
                {
                    'role': 'user',
                    'content': user_prompt,
                },
            ],
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
        )
        
        # Extract response
        review = completion.choices[0].message.content
        
        # Log token usage
        tokens_used = completion.usage.total_tokens
        tokens_prompt = completion.usage.prompt_tokens
        tokens_completion = completion.usage.completion_tokens
        
        print(f'💰 Tokens used: {tokens_used:,} (prompt: {tokens_prompt:,}, completion: {tokens_completion:,})')
        print(f'✓ Received review ({len(review):,} characters)')
        
        return review
        
    except Exception as e:
        raise Exception(f'OpenAI API error: {e}')

def create_system_prompt():
    """Create system prompt for the AI"""
    return """You are an experienced senior software engineer conducting a thorough code review.
Your role is to provide constructive, actionable feedback on pull requests.

Guidelines for your review:
- Be thorough but concise
- Focus on significant issues, not nitpicks
- Provide specific examples and suggestions
- Be encouraging and constructive
- Consider security, performance, maintainability, and best practices
- Use emojis to make the review engaging and easy to scan
- Reference specific files and line numbers when possible
- Prioritize issues by severity (🔴 Critical, 🟡 Medium, 🟢 Minor)

Your goal is to help improve code quality while being respectful and educational."""

def create_user_prompt(diff, pr_description):
    """Create user prompt with PR details"""
    return f"""Review this pull request:

**PR Title:** {PR_TITLE}
**Author:** @{PR_AUTHOR}
**Description:** 
{pr_description}

**Code Changes:**
```diff
{diff}
```

Provide a comprehensive code review in the following format:

## 📋 Summary
[Provide a 2-3 sentence overview of what this PR does and its purpose]

## ✅ Strengths
[List 2-4 things that are done well - be specific and encouraging]

## 🔍 Issues & Concerns
[List any problems found with severity indicators:
- 🔴 Critical: Security issues, bugs, breaking changes
- 🟡 Medium: Code quality, potential bugs, performance
- 🟢 Minor: Style, naming, minor improvements

Include file names and approximate line numbers when possible]

## 💡 Suggestions
[Provide actionable improvement recommendations. Include code examples where helpful]

## 🧪 Testing Recommendations
[Suggest specific test cases, edge cases, or testing strategies]

## 📚 Documentation
[Identify any documentation needs, missing comments, or unclear code]

## 🎯 Overall Assessment
[Provide a clear verdict:
- ✅ Approve with minor changes
- ⚠️ Needs work before merging  
- 🚫 Major concerns - significant changes required

Include a brief summary of next steps]

Be specific, reference actual code when possible, and provide actionable feedback that helps the author improve."""
