import os

packages={
    'sci-hub',
    'requests',
    'BeautifulSoup',
    'flask',
    'pdf2image',
    'poppler'
}

for pack in packages:
    os.system(f'pip3 install {pack}')
