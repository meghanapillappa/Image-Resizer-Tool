import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(800, 600), new_format="PNG"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Skip non-image files
        if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
            continue

        try:
            with Image.open(file_path) as img:
                # Resize
                img_resized = img.resize(size)

                # Change extension if converting
                base_name, _ = os.path.splitext(filename)
                new_filename = f"{base_name}.{new_format.lower()}"
                save_path = os.path.join(output_folder, new_filename)

                # Save
                img_resized.save(save_path, new_format.upper())
                print(f"✅ Saved: {save_path}")
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

# ---- Call function here with updated input path ----
resize_images(
    r"C:\Users\karth\Desktop\input_image",
    r"C:\Users\karth\Desktop\output_images",
    size=(400, 400),
    new_format="PNG"
)
