# 서울 출장마사지 사이트 공통 설정

BASE_URL = "https://seoul-outcall-massage.pages.dev"

BRAND = "간다 GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 서비스 지역(스키마·푸터 공통)
AREA_REGION = "서울특별시"

# 검색엔진 사이트 소유확인
NAVER_SITE_VERIFICATION = "b8738498666eaf202faaeff7f57fe68b9df4f470"
GOOGLE_SITE_VERIFICATION = ""  # 구글 서치콘솔 메타 확인 코드(있으면 입력)

# IndexNow 키 (빙·네이버 즉시 색인 통보용) — /{KEY}.txt 파일로 노출
INDEXNOW_KEY = "e0b8a03814f46001b136d56ee655b57c"

# 코스 시간별 기본 요금 (전 페이지 공통)
PRICE_COURSES = [
    ("60분 코스", "90,000", "60분", "핵심 부위 위주 가벼운 이완", False),
    ("90분 코스", "150,000", "90분", "전신 균형 표준 구성·아로마 포함", True),
    ("120분 코스", "180,000", "120분", "구석구석 집중하는 프리미엄 구성", False),
]


def price_table(heading_level="h2"):
    """코스 시간별 기본 요금표 HTML을 반환합니다. 모든 지역 페이지 공통."""
    cards = []
    for name, price, mins, note, featured in PRICE_COURSES:
        badge = '<span class="price-badge">추천</span>' if featured else ""
        cls = "price-card price-card-featured" if featured else "price-card"
        cards.append(
            f'<div class="{cls}">{badge}'
            f'<div class="price-name">{name}</div>'
            f'<div class="price-amount">{price}<span class="price-won">원</span></div>'
            f'<div class="price-mins">{mins}</div>'
            f'<div class="price-note">{note}</div>'
            f'<a href="tel:{PHONE}" class="price-cta">예약 문의</a>'
            f'</div>'
        )
    cards_html = "".join(cards)
    return f"""<section class="price-section" id="price">
  <{heading_level} class="price-title">코스 시간으로 보는 기본 요금</{heading_level}>
  <p class="price-sub">관리 시간(60·90·120분)을 기준으로 정리한 기본 금액입니다. 표시되지 않은 별도 비용은 두지 않는 것을 원칙으로 안내합니다.</p>
  <div class="price-grid">{cards_html}</div>
  <p class="price-foot">방문 지역과 시간대, 이동 거리에 따라 최종 금액은 통화 시 확정됩니다. <a href="/reservation/">요금·예약 기준 자세히 보기 →</a></p>
</section>"""


# 상단 메뉴 — 키워드 반복 없음, 지역명·권역명만 표시
NAV = [
    ("서울", "/", []),
    ("권역 안내", "/district/", [
        ("강남권", "/zone/gangnam-area/"),
        ("서남권", "/zone/southwest-area/"),
        ("동북권", "/zone/northeast-area/"),
        ("서북권", "/zone/northwest-area/"),
        ("도심권", "/zone/downtown-area/"),
    ]),
    ("행정구 안내", "/district/", [
        ("강남구", "/gangnam-gu/"),
        ("서초구", "/seocho-gu/"),
        ("송파구", "/songpa-gu/"),
        ("마포구", "/mapo-gu/"),
        ("영등포구", "/yeongdeungpo-gu/"),
        ("성동구", "/seongdong-gu/"),
        ("용산구", "/yongsan-gu/"),
        ("전체 25개 구", "/district/"),
    ]),
    ("지하철역 안내", "/station/", []),
    ("생활권 안내", "/life/", []),
    ("예약 안내", "/reservation/", []),
    ("이용 전 확인사항", "/check/", []),
    ("고객센터", "/support/", [
        ("개인정보처리방침", "/support/privacy/"),
    ]),
]
