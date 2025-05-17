import os
import yaml
import markdown
from nbconvert import HTMLExporter

# Paths
REGISTRY_PATH = 'registry.yaml'
AUTHORS_PATH = 'authors.yaml'
EXAMPLES_DIR = 'examples'
WIKI_DIR = 'wiki'
OUTPUT_DIR = 'site'

# Ensure output directory exists
def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Load YAML files
def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# Convert notebook to HTML
def notebook_to_html(nb_path):
    exporter = HTMLExporter()
    exporter.exclude_input_prompt = True
    exporter.exclude_output_prompt = True
    body, _ = exporter.from_filename(nb_path)
    return body

# Convert markdown to HTML
def markdown_to_html(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return markdown.markdown(text)

# Render a simple HTML page with metadata
def render_html(title, authors, date, tags, content, author_info):
    author_html = ''
    for author in authors:
        info = author_info.get(author, {})
        name = info.get('name', author)
        website = info.get('website', '#')
        avatar = info.get('avatar', '')
        author_html += f'<div><img src="{avatar}" width="32" style="vertical-align:middle;"> <a href="{website}">{name}</a></div>'
    tags_html = ', '.join(tags)
    return f'''
    <html>
    <head><title>{title}</title></head>
    <body>
        <h1>{title}</h1>
        <div><strong>Date:</strong> {date}</div>
        <div><strong>Authors:</strong> {author_html}</div>
        <div><strong>Tags:</strong> {tags_html}</div>
        <hr>
        {content}
    </body>
    </html>
    '''

def main():
    ensure_dir(OUTPUT_DIR)
    registry = load_yaml(REGISTRY_PATH)
    authors = load_yaml(AUTHORS_PATH)

    for entry in registry:
        path = entry['path']
        title = entry.get('title', 'Untitled')
        date = entry.get('date', '')
        entry_authors = entry.get('authors', [])
        tags = entry.get('tags', [])

        # Determine file type and convert
        if path.endswith('.ipynb'):
            src_path = os.path.join(EXAMPLES_DIR, os.path.basename(path))
            if not os.path.exists(src_path):
                print(f"Notebook not found: {src_path}")
                continue
            content = notebook_to_html(src_path)
        elif path.endswith('.md'):
            # Could be in examples/ or wiki/
            src_path = os.path.join(EXAMPLES_DIR, os.path.basename(path))
            if not os.path.exists(src_path):
                src_path = os.path.join(WIKI_DIR, os.path.basename(path))
            if not os.path.exists(src_path):
                print(f"Markdown not found: {src_path}")
                continue
            content = markdown_to_html(src_path)
        else:
            print(f"Unsupported file type: {path}")
            continue

        html = render_html(title, entry_authors, date, tags, content, authors)
        out_name = os.path.splitext(os.path.basename(path))[0] + '.html'
        out_path = os.path.join(OUTPUT_DIR, out_name)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Generated: {out_path}")

if __name__ == '__main__':
    main() 