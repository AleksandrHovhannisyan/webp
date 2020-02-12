# webp

> A CLI tool that converts all valid images and GIFs in a directory to a WebP equivalent.

## Getting Started

1. Download `webp.py`.

2. Run `chmod a+x webp.py`.

3. Create a soft link to the script using `sudo ln -s /path/to/downloads/webp.py /usr/bin/webp`.

4. Install the appropriate [libwebp precompiled utilities](https://developers.google.com/speed/webp/docs/precompiled) from Google.

## Usage and Syntax

The tool converts all valid images in a directory to webp and generates the output files for those images. Static images are converted using the `cwebp` CLI utility. Animated GIFs are converted using the `gif2webp` utility that comes with the download.

Syntax:

> webp [options] path/to/images

For a list of options, please see [Google's documentation for cwebp](https://developers.google.com/speed/webp/docs/cwebp).

Example usage:

```bash
webp -q 80 ~/img/
```

**Note**: If you're using WSL on Windows, copy the directory from File Explorer and feed it to the built-in `wslpath` utility:

```bash
webp [options] "$(wslpath "/path/to/images")"
```
