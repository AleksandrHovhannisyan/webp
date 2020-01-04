#! /usr/bin/python
import os

def splitAtExtension(file):
    split = file.split('.')
    return split[0], split[1]

cwebp = 'cwebp'
gif2webp = 'gif2webp'

extensionToCommand = {
    'png': cwebp,
    'PNG': cwebp,
    'jpeg': cwebp,
    'JPEG': cwebp,
    'jpg': cwebp,
    'JPG': cwebp,
    'gif': gif2webp,
    'GIF': gif2webp,
    'webp': None
}

cwd = os.getcwd()

for file in os.listdir(cwd):
    img, ext = splitAtExtension(file)
    tool = extensionToCommand[ext]
    if tool:
        os.system("{} -q 80 {}.{} -o {}.webp".format(tool, img, ext, img))
        print('\n')