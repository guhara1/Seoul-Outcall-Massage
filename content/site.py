# 서울 출장마사지 사이트 공통 설정

BASE_URL = "https://seoul-massage.pages.dev"

BRAND = "간다 GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 서비스 지역(스키마·푸터 공통)
AREA_REGION = "서울특별시"

# 상단 메뉴 — 키워드 반복 없음, 지역명·권역명만 표시
NAV = [
    ("서울", "/seoul/", []),
    ("권역 안내", "/seoul/district/", [
        ("강남권", "/seoul/zone/gangnam-area/"),
        ("서남권", "/seoul/zone/southwest-area/"),
        ("동북권", "/seoul/zone/northeast-area/"),
        ("서북권", "/seoul/zone/northwest-area/"),
        ("도심권", "/seoul/zone/downtown-area/"),
    ]),
    ("행정구 안내", "/seoul/district/", [
        ("강남구", "/seoul/gangnam-gu/"),
        ("서초구", "/seoul/seocho-gu/"),
        ("송파구", "/seoul/songpa-gu/"),
        ("마포구", "/seoul/mapo-gu/"),
        ("영등포구", "/seoul/yeongdeungpo-gu/"),
        ("성동구", "/seoul/seongdong-gu/"),
        ("용산구", "/seoul/yongsan-gu/"),
        ("전체 25개 구", "/seoul/district/"),
    ]),
    ("지하철역 안내", "/seoul/station/", []),
    ("생활권 안내", "/seoul/life/", []),
    ("예약 안내", "/seoul/reservation/", []),
    ("이용 전 확인사항", "/seoul/check/", []),
    ("고객센터", "/seoul/support/", [
        ("개인정보처리방침", "/seoul/support/privacy/"),
    ]),
]
