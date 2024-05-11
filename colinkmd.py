import re
import yaml
from markdown2 import markdown
from pathlib import Path

def parse_categories_and_links(lines):
    data = {}
    current_category = None

    for line in lines:
        trimmed_line = line.strip()
        if trimmed_line.startswith('##'):
            # Neuen Kategoriennamen als aktuellen Schlüssel festlegen
            current_category = trimmed_line[3:].strip()
            data[current_category] = []
        elif trimmed_line.startswith('['):
            # Linkdetails parsen und der aktuellen Kategorie hinzufügen
            link_details = parse_link_details(trimmed_line)
            if link_details and current_category:
                data[current_category].append(link_details)

    return data

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
    
    data = parse_categories_and_links(lines)

    # Eigene Funktion zur Behandlung von None-Werten, die im YAML als leere Strings erscheinen
    def none_representer(dumper, data):
        return dumper.represent_scalar('tag:yaml.org,2002:null', '')
    
    # Registriere den eigenen Repräsentierer für den Typ None
    yaml.add_representer(type(None), none_representer)

    # Save data to a YAML file
    with open('bookmarks.yaml', 'w') as yaml_file:
        yaml.dump(data, yaml_file, allow_unicode=True, default_flow_style=False)

if __name__ == '__main__':
    main()
