"""
Generates demo images for alineas_demo module.
Run with the Odoo venv python:
  /Users/neppoz/odoo-dev/19/venv/bin/python generate_images.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.dirname(__file__)

# ── Colour palette ─────────────────────────────────────────────────────────────
ALPINE_BLUE   = (30,  80, 140)
ALPINE_GREEN  = (40, 120,  70)
ALPINE_SNOW   = (240, 245, 250)
ALPINE_GREY   = (100, 110, 120)
GOLD          = (195, 155,  60)
WHITE         = (255, 255, 255)
DARK          = ( 30,  35,  45)

# ── Helpers ────────────────────────────────────────────────────────────────────

def _font(size):
    try:
        return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
    except Exception:
        return ImageFont.load_default()


def _save(img, name):
    path = os.path.join(OUT, name)
    img.save(path, "PNG", optimize=True)
    print(f"  saved {name}")


# ── Company logo ───────────────────────────────────────────────────────────────

def make_company_logo():
    W, H = 400, 200
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # Background card
    d.rounded_rectangle([0, 0, W - 1, H - 1], radius=18, fill=ALPINE_BLUE)

    # Mountain silhouette
    mountains = [
        (0, H), (60, 90), (120, 130), (180, 55), (240, 110), (300, 70), (360, 115), (400, 80), (400, H)
    ]
    d.polygon(mountains, fill=ALPINE_GREEN)
    # Snow caps
    d.polygon([(155, 75), (180, 55), (205, 75), (190, 65), (170, 65)], fill=ALPINE_SNOW)
    d.polygon([(278, 85), (300, 70), (322, 85), (308, 76), (292, 76)], fill=ALPINE_SNOW)

    # Company name
    d.text((W // 2, 140), "Alpenvision", font=_font(38), fill=WHITE, anchor="mm")
    d.text((W // 2, 172), "GmbH  ·  Bozen", font=_font(16), fill=ALPINE_SNOW, anchor="mm")

    _save(img, "company_logo.png")


# ── User avatar ────────────────────────────────────────────────────────────────

def make_user_avatar():
    S = 256
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # Circle background
    d.ellipse([0, 0, S, S], fill=ALPINE_BLUE)

    # Inner lighter circle
    m = 18
    d.ellipse([m, m, S - m, S - m], fill=(50, 110, 180))

    # Initials
    d.text((S // 2, S // 2 + 4), "NP", font=_font(88), fill=WHITE, anchor="mm")

    # Gold ring
    d.ellipse([4, 4, S - 4, S - 4], outline=GOLD, width=5)

    _save(img, "user_avatar.png")


# ── Product images ─────────────────────────────────────────────────────────────

PRODUCTS = [
    # (filename, label, bg_color, icon_char)
    ("prod_beratung_basis.png",    "Beratung\nBasis",       (52, 100, 170),  "💼"),
    ("prod_beratung_experte.png",  "Beratung\nExperte",     (30,  70, 140),  "🎓"),
    ("prod_it_support.png",        "IT-Support\nPauschal",  (40, 130, 110),  "🖥"),
    ("prod_software_abo.png",      "Software\nAbo",         (80,  60, 160),  "📦"),
    ("prod_wartung.png",           "Wartungs-\nvertrag",    (50, 120,  80),  "🔧"),
    ("prod_transport.png",         "Transport",             (180, 120, 30),  "🚚"),
    ("prod_laptop.png",            "Laptop\nBusiness",      (40,  80, 150),  "💻"),
    ("prod_monitor.png",           "Monitor\n27\" 4K",      (50,  90, 160),  "🖥"),
    ("prod_burostuhl.png",         "Bürostuhl\nErgo",       (100, 130,  70),  "🪑"),
    ("prod_schreibtisch.png",      "Schreibtisch\nElektr.", (120, 100,  50),  "🪟"),
    ("prod_drucker.png",           "Drucker\nMulti",        (80, 100, 130),  "🖨"),
    ("prod_stahlrohr.png",         "Stahlrohr\nDN50",       (90,  90,  90),  "⚙️"),
    ("prod_aluminium.png",         "Alu-Blech\n2mm",        (130, 140, 150),  "🔩"),
    ("prod_holzbalken.png",        "Holzbalken\n10×10",     (140, 100,  50),  "🪵"),
    ("prod_schrauben.png",         "Schrauben\nSortiment",  (100,  80,  60),  "🔩"),
    ("prod_reinigung.png",         "Reinigungs-\nmittel",   (60, 150, 140),  "🧴"),
    ("prod_sicherheit.png",        "Sicherheits-\nAusrüst.", (200, 80, 50),  "🦺"),
    ("prod_palette.png",           "Transport-\npalette",   (160, 120,  40),  "📦"),
    ("prod_messinstrument.png",    "Messinstr.\nkalib.",    (70, 100, 160),  "📏"),
]


def make_product_image(filename, label, bg, icon):
    W, H = 300, 300
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # Background
    d.rounded_rectangle([0, 0, W - 1, H - 1], radius=20, fill=bg)

    # Lighter top strip
    light = tuple(min(255, c + 40) for c in bg)
    d.rounded_rectangle([0, 0, W - 1, H // 2], radius=20, fill=light)
    d.rectangle([0, H // 2 - 20, W, H // 2], fill=light)

    # Icon (large, centred top half)
    d.text((W // 2, H // 4), icon, font=_font(72), fill=(255, 255, 255, 200), anchor="mm")

    # Divider line
    d.line([(20, H // 2 + 5), (W - 20, H // 2 + 5)], fill=(255, 255, 255, 80), width=1)

    # Label (bottom half)
    lines = label.split("\n")
    for i, line in enumerate(lines):
        y = H // 2 + 40 + i * 38
        d.text((W // 2, y), line, font=_font(28), fill=WHITE, anchor="mm")

    _save(img, filename)


# ── Main ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Generating demo images ...")
    make_company_logo()
    make_user_avatar()
    for args in PRODUCTS:
        make_product_image(*args)
    print("Done.")
