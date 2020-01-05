#! /usr/bin/python
import os
import sys
    
cwebp = 'cwebp'
gif2webp = 'gif2webp'

# This dict ensures we don't even attempt to process files whose extensions are not in here.
# We certainly could attempt to do that, but then the output would be cluttered with cwebp errors.
# Also, webp is mapped to None so we don't try to re-process the webp files that this script generates.
extensionMap = {
    'png': cwebp,
    'jpeg': cwebp,
    'jpg': cwebp,
    'jpe': cwebp,
    'jif': cwebp,
    'jfif': cwebp,
    'jfi': cwebp,
    'jp2': cwebp,
    'j2k': cwebp,
    'jpf': cwebp,
    'jpx': cwebp,
    'jpm': cwebp,
    'mj2': cwebp,
    'tiff': cwebp,
    'gif': gif2webp,
    'GIF': gif2webp,
    'webp': None
}

def split_at_extension(file):
    parts = file.split('.')
    if len(parts) == 2:
        return parts[0], parts[1].lower()
    return parts[0], None

def main():
    if len(sys.argv) == 1:
        print("webp: No target directory provided. Exiting.")
        sys.exit(1)

    # Any valid options that cwebp accepts; if invalid options are provided, the tool will complain anyway
    options = str.join(' ', sys.argv[1:-1])

    # Assume the user is competent and provides this
    target_dir = sys.argv[-1]

    # Walk the directory
    for file in os.listdir(target_dir):
        img, ext = split_at_extension(file)
        # Skip files with no extension
        if not ext:
            continue

        # To prevent a key error, we have to check if ext is in the map
        conversion_tool = extensionMap[ext] if ext in extensionMap else None

        # conversion_tool may be None if the file's extension is 'webp', for example, since we don't
        # want to reprocess files we've generated ourselves
        if not conversion_tool:
            continue
        
        img_path = os.path.join(target_dir, img)
        os.system("{} {} {}.{} -o {}.webp".format(conversion_tool, options, img_path, ext, img_path))
        print('\n')
            

if __name__ == "__main__":
    main()