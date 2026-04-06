# FLAC Image Fixer

This project processes `.flac` files from the `music` folder, copies them into the `converted` folder, and rewrites any embedded artwork as non-progressive JPEG images.

## What It Does

Some players and devices are picky about embedded album art. This script keeps the audio file the same, but updates the embedded images so they are saved as baseline JPEG instead of progressive JPEG.

I made this with love for my sweet boy https://github.com/TheLalilulelo
## Project Structure

- `main.py`: the script that performs the conversion
- `music/`: put your source `.flac` files here
- `converted/`: processed files are written here

## Requirements

- Python
- `mutagen`
- `Pillow`

This project already includes a `pyproject.toml`, so you can install dependencies with your preferred Python environment tooling.

## How To Use

1. Put the `.flac` files you want to process inside the `music` folder.
2. Run the script from the project root:

```powershell
python main.py
```

3. Check the `converted` folder for the processed files.

## Logging

The script prints:

- the folders it is using
- each file being processed
- when the original file is copied
- each embedded image conversion
- a final summary of processed files and converted images

## Notes

- The original files in `music` are not modified.
- The script expects to be run from the project root so it can find the `music` and `converted` folders.
- Only files ending in `.flac` are processed.
