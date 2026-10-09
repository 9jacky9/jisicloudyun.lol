import os, glob, re

path = r'e:\1落地页\落地页\极速cloud\jisicloudyun.lol'
html_files = glob.glob(os.path.join(path, '*.html'))

header_html = '''    <header>
        <a href="index.html" class="logo">
           <svg width="36" height="36" viewBox="0 0 100 100">
             <defs>
               <linearGradient id="cloudGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                 <stop offset="0%" stop-color="#FF3366" />
                 <stop offset="50%" stop-color="#00C9A7" />
                 <stop offset="100%" stop-color="#FFD166" />
               </linearGradient>
               <clipPath id="cloudClip">
                 <path d="M73.5,35c-1.5-12-11.5-21-23.5-21c-9.5,0-18,5.5-21.5,14c-1-0.5-2-0.5-3.5-0.5c-8.5,0-15,6.5-15,15c0,8.5,6.5,15,15,15h47.5c11,0,20-9,20-20C92.5,42.5,84,35,73.5,35z"/>
               </clipPath>
             </defs>
             <rect width="100" height="100" fill="url(#cloudGrad)" clip-path="url(#cloudClip)" />
           </svg>
           <span>极速cloud</span>
        </a>
        <nav>
            <a href="index.html#features" class="nav-link">核心体验</a>
            <a href="index.html#streaming" class="nav-link">流媒体支持</a>
            <a href="index.html#pricing" class="nav-link">价格方案</a>
            <a href="index.html#faq" class="nav-link">常见问题</a>
            <a href="news.html" class="nav-link">灵感视界</a>
        </nav>
        <a href="https://ww012.twilightaff.com/#/?code=A56DH1Af" rel="nofollow" target="_blank" class="btn-primary header-cta">立即注册</a>
    </header>'''

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # If the file already has a header, we just replace it
    if '<header>' in content:
        content = re.sub(r'<header>.*?</header>', header_html, content, flags=re.DOTALL)
    else:
        # Article file: we need to transform it
        # Remove inline <style> block
        content = re.sub(r'<style>.*?</style>', '<link rel=\"stylesheet\" href=\"style.css\">', content, flags=re.DOTALL)
        
        # Replace <body> with <body>\nheader_html\n<main>\n<div class="page-header">\n<h1>Title</h1>\n</div>\n<div class="page-content">
        # Wait, simple: just insert header after <body>
        content = content.replace('<body>', '<body>\n' + header_html + '\n<main>')
        content = content.replace('</body>', '</main>\n</body>')
        content = content.replace('<div class=\"content-box\">', '<div class=\"page-content\">')
        
        # Change <h1>...</h1> to be inside page-header?
        # Let's extract h1 and move it
        h1_match = re.search(r'<h1>(.*?)</h1>', content)
        if h1_match:
            h1_text = h1_match.group(1)
            content = content.replace(h1_match.group(0), '')
            page_header = f'<div class=\"page-header\"><h1>{h1_text}</h1></div>'
            content = content.replace('<div class=\"page-content\">', page_header + '\n<div class=\"page-content\">')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Processed {os.path.basename(f)}')
