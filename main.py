from mutagen.flac import FLAC
from PIL import Image
import os
import io
import shutil

base_dir = os.getcwd()

music_folder = os.path.join(base_dir, "music")
output_folder = os.path.join(base_dir, "converted")

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(music_folder):

    if file.lower().endswith(".flac"):

        input_path = os.path.join(music_folder, file)
        output_path = os.path.join(output_folder, file)

        print("Processing:", file)

        # copy original FLAC first
        shutil.copy2(input_path, output_path)

        audio = FLAC(output_path)

        for picture in audio.pictures:

            if picture.mime.startswith("image/"):

                img = Image.open(io.BytesIO(picture.data))

                buffer = io.BytesIO()
                img.save(buffer, "JPEG", progressive=False)

                picture.data = buffer.getvalue()
                picture.mime = "image/jpeg"

        audio.save()

        print("Saved:", output_path)

print("Done.")