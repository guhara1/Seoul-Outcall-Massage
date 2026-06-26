# 서울 5대 권역 허브 페이지
from .seoul_data import ZONES, DISTRICTS
from .site import BRAND, PHONE

# 권역별 고유 안내 (복제 금지 — 권역 성격 반영)
ZONE_GUIDES = {
    "gangnam-area": "강남권은 서울에서 오피스텔·호텔·고급 주거가 가장 촘촘하게 섞인 권역입니다. 강남구 테헤란로의 업무지구, 서초구 반포의 한강변 대단지, 송파구 잠실의 복합 상권, 강동구 천호·둔촌의 주거권이 서로 다른 동선을 가집니다. 같은 권역이라도 평일 낮 업무지구 수요와 저녁·주말 주거지 수요가 갈리므로, 예약 시 방문 장소 유형과 시간대를 함께 알려주시면 일정 조율이 정확합니다. 강남역·잠실역만 반복하기보다 역삼·삼성·문정·천호까지 생활권을 넓게 확인하는 것이 좋습니다.",
    "southwest-area": "서남권은 업무지구와 주거지, 숙소 수요가 가장 다양하게 섞인 권역입니다. 여의도 금융가, 구로·금천 디지털단지, 강서 마곡의 신업무권은 빌딩·오피스텔 출입 절차가 중요하고, 목동·신림·노량진 주거·생활권은 정확한 주소와 공동현관·주차 확인이 중요합니다. 디지털단지권은 지식산업센터와 오피스텔이 밀집해 건물명과 동·호수를 함께 확인하면 방문이 정확합니다.",
    "northeast-area": "동북권은 주거 밀집 지역과 대학가, 환승 역세권이 폭넓게 분포한 권역입니다. 성수·건대는 상권형, 청량리·왕십리는 환승 중심형, 노원·상봉·창동은 대단지 주거형으로 성격이 또렷이 갈립니다. 대학가 원룸권은 건물·호수 확인이, 대단지 주거권은 단지번호와 동·호수 확인이 방문을 정확하게 만듭니다. 시간대별 수요 편차가 크므로 예약 시간대를 미리 확인하세요.",
    "northwest-area": "서북권은 상권·숙소 생활권과 주거 생활권이 뚜렷이 나뉘는 권역입니다. 홍대·신촌·공덕은 게스트하우스·원룸이 밀집한 상권·숙소권으로 숙소명과 객실·체크인 확인이 중요하고, 은평 연신내·뉴타운은 주거권으로 단지·동호수와 공동현관 확인이 중요합니다. 마포구와 서대문구가 겹치는 연남·연희 생활권은 인접 구 안내도 함께 확인하면 좋습니다. 홍대·합정 일대는 야간 수요가 많아 가능 시간을 먼저 확인하는 편이 좋고, 상암 DMC 미디어권과 은평뉴타운은 오피스·대단지 특성에 따라 출입 절차가 달라지므로 방문지 유형을 분명히 알려주시면 일정 조율이 빠릅니다.",
    "downtown-area": "도심권은 호텔·숙소·업무지구·관광지가 한데 모인 서울의 중심 권역입니다. 명동·서울역·이태원은 호텔·게스트하우스 이용 비중이 높아 숙소명과 객실, 출입 절차 확인이 특히 중요하고, 광화문·을지로·종로는 업무 빌딩 방문자 등록과 야간 출입 가능 시간을 확인하는 것이 좋습니다. 용산역·한남 일대는 외국인 숙소 인접권이 넓어 방문지 유형을 먼저 확인하면 방문이 원활합니다. 관광·업무 인접권 특성상 평일 낮과 야간의 수요가 모두 있어, 예약 시 희망 시간대와 방문 장소를 함께 알려주시면 동선과 일정을 정확히 잡을 수 있습니다. 도심권은 도로가 복잡하고 일방통행 구간이 많아, 정확한 건물명과 출입구 위치를 미리 확인해 두면 방문이 한결 수월합니다.",
}


def _zone_body(z):
    cards = "".join(
        f'<a href="/{slug}/" class="card"><h3>{DISTRICTS[slug]["name"]}</h3>'
        f'<p>{DISTRICTS[slug]["life"][0]} · {DISTRICTS[slug]["stations"][0]} 생활권</p>'
        f'<span class="card-arrow">→</span></a>'
        for slug in z["districts"]
    )
    life_items = "".join(f'<li><a href="/life/">{l}</a></li>' for l in z["life"])
    stations_txt = ", ".join(z["stations"])
    gu_names = ", ".join(DISTRICTS[s]["name"] for s in z["districts"])

    return f"""
<section id="zone-intro">
<h2>{z['name']} 출장마사지·홈타이 안내</h2>
{z['intro']}
</section>

<section id="zone-districts">
<h2>{z['name']} 포함 행정구</h2>
<p>{z['name']}에는 {gu_names}이(가) 속합니다. 각 구별 대표 행정동·역세권·생활권을 확인하세요.</p>
<div class="card-grid">{cards}</div>
</section>

<section id="zone-stations">
<h2>{z['name']} 대표 지하철역</h2>
<p>{z['name']}에서 방문 동선의 기준이 되는 대표 역은 {stations_txt} 입니다.</p>
</section>

<section id="zone-life">
<h2>{z['name']} 대표 생활권</h2>
<p>{z['name']}은(는) 아래 생활권으로 폭넓게 안내합니다.</p>
<ul class="link-cloud">{life_items}</ul>
</section>

<section id="zone-focus">
<h2>{z['name']} 이용 안내</h2>
{z['focus']}
<p>{ZONE_GUIDES.get(z['slug'], '')}</p>
<p>방문 전 자세한 사항은 <a href="/check/">이용 전 확인사항</a>과 <a href="/reservation/">예약 안내</a>를 참고하세요. 전체 행정구는 <a href="/district/">서울 25개 구 안내</a>에서 확인할 수 있습니다.</p>
</section>

<section id="source">
<h2>{z['name']} 안내 정보 및 출처</h2>
<p><strong>작성·운영</strong>: {BRAND} 고객센터 · <a href="tel:{PHONE}">{PHONE}</a> (연중무휴 24시간 상담). 본 페이지는 {z['name']} 방문 예약 전 확인을 돕기 위한 권역 안내입니다.</p>
<p><strong>지역 정보 참고</strong>: <a href="https://ko.wikipedia.org/wiki/서울특별시" target="_blank" rel="noopener">위키백과 서울특별시</a> · <a href="/about/">운영 정보</a> · <a href="/district/">서울 25개 구 안내</a></p>
</section>
"""


def _make_zone_page(z):
    return {
        "path": f"zone/{z['slug']}/",
        "title": f"{z['name']} 출장마사지·홈타이｜{'·'.join(z['life'][:3])} 생활권 안내",
        "desc": f"{z['name']} 출장마사지·홈타이 예약 전 포함 구와 대표 생활권을 확인하세요.",
        "h1": f"{z['name']} 출장마사지 안내",
        "breadcrumb": [("서울", "/"), (z["name"], "")],
        "body": _zone_body(z),
    }


PAGES = [_make_zone_page(z) for z in ZONES]
