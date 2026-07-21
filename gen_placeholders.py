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
    # vertical gradient
    for y in range(h):
        t = y / max(h-1,1)
        r = int(c1[0] + (c2[0]-c1[0])*t)
        g = int(c1[1] + (c2[1]-c1[1])*t)
        b = int(c1[2] + (c2[2]-c1[2])*t)
        draw.line([(0,y),(w,y)], fill=(r,g,b))
    # subtle border
    draw.rectangle([0,0,w-1,h-1], outline=(220,180,190), width=2)
    # center dashed box
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

# Hero images
make_placeholder("hero-main.jpg", 1920, 1080, "MAIN HERO IMAGE", "여기에 대표 이미지를 넣어주세요")
make_placeholder("hero-company.jpg", 1920, 700, "COMPANY HERO", "회사 소개 상단 이미지")
make_placeholder("hero-howwework.jpg", 1920, 700, "HOW WE WORK HERO", "일하는 방법 상단 이미지")
make_placeholder("hero-growth.jpg", 1920, 700, "GROWTH SUPPORT HERO", "성장 지원 상단 이미지")
make_placeholder("hero-careers.jpg", 1920, 700, "CAREERS HERO", "채용 공고 상단 이미지")

# People
make_placeholder("founder-ceo.jpg", 500, 500, "CEO PHOTO", "대표 프로필 사진", c1=(230,230,255), c2=(245,245,255))
make_placeholder("founder-cpo.jpg", 500, 500, "CPO PHOTO", "대표 프로필 사진", c1=(230,230,255), c2=(245,245,255))
make_placeholder("testimonial-1.jpg", 400, 400, "TEAM PHOTO", "인터뷰 사진 1", c1=(225,245,235), c2=(245,255,250))
make_placeholder("testimonial-2.jpg", 400, 400, "TEAM PHOTO", "인터뷰 사진 2", c1=(225,245,235), c2=(245,255,250))
make_placeholder("testimonial-3.jpg", 400, 400, "TEAM PHOTO", "인터뷰 사진 3", c1=(225,245,235), c2=(245,255,250))

# Story / brand
make_placeholder("biodance-story.jpg", 1200, 800, "BIODANCE STORY", "브랜드 스토리 이미지", c1=(255,225,225), c2=(255,245,240))
make_placeholder("welcome-kit.jpg", 800, 800, "WELCOME KIT", "웰컴 키트 이미지", c1=(255,235,210), c2=(255,248,235))

# Newsroom thumbnails
for i in range(1,7):
    make_placeholder(f"news-thumb-{i}.jpg", 640, 420, "NEWS THUMBNAIL", f"뉴스 이미지 {i}", c1=(235,235,255), c2=(248,248,255))

print("ALL DONE")
