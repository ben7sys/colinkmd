import re
import yaml
from markdown2 import markdown
from pathlib import Path

def parse_categories(lines):
    categories = []
    for line in lines:
        # Trim whitespace for accurate matching
        trimmed_line = line.strip()
        if trimmed_line.startswith('##'):
            # Remove '## ' to just get the category name
            category_name = trimmed_line[3:].strip()
            categories.append(category_name)
    return categories

def parse_basic_links(lines):
    """Parse basic Markdown links."""
    links = []
    for line in lines:
        trimmed_line = line.strip()
        if trimmed_line.startswith('['):
            links.append(trimmed_line)
    return links

def parse_link_details(link_line):
    # Regex to extract title and URL
    title_url_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    match = re.search(title_url_pattern, link_line)
    if not match:
        return None  # Return None if no match is found
    title, url = match.groups()

    # Extracting description, abbreviation, and icon
    desc_match = re.search(r'desc:([^+]+)', link_line)
    description = desc_match.group(1).strip() if desc_match else None

    abbr_match = re.search(r'abbr:([^+]+)', link_line)
    abbreviation = abbr_match.group(1).strip() if abbr_match else None

    icon_match = re.search(r'icon:([^+]+)', link_line)
    icon = icon_match.group(1).strip() if icon_match else None

    # Create a nested dictionary structure for YAML output
    return {title: {'href': url, 'description': description, 'abbr': abbreviation, 'icon': icon}}

def main():
    file_path = 'bookmarks.md'
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    categories = parse_categories(lines)
    links = parse_basic_links(lines)
    link_details = [parse_link_details(link) for link in links if parse_link_details(link) is not None]

    # Prepare a structured dictionary for YAML output
    yaml_data = [{'Gruppe': details} for details in link_details if details is not None]

    # Save data to a YAML file
    with open('bookmarks.yaml', 'w') as yaml_file:
        yaml.dump(yaml_data, yaml_file, allow_unicode=True, default_flow_style=False)

if __name__ == '__main__':
    main()

