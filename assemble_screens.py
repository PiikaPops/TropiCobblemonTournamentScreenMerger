from PIL import Image
import os
import math
import sys

SCREEN_DIR = "screen"
OUTPUT_FILE = "assembled.png"
COLS = 3
TARGET_W = 390
TARGET_H = 220
EXTENSIONS = (".png", ".jpg", ".jpeg")

files = sorted(
    f for f in os.listdir(SCREEN_DIR)
    if f.lower().endswith(EXTENSIONS)
)

if not files:
    print("Aucune image trouvee dans le dossier screen/")
    input("Appuyez sur Entree pour fermer...")
    sys.exit(1)

ROWS = math.ceil(len(files) / COLS)

images = []
for f in files:
    img = Image.open(os.path.join(SCREEN_DIR, f))
    img = img.resize((TARGET_W, TARGET_H), Image.LANCZOS)
    images.append(img)

result = Image.new("RGB", (COLS * TARGET_W, ROWS * TARGET_H))

for idx, img in enumerate(images):
    col = idx % COLS
    row = idx // COLS
    result.paste(img, (col * TARGET_W, row * TARGET_H))

result.save(OUTPUT_FILE)
print(f"Image assemblee sauvegardee dans {OUTPUT_FILE} ({result.size[0]}x{result.size[1]}) - {len(images)} images")
input("Appuyez sur Entree pour fermer...")
