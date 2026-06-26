#!/usr/bin/env python3
"""서울 출장마사지 사이트 OG/썸네일 이미지 생성 (1200x630, 600x600)."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SANS_B = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
SANS_R = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"

# 팔레트 (사이트 토큰과 일치)
BG = (5, 7, 16)
BG2 = (12, 17, 32)
GOLD = (216, 181, 110)
GOLD_SOFT = (244, 231, 194)
CHAMPAGNE = (231, 210, 160)
ORANGE = (255, 122, 61)
TEXT = (243, 245, 251)
DIM = (154, 164, 186)


def font(path, size):
    return ImageFont.truetype(path, size)


def vgrad(w, h, top, bottom):
    base = Image.new("RGB", (w, h), top)
    top_r, top_g, top_b = top
    bot_r, bot_g, bot_b = bottom
    px = base.load()
    for y in range(h):
        t = y / max(1, h - 1)
        r = int(top_r + (bot_r - top_r) * t)
        g = int(top_g + (bot_g - top_g) * t)
        b = int(top_b + (bot_b - top_b) * t)
        for x in range(w):
            px[x, y] = (r, g, b)
    return base


def radial_glow(w, h, cx, cy, radius, color, max_alpha):
    glow = Image.new("L", (w, h), 0)
    gd = ImageDraw.Draw(glow)
    steps = 60
    for i in range(steps, 0, -1):
        rr = int(radius * i / steps)
        a = int(max_alpha * (1 - i / steps))
        gd.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=a)
    glow = glow.filter(ImageFilter.GaussianBlur(40))
    layer = Image.new("RGB", (w, h), color)
    return layer, glow


def rounded(draw, box, r, **kw):
    draw.rounded_rectangle(box, radius=r, **kw)


def draw_logo(img, cx, cy, r):
    """파비콘과 동일한 둥근 사각 + 오렌지 원 + 흰색 B 마크."""
    d = ImageDraw.Draw(img)
    # 둥근 사각 배경
    rounded(d, [cx - r, cy - r, cx + r, cy + r], int(r * 0.44), fill=(10, 17, 32))
    # 오렌지 그라디언트 원 (근사: 단색 + 글로우)
    cr = int(r * 0.68)
    circle = Image.new("RGBA", (cr * 2, cr * 2), (0, 0, 0, 0))
    cd = ImageDraw.Draw(circle)
    for i in range(cr, 0, -1):
        t = 1 - i / cr
        rr = int(255 + (232 - 255) * t)
        gg = int(184 + (90 - 184) * t)
        bb = int(77 + (43 - 77) * t)
        cd.ellipse([cr - i, cr - i, cr + i, cr + i], fill=(rr, gg, bb, 255))
    img.paste(circle, (cx - cr, cy - cr), circle)
    # B 글자
    bf = font(SANS_B, int(r * 1.0))
    d.text((cx, cy - int(r * 0.04)), "B", font=bf, fill=(255, 255, 255), anchor="mm")


def text_w(draw, s, f):
    b = draw.textbbox((0, 0), s, font=f)
    return b[2] - b[0]


def make_og():
    W, H = 1200, 630
    img = vgrad(W, H, BG, BG2).convert("RGB")
    # 골드 글로우 (상단 중앙)
    layer, mask = radial_glow(W, H, W // 2, -40, 620, (216, 181, 110), 70)
    img.paste(layer, (0, 0), mask)
    # 오렌지 글로우 (우하단)
    layer2, mask2 = radial_glow(W, H, W - 80, H + 60, 460, (255, 122, 61), 55)
    img.paste(layer2, (0, 0), mask2)

    d = ImageDraw.Draw(img)
    # 외곽 보더
    rounded(d, [16, 16, W - 16, H - 16], 28, outline=(216, 181, 110), width=2)
    # 미세 내부 보더
    rounded(d, [22, 22, W - 22, H - 22], 24, outline=(60, 52, 34), width=1)

    # 로고 + 브랜드명
    draw_logo(img, 92, 92, 40)
    d = ImageDraw.Draw(img)
    d.text((150, 92), "간다 GO", font=font(SANS_B, 40), fill=GOLD_SOFT, anchor="lm")

    # 상단 우측 배지
    badge = "서울 25개 구 전역 방문"
    bf = font(SANS_R, 26)
    bw = text_w(d, badge, bf)
    bx2 = W - 70
    rounded(d, [bx2 - bw - 44, 70, bx2, 118], 24,
            fill=(20, 26, 44), outline=(216, 181, 110), width=1)
    d.text(((bx2 - bw - 44 + bx2) // 2, 94), badge, font=bf, fill=CHAMPAGNE, anchor="mm")

    # 메인 타이틀
    d.text((72, 232), "서울 출장마사지 · 홈타이", font=font(SANS_B, 78), fill=TEXT, anchor="lm")
    # 골드 강조 라인
    d.text((72, 330), "생활권별 방문 예약 안내", font=font(SANS_B, 62), fill=GOLD, anchor="lm")

    # 구분선
    d.line([72, 400, W - 72, 400], fill=(60, 52, 34), width=1)

    # 가격 요약 (3코스)
    courses = [("60분", "90,000원"), ("90분", "150,000원"), ("120분", "180,000원")]
    cw = (W - 144 - 40) // 3
    cx = 72
    for i, (mins, price) in enumerate(courses):
        x1 = 72 + i * (cw + 20)
        feat = (i == 1)
        if feat:
            rounded(d, [x1, 430, x1 + cw, 540], 16,
                    fill=(30, 36, 56), outline=GOLD, width=2)
        else:
            rounded(d, [x1, 430, x1 + cw, 540], 16,
                    fill=(18, 23, 40), outline=(50, 56, 76), width=1)
        mid = x1 + cw // 2
        d.text((mid, 466), mins + " 코스", font=font(SANS_R, 26), fill=DIM, anchor="mm")
        d.text((mid, 506), price, font=font(SANS_B, 40),
               fill=(GOLD_SOFT if feat else TEXT), anchor="mm")

    # 하단 전화
    d.text((W // 2, 588), "예약문의  0508-202-4719  ·  연중무휴 24시간",
           font=font(SANS_R, 28), fill=DIM, anchor="mm")

    img.save("assets/og-image.png", "PNG")
    print("wrote assets/og-image.png", img.size)

    # 네이버 정사각 썸네일 (600x600)
    sq = make_square()
    sq.save("assets/thumb-square.png", "PNG")
    print("wrote assets/thumb-square.png", sq.size)


def make_square():
    W = H = 600
    img = vgrad(W, H, BG, BG2).convert("RGB")
    layer, mask = radial_glow(W, H, W // 2, 40, 460, (216, 181, 110), 80)
    img.paste(layer, (0, 0), mask)
    layer2, mask2 = radial_glow(W, H, W // 2, H + 30, 380, (255, 122, 61), 55)
    img.paste(layer2, (0, 0), mask2)
    d = ImageDraw.Draw(img)
    rounded(d, [14, 14, W - 14, H - 14], 26, outline=GOLD, width=2)

    draw_logo(img, W // 2, 150, 56)
    d = ImageDraw.Draw(img)
    d.text((W // 2, 250), "간다 GO", font=font(SANS_B, 46), fill=GOLD_SOFT, anchor="mm")
    d.text((W // 2, 322), "서울 출장마사지", font=font(SANS_B, 52), fill=TEXT, anchor="mm")
    d.text((W // 2, 384), "홈타이 방문 예약", font=font(SANS_B, 44), fill=GOLD, anchor="mm")
    d.line([110, 440, W - 110, 440], fill=(60, 52, 34), width=1)
    d.text((W // 2, 478), "서울 25개 구 전역", font=font(SANS_R, 30), fill=CHAMPAGNE, anchor="mm")
    d.text((W // 2, 524), "0508-202-4719", font=font(SANS_B, 36), fill=TEXT, anchor="mm")
    return img


if __name__ == "__main__":
    make_og()
