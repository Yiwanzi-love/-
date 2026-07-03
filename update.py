import shutil, os
from pathlib import Path

ROOT = Path(__file__).parent
PAGES = ROOT / 'pages'

shutil.copy2(ROOT / 'index.html', PAGES / 'index.html')

assets_dst = PAGES / 'assets'
if assets_dst.exists():
    shutil.rmtree(assets_dst)
shutil.copytree(ROOT / 'assets', assets_dst)

for f in (PAGES / 'assets').rglob('*.md'):
    f.unlink()

print('Updated pages/ with homepage and assets')