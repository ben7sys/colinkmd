import re
import yaml
from markdown2 import markdown
from pathlib import Path

def parse_markdown(file_path):
    content = Path(file_path).read_text()
    lines = content.split('\n')
    bookmarks = {}
    current_category = None

    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)\s*(desc:[^\+]+)?\s*\+\+\s*abbr:([^\s]+)\s*\+\+\s*icon:([^\s]+)'
    simple_link_pattern = r'^\s*http[s]?://[^\s]+$'
    
    for line in lines:
        if line.startswith('## '):
            current_category = line.strip('# ').strip()
            bookmarks[current_category] = []
        elif re.match(link_pattern, line):
            match = re.match(link_pattern, line)
            title, url, description, abbr, icon = match.groups()
            description = description.split('desc:')[1].strip() if description else "Keine Beschreibung"
            bookmarks[current_category].append({
                'title': title,
                'href': url,
                'description': description,
                'abbr': abbr,
                'icon': icon
            })
        elif re.match(simple_link_pattern, line):
            bookmarks[current_category].append({
                'href': line.strip()
            })

    return bookmarks

def convert_to_yaml(bookmarks, output_file):
    with open(output_file, 'w') as f:
        yaml.dump([{'Gruppe': bookmarks[category]} for category in bookmarks], f, allow_unicode=True)

def main():
    input_md = 'bookmarks.md'
    output_yaml = 'bookmarks.yaml'
    bookmarks = parse_markdown(input_md)
    convert_to_yaml(bookmarks, output_yaml)
    print(f'YAML file created at {output_yaml}')

if __name__ == '__main__':
    main()
