from mutagen.flac import FLAC
from PIL import Image
import os
import io
import shutil

base_dir = os.getcwd()

music_folder = os.path.join(base_dir, "music")
output_folder = os.path.join(base_dir, "converted")

os.makedirs(output_folder, exist_ok=True)

print("FLAC image fixer")
print("Base directory:", base_dir)
print("Input folder:", music_folder)
print("Output folder:", output_folder)

processed_files = 0
converted_images = 0

for file in os.listdir(music_folder):

    if file.lower().endswith(".flac"):

        input_path = os.path.join(music_folder, file)
        output_path = os.path.join(output_folder, file)

        print("Processing:", file)

        # copy original FLAC first
        shutil.copy2(input_path, output_path)
        print("Copied original file to:", output_path)

        audio = FLAC(output_path)
        file_picture_count = 0

        for picture in audio.pictures:

            if picture.mime.startswith("image/"):
                file_picture_count += 1
                print("Converting embedded image", file_picture_count, "in", file)

                img = Image.open(io.BytesIO(picture.data))

                buffer = io.BytesIO()
                img.save(buffer, "JPEG", progressive=False)

                picture.data = buffer.getvalue()
                picture.mime = "image/jpeg"
                converted_images += 1

        audio.save()
        processed_files += 1

        print("Converted", file_picture_count, "image(s) in", file)
        print("Saved:", output_path)

print("Processed files:", processed_files)
print("Converted images:", converted_images)
print("Done.")
