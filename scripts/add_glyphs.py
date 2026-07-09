#!/usr/bin/env python3
"""
Adds broken link warning glyphs to markdown pages based on link_check_report.md.
"""
import os
import re
import sys

def parse_report(report_path):
    """
    Parses link_check_report.md and returns a grouped dictionary:
    { file_path: { line_number: [urls...] } }
    """
    # Pattern matching: | [Path](Path#Lline) | Line | `URL` | Status |
    row_pattern = re.compile(
        r'^\|\s*\[([^\]]+)\]\([^)]+\)\s*\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|'
    )
    
    entries = {}
    if not os.path.exists(report_path):
        print(f"Error: Report file '{report_path}' not found.", file=sys.stderr)
        sys.exit(1)
        
    with open(report_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = row_pattern.match(line)
            if match:
                file_path = match.group(1).strip()
                line_num = int(match.group(2))
                url = match.group(3).strip()
                
                if file_path not in entries:
                    entries[file_path] = {}
                if line_num not in entries[file_path]:
                    entries[file_path][line_num] = []
                if url not in entries[file_path][line_num]:
                    entries[file_path][line_num].append(url)
                    
    return entries

def modify_line_with_urls(line, urls, glyph=" ⚠️"):
    """
    Modifies a single line, placing the glyph outside markdown syntax 
    containers, processing right-to-left to prevent shifting indices.
    """
    occurrences = []
    for url in urls:
        start_idx = 0
        while True:
            idx = line.find(url, start_idx)
            if idx == -1:
                # Prefix matching fallback for slightly stripped/modified report URLs
                temp_url = url
                while temp_url and temp_url not in line:
                    temp_url = temp_url[:-1]
                if temp_url and len(temp_url) > 10:
                    idx = line.find(temp_url, start_idx)
                    url = temp_url
                else:
                    break
            
            if idx != -1:
                occurrences.append((idx, url))
                start_idx = idx + len(url)
            else:
                break
                
    # Sort descending by start index to modify from right to left
    occurrences.sort(key=lambda x: x[0], reverse=True)
    
    for idx, url in occurrences:
        # Determine context (Markdown, Autolink, or Raw)
        is_markdown = False
        if idx > 0 and line[idx - 1] == '(':
            is_markdown = True
        elif idx > 1 and line[idx - 1] in ('"', "'") and line[idx - 2] == '(':
            is_markdown = True
            
        if is_markdown:
            # Find matching closing parenthesis
            paren_count = 1
            close_idx = -1
            for i in range(idx, len(line)):
                if line[i] == '(':
                    paren_count += 1
                elif line[i] == ')':
                    paren_count -= 1
                    if paren_count == 0:
                        close_idx = i
                        break
            if close_idx != -1:
                after_part = line[close_idx + 1:]
                # Check for duplicate
                if not after_part.lstrip().startswith(glyph.strip()):
                    line = line[:close_idx + 1] + glyph + after_part
        else:
            # Check for autolink <url>
            if idx > 0 and line[idx - 1] == '<':
                close_idx = line.find('>', idx)
                if close_idx != -1:
                    after_part = line[close_idx + 1:]
                    if not after_part.lstrip().startswith(glyph.strip()):
                        line = line[:close_idx + 1] + glyph + after_part
                    continue
            
            # Raw URL
            after_part = line[idx + len(url):]
            if not after_part.lstrip().startswith(glyph.strip()):
                line = line[:idx + len(url)] + glyph + after_part
                
    return line

def main():
    report_path = "link_check_report.md"
    glyph = " ⚠️" # Yellow warning sign glyph
    
    print(f"Parsing '{report_path}'...")
    entries = parse_report(report_path)
    
    total_files = len(entries)
    total_modifications = sum(len(lines) for lines in entries.values())
    print(f"Found {total_modifications} broken link references across {total_files} files.")
    
    modified_files_count = 0
    modified_links_count = 0
    
    for file_path, line_data in entries.items():
        if not os.path.exists(file_path):
            print(f"Warning: File '{file_path}' not found. Skipping.")
            continue
            
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            
        file_modified = False
        
        # Process lines (1-based to 0-based indexing)
        for line_num, urls in line_data.items():
            idx = line_num - 1
            if idx < len(lines):
                original_line = lines[idx]
                modified_line = modify_line_with_urls(original_line, urls, glyph)
                if modified_line != original_line:
                    lines[idx] = modified_line
                    file_modified = True
                    modified_links_count += 1
            else:
                print(f"Warning: Line number {line_num} exceeds lines in '{file_path}'.")
                
        if file_modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            modified_files_count += 1
            print(f"Updated: {file_path}")
            
    print("\nGlyphs added successfully!")
    print(f"Updated {modified_links_count} links across {modified_files_count} files.")

if __name__ == "__main__":
    main()
