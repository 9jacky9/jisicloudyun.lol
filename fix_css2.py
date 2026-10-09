import re

css_path = r'e:\1落地页\落地页\极速cloud\jisicloudyun.lol\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix the .page-header section
bad_css = '''\.page-header \{
  display: flex;
  align-items: center;
  padding: 16px 5%;
  background: var\(--surface\);
  position: sticky;
  top: 0;
  z-index: 9999;
  border-bottom: 1px solid var\(--border\);
  gap: 24px;
\}

header \.logo \{
  margin-right: auto;
\}'''

good_css = '''.page-header {
  text-align: center;
  padding: 80px 0 40px;
}'''

css = re.sub(bad_css, good_css, css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Fixed .page-header in style.css")
