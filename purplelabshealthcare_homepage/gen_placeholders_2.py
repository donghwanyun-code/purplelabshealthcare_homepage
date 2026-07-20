from PIL import Image, ImageDraw, ImageFont
import os

OUT = "/sessions/upbeat-gifted-turing/mnt/outputs/images"
os.makedirs(OUT, exist_ok=True)

def find_font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

def make_placeholder(name, w, h, label, sub, c1=(255,214,224), c2=(255,241,235)):
    img = Image.new("RGB", (w, h), c1)
    draw = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(h-1,1)
        r = int(c1[0] + (c2[0]-c1[0])*t)
        g = int(c1[1] + (c2[1]-c1[1])*t)
        b = int(c1[2] + (c2[2]-c1[2])*t)
        draw.line([(0,y),(w,y)], fill=(r,g,b))
    draw.rectangle([0,0,w-1,h-1], outline=(220,180,190), width=2)
    margin = min(w,h)//12
    draw.rectangle([margin,margin,w-margin,h-margin], outline=(200,150,165), width=2)
    font_size = max(16, min(w,h)//14)
    font = find_font(font_size, bold=True)
    sub_font = find_font(max(12,font_size//2))
    tw = draw.textlength(label, font=font)
    draw.text(((w-tw)/2, h/2 - font_size), label, fill=(120,60,80), font=font)
    tw2 = draw.textlength(sub, font=sub_font)
    draw.text(((w-tw2)/2, h/2 + font_size*0.3), sub, fill=(150,100,115), font=sub_font)
    dims = f"{w} x {h}"
    tw3 = draw.textlength(dims, font=sub_font)
    draw.text(((w-tw3)/2, h/2 + font_size*1.3), dims, fill=(170,130,145), font=sub_font)
    img.save(os.path.join(OUT, name), quality=88)
    print("saved", name)

# Core Values (company.html) - 4 image cards
make_placeholder("value-product.jpg", 640, 520, "PRODUCT FIRST", "제품 이미지", c1=(255,232,225), c2=(255,247,242))
make_placeholder("value-global.jpg", 640, 520, "GLOBAL MINDED", "글로벌 이미지", c1=(225,238,255), c2=(245,250,255))
make_placeholder("value-startup.jpg", 640, 520, "START-UP CULTURE", "팀 이미지", c1=(232,255,235), c2=(247,255,248))
make_placeholder("value-growth.jpg", 640, 520, "GROWTH OBSESSED", "성장 이미지", c1=(255,240,225), c2=(255,250,242))

# Timeline banner (우리가 걸어온 길)
make_placeholder("timeline-products.jpg", 700, 560, "PRODUCT LINE-UP", "바이오던스 제품 이미지", c1=(250,225,205), c2=(255,242,232))

# howwework.html gallery (3 images)
make_placeholder("howwework-gallery-1.jpg", 700, 560, "WORK SCENE 1", "협업 사진 1", c1=(235,235,245), c2=(248,248,252))
make_placeholder("howwework-gallery-2.jpg", 700, 560, "WORK SCENE 2", "협업 사진 2", c1=(235,235,245), c2=(248,248,252))
make_placeholder("howwework-gallery-3.jpg", 700, 560, "WORK SCENE 3", "협업 사진 3", c1=(235,235,245), c2=(248,248,252))

# growth-support.html gallery (5 images)
for i in range(1,6):
    make_placeholder(f"growth-gallery-{i}.jpg", 700, 560, "OFFICE PERK", f"복지 사진 {i}", c1=(255,238,225), c2=(255,249,242))

# careers.html
make_placeholder("careers-speaker.jpg", 1400, 900, "TOWNHALL SPEAKER", "채용 소개 이미지", c1=(225,225,225), c2=(245,245,245))
make_placeholder("coffeechat.jpg", 1600, 900, "COFFEE CHAT", "커피챗 사진", c1=(200,200,205), c2=(225,225,230))

# newsroom.html extra thumbnails (7-12)
for i in range(7,13):
    make_placeholder(f"news-thumb-{i}.jpg", 640, 420, "NEWS THUMBNAIL", f"뉴스 이미지 {i}", c1=(235,235,255), c2=(248,248,255))

print("ALL DONE 2")
