import os

python_packages={
    'sci-hub',
    'flask',
    'pdf2image',
    'opencv-python',
    # 'python3-opencv'
}

for pack in python_packages:
    os.system(f'pip3 install {pack}')

ubuntu_packages={
    'poppler-utils',
    'libgl1-mesa-dev'
}
for pack in ubuntu_packages:
    os.system(f'sudo apt install {pack}')