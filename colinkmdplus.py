import re
import yaml


def parse_categories_and_links(lines):
    data = []
    current_category = None
    current_links = []

    for line in lines:
        trimmed_line = line.strip()
        if trimmed_line.startswith('##'):
            if current_category is not None:
                # Füge die vorherige Kategorie und ihre Links der Hauptliste hinzu
                data.append({current_category: current_links})
            # Starte eine neue Kategorie
            current_category = trimmed_line[3:].strip()
            current_links = []
        elif trimmed_line.startswith('[') or trimmed_line.startswith('http') or trimmed_line.startswith('www'):
            link_details = parse_link_details(trimmed_line)
            if link_details:
                current_links.append(link_details)

    # Vergiss nicht, die letzte Kategorie und ihre Links hinzuzufügen
    if current_category is not None:
        data.append({current_category: current_links})

    return data

def parse_link_details(link_line):
    # Handle simple links that start directly with 'http' or 'www'
    if link_line.startswith('http') or link_line.startswith('www'):
        url = link_line
        title = url.split('//')[-1]  # Use the part after '//' as a simple title
        return {title: [{'href': url, 'description': '', 'abbr': '', 'icon': ''}]}

    # Regex to extract title and URL for formatted links
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

    return {title: [{'href': url, 'description': description, 'abbr': abbreviation, 'icon': icon}]}


def main():
    file_path = 'bookmarks.md'
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = parse_categories_and_links(lines)

    # Eigene Funktion zur Behandlung von None-Werten, die im YAML als leere Strings erscheinen
    def none_representer(dumper, data):
        return dumper.represent_scalar('tag:yaml.org,2002:null', '')
    yaml.add_representer(type(None), none_representer)

    # Save data to a YAML file
    with open('bookmarks.yaml', 'w') as yaml_file:
        yaml.dump(data, yaml_file, allow_unicode=True, default_flow_style=False)

if __name__ == '__main__':
    main()

