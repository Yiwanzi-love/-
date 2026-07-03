import os, re, markdown, yaml, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, 'docs')
PAGES = os.path.join(ROOT, 'pages')

HEAD = '''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title} - KB</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../assets/css/style.css"></head><body>'''

TAIL = '''<button class="mobile-menu-btn" onclick="document.getElementById('sidebar').classList.toggle('open')">☰</button>
<script>
function ts(b){var s=b.nextElementSibling;var a=b.querySelector('.arrow');if(!s||s.style.display=='none'||s.style.display==''){s.style.display='block';if(a)a.classList.add('open')}else{s.style.display='none';if(a)a.classList.remove('open')}}
function tm(){document.getElementById('sidebar').classList.toggle('open')}
document.addEventListener('DOMContentLoaded',function(){var p=window.location.pathname;document.querySelectorAll('.nav-item').forEach(function(i){var h=i.getAttribute('href');if(h&&(p==h||p==h+'index.html'||p.startsWith(h))){i.classList.add('active');var s=i.closest('.nav-section');if(s){var b=s.querySelector('.nav-section-toggle');if(b){b.nextElementSibling.style.display='block';var a=b.querySelector('.arrow');if(a)a.classList.add('open')}}}})})})
</script></body></html>'''

NAV = [['s','\u521b\u610f\u751f\u4ea7\u65b9\u6cd5\u8bba',[['\u6982\u8ff0','creative'],['\u91d1\u878d\u884c\u4e1a','creative/finance'],['\u6559\u80b2\u884c\u4e1a','creative/education'],['\u6848\u4f8b\u5e93','creative/cases']]],
['s','\u5e73\u53f0\u7d20\u6750\u751f\u6001',[['\u6982\u8ff0','platform'],['\u7b56\u7565\u4ecb\u7ecd','platform/strategy'],['\u4f9b\u7ed9\u65b9\u6cd5','platform/supply'],['\u6848\u4f8b\u5e93','platform/cases']]],
['l','\u4e2a\u4eba\u5de5\u5177\u5e93','toolkit'],['l','\u6807\u7b7e','tags'],['l','\u642d\u5efa\u8bb0\u5f55','buildlog']]

SIDEBAR = '<aside class=sidebar id=sidebar><div class=sidebar-header><a href=../../ class=sidebar-logo style=text-decoration:none;color:inherit><span class=sidebar-logo-img>K</span> \u4e2a\u4eba\u77e5\u8bc6\u5e93</a></div><nav class=sidebar-nav>'
for n in NAV:
    if n[0]=='s':
        SIDEBAR += '<div class=nav-section><button class=nav-section-toggle onclick=ts(this)><span class=arrow>\u25b6</span> '+n[1]+'</button><div class=nav-sub style=display:none>'
        for c in n[2]: SIDEBAR += '<a href=pages/'+c[1]+'/ class=nav-item>'+c[0]+'</a>'
        SIDEBAR += '</div></div>'
    else: SIDEBAR += '<a href=pages/'+n[2]+'/ class=nav-item style=display:block;padding:0.35rem 0.9rem>'+n[1]+'</a>'
SIDEBAR += '</nav></aside>'

PATHMAP = {'\u521b\u610f\u751f\u4ea7\u65b9\u6cd5\u8bba/index':'creative','\u521b\u610f\u751f\u4ea7\u65b9\u6cd5\u8bba/\u91d1\u878d\u884c\u4e1a':'creative/finance','\u521b\u610f\u751f\u4ea7\u65b9\u6cd5\u8bba/\u6559\u80b2\u884c\u4e1a':'creative/education','\u521b\u610f\u751f\u4ea7\u65b9\u6cd5\u8bba/\u6848\u4f8b\u5e93':'creative/cases','\u521b\u610f\u7b56\u7565-\u5e73\u53f0\u7d20\u6750\u751f\u6001\u65b9\u5411/index':'platform','\u521b\u610f\u7b56\u7565-\u5e73\u53f0\u7d20\u6750\u751f\u6001\u65b9\u5411/\u7b56\u7565\u4ecb\u7ecd':'platform/strategy','\u521b\u610f\u7b56\u7565-\u5e73\u53f0\u7d20\u6750\u751f\u6001\u65b9\u5411/\u4f9b\u7ed9\u65b9\u6cd5':'platform/supply','\u521b\u610f\u7b56\u7565-\u5e73\u53f0\u7d20\u6750\u751f\u6001\u65b9\u5411/\u6848\u4f8b\u5e93':'platform/cases','\u4e2a\u4eba\u5de5\u5177\u5e93':'toolkit','tags':'tags','\u9879\u76ee\u642d\u5efa\u8bb0\u5f55':'buildlog'}

def parse(fp):
    with open(fp,encoding='utf-8') as f: c = f.read().lstrip()
    fm = {'title':'','tags':[]}
    b = c
    if c.startswith('---'):
        p = c.split('---',2)
        if len(p)>=3:
            try: d=yaml.safe_load(p[1]); fm.update(d)
            except: pass
            b = p[2].strip()
    b = re.sub(r'<!--.*?-->','',b,flags=re.DOTALL)
    md = markdown.Markdown(extensions=['admonition','pymdownx.details','pymdownx.superfences','pymdownx.highlight','attr_list','md_in_html','footnotes','tables','toc'])
    return fm, md.convert(b)

def gen():
    if os.path.exists(PAGES): shutil.rmtree(PAGES)
    os.makedirs(PAGES, exist_ok=True)
    n = 0
    for r,d,fs in os.walk(DOCS):
        for fn in fs:
            if not fn.endswith('.md'): continue
            fp = os.path.join(r,fn)
            rel = os.path.relpath(fp,DOCS).replace('\\','/')
            rn = os.path.splitext(rel)[0]
            if rn in ('index',''): continue
            dst = PATHMAP.get(rn)
            if not dst: continue
            d = os.path.join(PAGES,dst)
            fm,html = parse(fp)
            title = fm.get('title','') or dst.split('/')[-1]
            tg = '<div class=page-tags>'+''.join('<span class=page-tag>'+t+'</span>' for t in fm.get('tags',[]))+'</div>' if fm.get('tags') else ''
            body = HEAD.format(title=title)+'<div class=app>'+SIDEBAR+'<main class=main><article><div class=page-header><h1>'+title+'</h1>'+tg+'</div><div class=page-content>'+html+'</div></article></main></div>'+TAIL
            os.makedirs(d,exist_ok=True)
            with open(os.path.join(d,'index.html'),'w',encoding='utf-8') as f: f.write(body)
            n+=1
    print(f'\u6784\u5efa\u5b8c\u6210\uff0c\u5171 {n} \u4e2a\u9875\u9762')

if __name__ == '__main__': gen()
# Knowledge base build script
