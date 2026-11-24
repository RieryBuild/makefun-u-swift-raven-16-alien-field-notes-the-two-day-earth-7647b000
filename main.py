import os

# Alien Field Notes: The Two Day Earth Review — an alien tourist's one-line
# review of planet Earth. Chosen line (107 chars / 107 bytes, ASCII only):
# the locals pre-wash their dishes before loading the machine that washes
# dishes, then dismiss the machine as purely decorative. Single joke, punch at the end.
LINE = "Earth: the locals wash their dishes before loading the machine that washes dishes. 4/5 - purely decorative."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
