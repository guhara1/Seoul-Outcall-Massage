import json
from .site import BRAND, BASE_URL, PHONE, AREA_REGION
from .seoul_data import ZONES, DISTRICTS, DISTRICT_ORDER

_BASE = BASE_URL.rstrip("/")

# 메타 설명 (80자 이내)
DESC = "서울 출장마사지·홈타이 예약 전 강남, 잠실, 홍대, 여의도, 성수, 용산 생활권을 확인하세요."

# 자주 묻는 질문 (FAQ 스키마)
_FAQ = [
    ("서울 출장마사지는 어떤 서비스인가요?",
     "고객의 자택·호텔·오피스텔 등으로 전문가가 방문해 관리하는 방문형 마사지 서비스입니다. 서울 25개 구 전역으로 방문 가능합니다."),
    ("서울은 어떤 기준으로 지역을 찾나요?",
     "서울은 행정구가 명확하지만 실제 이용은 강남·홍대·여의도·성수처럼 생활권 중심으로 움직입니다. 행정구, 행정동, 지하철역, 생활권을 함께 확인하면 정확합니다."),
    ("강남역과 역삼동은 같은 안내인가요?",
     "아닙니다. 강남역은 역세권 기준, 역삼동은 행정동·업무지구 기준으로 방문 동선과 이용 목적이 다릅니다. 각각 따로 확인하는 것이 좋습니다."),
    ("예약 전 꼭 확인해야 할 사항은?",
     "방문 가능 주소와 건물 유형, 예약 가능 시간, 건물 출입 방식, 결제 방식, 개인정보 처리 기준을 먼저 확인하고 예약하는 것이 좋습니다."),
    ("호텔·숙소에서도 이용할 수 있나요?",
     "명동·서울역·이태원·용산 등 호텔·숙소 인접권에서 이용 가능 여부와 예약 시간을 먼저 확인하면 방문이 원활합니다."),
]

_faq_schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "@id": f"#faq-{i+1}", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a}}
        for i, (q, a) in enumerate(_FAQ)
    ],
}
_faq_schema_str = json.dumps(_faq_schema, ensure_ascii=False, indent=2)

_org_schema = {
    "@context": "https://schema.org",
    "@type": "HealthAndBeautyBusiness",
    "name": BRAND,
    "telephone": PHONE,
    "url": _BASE + "/",
    "image": _BASE + "/assets/og-image.png",
    "description": "서울 출장마사지·홈타이 생활권별 안내 사이트",
    "priceRange": "₩₩",
    "address": {
        "@type": "PostalAddress",
        "addressRegion": AREA_REGION,
        "addressCountry": "KR",
    },
    "areaServed": {"@type": "AdministrativeArea", "name": AREA_REGION},
    "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "opens": "00:00", "closes": "23:59",
    },
}
_org_schema_str = json.dumps(_org_schema, ensure_ascii=False, indent=2)

_breadcrumb_schema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "홈", "item": _BASE + "/"},
    ],
}
_breadcrumb_schema_str = json.dumps(_breadcrumb_schema, ensure_ascii=False, indent=2)

_EXTRA_HEAD = f"""<script type="application/ld+json">
{_org_schema_str}
</script>
<script type="application/ld+json">
{_breadcrumb_schema_str}
</script>
<script type="application/ld+json">
{_faq_schema_str}
</script>"""

_HERO = """<div class="hero">
  <div class="hero-content">
    <div class="hero-badge">서울 25개 구 생활권별 방문 안내</div>
    <h1 class="hero-title">서울 출장마사지<br><span class="hero-accent">홈타이</span><br>생활권별 예약 안내</h1>
    <p class="hero-lead">강남, 잠실, 홍대, 여의도, 성수, 용산, 목동, 연신내 등 서울 주요 생활권별 방문 가능 지역과 예약 전 확인사항을 안내합니다.</p>
    <div class="hero-cta">
      <a href="#zones" class="btn btn-primary">권역별 보기</a>
      <a href="/district/" class="btn btn-secondary">행정구 찾기</a>
      <a href="/station/" class="btn btn-secondary">지하철역 찾기</a>
      <a href="/life/" class="btn btn-secondary">생활권 찾기</a>
      <a href="/reservation/" class="btn btn-secondary">예약 안내 보기</a>
    </div>
  </div>
  <div class="hero-stats">
    <div class="stat"><div class="stat-number">5</div><div class="stat-label">대 권역</div></div>
    <div class="stat"><div class="stat-number">25</div><div class="stat-label">개 행정구</div></div>
    <div class="stat"><div class="stat-number">서울</div><div class="stat-label">전역 안내</div></div>
    <div class="stat"><div class="stat-number">24H</div><div class="stat-label">상담 가능</div></div>
  </div>
</div>"""

# 5대 권역 카드
_zone_cards = "".join(
    f'<a href="/zone/{z["slug"]}/" class="card"><h3>{z["name"]}</h3>'
    f'<p>{", ".join(DISTRICTS[s]["name"] for s in z["districts"][:4])} 등</p>'
    f'<span class="card-arrow">→</span></a>'
    for z in ZONES
)

# 25개 구 카드
_district_cards = "".join(
    f'<a href="/{slug}/" class="card"><h3>{DISTRICTS[slug]["name"]}</h3>'
    f'<p>{DISTRICTS[slug]["life"][0]} 생활권</p></a>'
    for slug in DISTRICT_ORDER
)

PAGE = {
    "path": "",
    "title": "서울 출장마사지｜강남·잠실·홍대·여의도·성수 홈타이 안내",
    "desc": DESC,
    "h1": "서울 출장마사지 · 생활권별 홈타이 예약 안내",
    "hero": _HERO,
    "breadcrumb": [],
    "extra_head": _EXTRA_HEAD,
    "body": f"""
<section id="criteria">
  <h2>서울 출장마사지는 행정구보다 생활권 기준이 중요합니다</h2>
  <p>서울특별시는 25개 구로 나뉘는 행정구역이 명확하지만, 실제 검색과 이용은 강남·홍대·여의도·성수·목동·연신내처럼 생활권 단어를 중심으로 움직입니다. 같은 강남구 안에서도 강남역, 역삼, 삼성, 청담은 이용 목적과 이동 기준이 서로 다르고, 송파구도 잠실, 문정, 가락, 위례는 같은 구 안에서 예약 기준이 다릅니다.</p>
  <p>그래서 이 사이트는 행정구, 행정동, 지하철역, 생활권을 따로 분리해 안내합니다. 먼저 서울을 5대 권역으로 나누고, 그 안에서 25개 구와 대표 행정동, 역세권, 생활권을 순서대로 확인할 수 있도록 구성했습니다. 본인 위치의 권역과 구, 가까운 역, 생활권을 차례로 확인하면 방문 주소와 예약 시간을 정확히 잡을 수 있습니다.</p>
</section>

<section id="zones">
  <h2>서울 권역별 방문 가능 지역 안내</h2>
  <p>서울을 강남권·서남권·동북권·서북권·도심권 5대 권역으로 나누어 안내합니다. 각 권역의 포함 구와 대표 생활권, 대표 역을 확인하세요.</p>
  <div class="card-grid">{_zone_cards}</div>
</section>

<section id="districts">
  <h2>서울 25개 구별 안내</h2>
  <p>행정구별 대표 행정동, 지하철역, 생활권을 확인하세요. 전체 목록은 <a href="/district/">서울 25개 구 안내</a>에서 볼 수 있습니다.</p>
  <div class="card-grid">{_district_cards}</div>
</section>

<section id="stations">
  <h2>서울 주요 지하철역별 안내</h2>
  <p>강남역, 잠실역, 홍대입구역, 여의도역, 성수역, 용산역 등 주요 역을 기준으로 인접 생활권과 예약 기준을 안내합니다. 역명 기준 안내는 <a href="/station/">지하철역 안내</a>에서 단계적으로 제공됩니다.</p>
  <ul>
    <li><strong>강남역</strong> — 역삼동, 서초동, 신논현 인접 생활권. 오피스텔·호텔·자택 이용 여부를 먼저 확인하세요.</li>
    <li><strong>잠실역</strong> — 잠실동, 석촌동, 방이동 인접 생활권. 방문 주소와 건물 출입 가능 여부를 확인하세요.</li>
    <li><strong>홍대입구역</strong> — 서교동, 연남동, 합정동 인접 생활권. 숙소 이용 가능 여부와 예약 시간을 먼저 확인하세요.</li>
  </ul>
</section>

<section id="purpose">
  <h2>서울 방문형 관리 서비스 이용 전 확인사항</h2>
  <p>방문 장소 유형에 따라 출입 절차와 예약 기준이 다릅니다. 이용 목적별로 확인할 사항을 정리했습니다.</p>
  <ul>
    <li><strong>자택 이용</strong> — 공동현관·주차 가능 여부와 정확한 주소 확인</li>
    <li><strong>호텔·숙소 이용</strong> — 숙소 이용 가능 여부와 예약 시간, 출입 절차 확인</li>
    <li><strong>오피스텔 이용</strong> — 로비 출입, 엘리베이터 카드 등 건물 출입 방식 확인</li>
    <li><strong>업무지구 예약</strong> — 빌딩 출입 절차와 방문 가능 시간대 확인</li>
    <li><strong>야간 예약</strong> — 야간 방문 가능 시간과 추가 안내 확인</li>
    <li><strong>외국인 숙소 인접권</strong> — 이태원·한남 등 숙소 인접권의 예약·출입 기준 확인</li>
  </ul>
  <p>자세한 사항은 <a href="/check/">이용 전 확인사항</a>과 <a href="/reservation/">예약 안내</a>를 참고하세요.</p>
</section>

<section id="faq">
  <h2>서울 출장마사지 자주 묻는 질문</h2>
  <dl class="faq-list">
    <dt id="faq-1">서울 출장마사지는 어떤 서비스인가요?</dt>
    <dd>고객의 자택·호텔·오피스텔 등으로 전문가가 방문해 관리하는 방문형 마사지 서비스입니다. 서울 25개 구 전역으로 방문 가능합니다.</dd>
    <dt id="faq-2">서울은 어떤 기준으로 지역을 찾나요?</dt>
    <dd>서울은 행정구가 명확하지만 실제 이용은 강남·홍대·여의도·성수처럼 생활권 중심으로 움직입니다. 행정구, 행정동, 지하철역, 생활권을 함께 확인하면 정확합니다.</dd>
    <dt id="faq-3">강남역과 역삼동은 같은 안내인가요?</dt>
    <dd>아닙니다. 강남역은 역세권 기준, 역삼동은 행정동·업무지구 기준으로 방문 동선과 이용 목적이 다릅니다. 각각 따로 확인하는 것이 좋습니다.</dd>
    <dt id="faq-4">예약 전 꼭 확인해야 할 사항은?</dt>
    <dd>방문 가능 주소와 건물 유형, 예약 가능 시간, 건물 출입 방식, 결제 방식, 개인정보 처리 기준을 먼저 확인하고 예약하는 것이 좋습니다.</dd>
    <dt id="faq-5">호텔·숙소에서도 이용할 수 있나요?</dt>
    <dd>명동·서울역·이태원·용산 등 호텔·숙소 인접권에서 이용 가능 여부와 예약 시간을 먼저 확인하면 방문이 원활합니다.</dd>
  </dl>
</section>

<section id="references">
  <h2>서울 지역 공식 정보 및 참고 자료</h2>
  <p>방문 관리 서비스를 이용하기 전, 지역 행정 정보와 소비자 보호·보건 관련 공식 기관 자료를 함께 참고하시면 도움이 됩니다.</p>
  <ul>
    <li><a href="https://www.seoul.go.kr/" target="_blank" rel="noopener">서울특별시청 공식 홈페이지</a> — 서울 행정구역·생활 정보·민원 안내</li>
    <li><a href="https://www.seoulmetro.co.kr/" target="_blank" rel="noopener">서울교통공사</a> — 서울 지하철 노선·역 정보</li>
    <li><a href="https://www.mohw.go.kr/" target="_blank" rel="noopener">보건복지부</a> — 보건·위생 및 건강 관리 관련 공식 정보</li>
    <li><a href="https://www.kca.go.kr/" target="_blank" rel="noopener">한국소비자원</a> — 소비자 권리 및 예약·결제 분쟁 관련 안내</li>
  </ul>
  <p class="ref-note">위 외부 링크는 공공·공식 기관 자료로, 이용자의 정확한 정보 확인을 돕기 위해 제공됩니다.</p>
</section>
"""
}
