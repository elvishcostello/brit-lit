#!/usr/bin/env python3
import re
import sys

def slugify(text):
    """Convert heading text to hashtag format"""
    text = re.sub(r'^#+\s*', '', text)
    text = text.lower().strip()
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'[^\w-]', '', text)
    return text

def strip_formatting(text):
    """Remove inline markdown formatting"""
    # Remove bold: **text** or __text__
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'__(.+?)__', r'\1', text)
    # Remove italic: *text* or _text_
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'_(.+?)_', r'\1', text)
    # Remove code: `text`
    text = re.sub(r'`(.+?)`', r'\1', text)
    # Remove strikethrough: ~~text~~
    text = re.sub(r'~~(.+?)~~', r'\1', text)
    # Remove links: [text](url) -> text
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    return text.strip()


def process_markdown(filename):
    current_heading = None
    
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            
            if line.startswith('#'):
                current_heading = slugify(line)

            elif line.strip().startswith('* ') or line.strip().startswith('- '):
                item = strip_formatting(line.strip()[2:])
          
                if current_heading:
                    print(f"* {item} #{current_heading}")
                # else:
                #     print(f"* {item}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python pivot_markdown.py <markdown_file>", file=sys.stderr)
        sys.exit(1)
    
    process_markdown(sys.argv[1])
