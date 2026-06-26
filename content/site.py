# 서울 출장마사지 사이트 공통 설정

BASE_URL = "https://seoul-outcall-massage.pages.dev"

BRAND = "간다 GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 서비스 지역(스키마·푸터 공통)
AREA_REGION = "서울특별시"

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
