# 서울 생활권 개별 페이지 (24개) + 생활권 인덱스 — 고유 본문, 전부 색인
from .seoul_data import DISTRICTS, ZONES, _zone_of
from .seoul_dongs import DONG_SLUGS
from .site import BRAND, PHONE, price_table

# name, slug, gu_slug(대표), dongs[(gu_slug,name)], stations[(name,slug)], character(고유 2문장)
LIFE = [
    ("강남·역삼", "gangnam-yeoksam", "gangnam-gu",
     [("gangnam-gu", "역삼동"), ("gangnam-gu", "논현동")],
     [("강남역", "gangnam-station"), ("역삼역", "yeoksam-station")],
     "강남·역삼 생활권은 강남역과 테헤란로를 따라 오피스텔과 업무 빌딩, 상권이 밀집한 서울 최대 업무·상권 권역입니다. 평일 낮 업무 수요와 저녁 상권 수요가 함께 움직여 방문 시간대와 건물 유형 확인이 중요합니다."),
    ("삼성·선릉", "samseong-seolleung", "gangnam-gu",
     [("gangnam-gu", "삼성동"), ("gangnam-gu", "대치동")],
     [("삼성역", "samseong-station"), ("선릉역", "seolleung-station")],
     "삼성·선릉 생활권은 코엑스·무역센터의 전시·업무권과 대치 학원가가 이어지는 지역입니다. 전시·행사 일정에 따라 유동 인구가 크게 달라져 방문 시간을 여유 있게 잡는 것이 좋습니다."),
    ("청담·압구정", "cheongdam-apgujeong", "gangnam-gu",
     [("gangnam-gu", "청담동"), ("gangnam-gu", "압구정동")],
     [("압구정로데오역", None), ("청담역", None)],
     "청담·압구정 생활권은 명품거리와 갤러리, 고급 주거 단지가 모인 강남의 대표 고급 생활권입니다. 늦은 오후·저녁 수요가 두드러지고 단지 보안 절차가 엄격한 편입니다."),
    ("잠실·송파", "jamsil-songpa", "songpa-gu",
     [("songpa-gu", "잠실동"), ("songpa-gu", "송파동")],
     [("잠실역", "jamsil-station"), ("석촌역", "seokchon-station")],
     "잠실·송파 생활권은 롯데월드타워와 석촌호수, 잠실역 환승 상권을 낀 복합 생활권입니다. 초고층 주상복합과 대단지가 많아 단지·동·호수와 출입 절차 확인이 중요합니다."),
    ("문정·가락", "munjeong-garak", "songpa-gu",
     [("songpa-gu", "문정동"), ("songpa-gu", "가락동")],
     [("문정역", "munjeong-station")],
     "문정·가락 생활권은 법조타운과 지식산업센터, 가락시장 일대의 업무·물류 생활권입니다. 지식산업센터형 오피스가 많아 건물명과 층·호수, 로비 출입 확인이 중요합니다."),
    ("홍대·합정", "hongdae-hapjeong", "mapo-gu",
     [("mapo-gu", "서교동"), ("mapo-gu", "합정동")],
     [("홍대입구역", "hongik-univ-station"), ("합정역", "hapjeong-station")],
     "홍대·합정 생활권은 클럽·라이브 상권과 게스트하우스, 원룸이 밀집한 서울 서북부 대표 상권·숙소권입니다. 저녁·야간 수요가 많아 가능 시간과 출입 방식을 먼저 확인하는 것이 좋습니다."),
    ("연남·망원", "yeonnam-mangwon", "mapo-gu",
     [("mapo-gu", "연남동"), ("mapo-gu", "망원동")],
     [("홍대입구역", "hongik-univ-station"), ("망원역", None)],
     "연남·망원 생활권은 경의선숲길을 따라 카페거리와 주택가가 어우러진 지역입니다. 주택·빌라가 많아 도로명 주소와 골목 진입 동선 확인이 중요합니다."),
    ("공덕·마포", "gongdeok-mapo", "mapo-gu",
     [("mapo-gu", "공덕동"), ("mapo-gu", "도화동")],
     [("공덕역", "gongdeok-station")],
     "공덕·마포 생활권은 다중 환승 거점을 중심으로 오피스와 주거가 함께 발달한 업무·주거권입니다. 평일 낮 오피스 수요가 많아 빌딩 출입 절차 확인이 중요합니다."),
    ("여의도·영등포", "yeouido-yeongdeungpo", "yeongdeungpo-gu",
     [("yeongdeungpo-gu", "여의도동"), ("yeongdeungpo-gu", "영등포동")],
     [("여의도역", "yeouido-station"), ("영등포역", "yeongdeungpo-station")],
     "여의도·영등포 생활권은 금융 업무가와 영등포역 상권이 맞닿은 지역입니다. 여의도 오피스 빌딩은 보안 게이트와 야간 출입 제한이 있어 시간대 확인이 필요합니다."),
    ("문래·당산", "mullae-dangsan", "yeongdeungpo-gu",
     [("yeongdeungpo-gu", "문래동"), ("yeongdeungpo-gu", "당산동")],
     [("당산역", "dangsan-station")],
     "문래·당산 생활권은 문래 창작촌과 당산 환승 주거권이 이어지는 지역입니다. 주상복합과 주거 아파트가 많아 공동현관과 주차 확인이 중요합니다."),
    ("신림·서울대입구", "sillim-snu", "gwanak-gu",
     [("gwanak-gu", "신림동"), ("gwanak-gu", "봉천동")],
     [("신림역", "sillim-station"), ("서울대입구역", "seoul-nat-univ-station")],
     "신림·서울대입구 생활권은 원룸·오피스텔이 밀집한 서울 대표 1인 가구 생활권입니다. 건물과 호수 단위 방문이 잦아 정확한 호수와 야간 가능 시간 확인이 중요합니다."),
    ("건대·광진", "konkuk-gwangjin", "gwangjin-gu",
     [("gwangjin-gu", "화양동"), ("gwangjin-gu", "구의동")],
     [("건대입구역", "konkuk-univ-station"), ("구의역", "guui-station")],
     "건대·광진 생활권은 대학가 상권과 구의·강변 환승권이 이어지는 지역입니다. 대학가 원룸은 건물 출입과 호수 확인이 특히 중요합니다."),
    ("성수·왕십리", "seongsu-wangsimni", "seongdong-gu",
     [("seongdong-gu", "성수동"), ("seongdong-gu", "행당동")],
     [("성수역", "seongsu-station"), ("왕십리역", "wangsimni-station")],
     "성수·왕십리 생활권은 성수 카페·창업 상권과 왕십리 다중 환승권이 맞닿은 지역입니다. 리모델링 건물이 많아 건물명과 층·호수 확인이 중요합니다."),
    ("용산·서울역", "yongsan-seoul-station", "yongsan-gu",
     [("yongsan-gu", "한강로동"), ("yongsan-gu", "이촌동")],
     [("용산역", "yongsan-station"), ("서울역", "seoul-station")],
     "용산·서울역 생활권은 주상복합과 업무, 호텔·역세권이 모인 도심 관문 지역입니다. 방문자 등록과 출입 절차가 있는 건물이 많아 사전 확인이 필요합니다."),
    ("한남·이태원", "hannam-itaewon", "yongsan-gu",
     [("yongsan-gu", "한남동"), ("yongsan-gu", "이태원동")],
     [("이태원역", "itaewon-station"), ("한강진역", "hangangjin-station")],
     "한남·이태원 생활권은 외국인 숙소와 상권이 발달한 서울의 대표 글로벌 생활권입니다. 호텔·게스트하우스 이용 시 숙소명·객실과 출입 절차 확인이 중요합니다."),
    ("목동·양천", "mokdong-yangcheon", "yangcheon-gu",
     [("yangcheon-gu", "목동"), ("yangcheon-gu", "신정동")],
     [("목동역", "mok-dong-station"), ("오목교역", "omokgyo-station")],
     "목동·양천 생활권은 대단지 아파트와 학원가가 밀집한 대표 주거권입니다. 단지번호와 동·호수, 공동현관 절차 확인이 방문을 빠르게 합니다."),
    ("연신내·은평", "yeonsinnae-eunpyeong", "eunpyeong-gu",
     [("eunpyeong-gu", "불광동"), ("eunpyeong-gu", "갈현동")],
     [("연신내역", "yeonsinnae-station"), ("불광역", "bulgwang-station")],
     "연신내·은평 생활권은 연신내 환승 상권과 은평뉴타운 대단지가 이어지는 지역입니다. 상권은 야간 수요가, 뉴타운은 대단지 출입 확인이 중요합니다."),
    ("노원·상계", "nowon-sanggye", "nowon-gu",
     [("nowon-gu", "상계동"), ("nowon-gu", "중계동")],
     [("노원역", "nowon-station")],
     "노원·상계 생활권은 노원역 상권과 상계·중계 대단지가 모인 동북부 대표 주거권입니다. 대단지가 많아 단지번호와 가까운 출입구 안내가 중요합니다."),
    ("상봉·중랑", "sangbong-jungnang", "jungnang-gu",
     [("jungnang-gu", "상봉동"), ("jungnang-gu", "망우동")],
     [("상봉역", "sangbong-station")],
     "상봉·중랑 생활권은 상봉 환승·터미널 상권과 면목·망우 주거권이 넓게 자리한 지역입니다. 주거권은 빌라·아파트가 섞여 정확한 주소 확인이 중요합니다."),
    ("종로·광화문", "jongno-gwanghwamun", "jongno-gu",
     [("jongno-gu", "종로1·2·3·4가동"), ("jongno-gu", "사직동")],
     [("종로3가역", "jongno-3-ga-station"), ("광화문역", "gwanghwamun-station")],
     "종로·광화문 생활권은 도심 업무 빌딩과 관광·문화권이 어우러진 서울 중심 지역입니다. 업무권은 빌딩 방문자 등록, 호텔은 출입 절차 확인이 필요합니다."),
    ("명동·을지로", "myeongdong-euljiro", "jung-gu",
     [("jung-gu", "명동"), ("jung-gu", "을지로동")],
     [("명동역", "myeongdong-station"), ("을지로입구역", "euljiro-1-ga-station")],
     "명동·을지로 생활권은 호텔·관광 상권과 인쇄·업무권이 맞닿은 도심 지역입니다. 호텔·게스트하우스 이용 비중이 높아 숙소·출입 확인이 특히 중요합니다."),
    ("마곡·발산", "magok-balsan", "gangseo-gu",
     [("gangseo-gu", "마곡동"), ("gangseo-gu", "발산동")],
     [("마곡역", "magok-station"), ("발산역", "balsan-station")],
     "마곡·발산 생활권은 마곡지구 연구·업무 빌딩과 신축 아파트가 모인 신생활권입니다. 신축 건물이 많아 도로명 주소와 건물 출입 확인이 정확합니다."),
    ("구디·가디", "gd-gd", "guro-gu",
     [("guro-gu", "구로동"), ("geumcheon-gu", "가산동")],
     [("구로디지털단지역", "guro-digital-complex-station"), ("가산디지털단지역", "gasan-digital-complex-station")],
     "구디·가디 생활권은 구로·가산 디지털단지의 IT·업무 생활권입니다. 지식산업센터와 오피스텔이 밀집해 건물명·호수와 로비 출입 절차 확인이 중요합니다."),
    ("노량진·동작", "noryangjin-dongjak", "dongjak-gu",
     [("dongjak-gu", "노량진동"), ("dongjak-gu", "상도동")],
     [("노량진역", "noryangjin-station"), ("사당역", "sadang-station")],
     "노량진·동작 생활권은 학원가와 환승권, 주거권이 어우러진 지역입니다. 학원가 원룸·고시텔은 건물·호수 확인이 특히 중요합니다."),
]

LIFE_SLUGS = {name: slug for name, slug, *_ in LIFE}


def _dong_link(gu_slug, name):
    if name in DONG_SLUGS:
        gu_name = DISTRICTS[gu_slug]["name"]
        return f'<li><a href="/{gu_slug}/{DONG_SLUGS[name]}/">{gu_name} {name}</a></li>'
    return f"<li>{name}</li>"


def _station_link(name, slug):
    if slug:
        return f'<li><a href="/station/{slug}/">{name}</a></li>'
    return f"<li>{name}</li>"


def _life_body(entry):
    name, slug, gu_slug, dongs, stations, character = entry
    gu_name = DISTRICTS[gu_slug]["name"]
    zone_slug, zone_name = _zone_of(gu_slug)
    gus = sorted({g for g, _ in dongs})
    gu_links = " · ".join(
        f'<a href="/{g}/">{DISTRICTS[g]["name"]}</a>' for g in gus
    )
    dong_items = "".join(_dong_link(g, n) for g, n in dongs)
    station_items = "".join(_station_link(n, s) for n, s in stations)
    return f"""
<section id="intro">
<h2>{name} 생활권 출장마사지·홈타이 안내</h2>
<p>{character}</p>
<p>{name} 생활권으로 출장마사지·홈타이를 예약할 때는 행정구·행정동·역세권을 함께 확인하면 방문 주소와 시간을 정확히 잡을 수 있습니다. 같은 생활권 안에서도 건물 유형(자택·오피스텔·호텔)에 따라 출입 방식이 다르니 예약 시 방문지 유형을 알려주세요.</p>
</section>

<section id="dongs">
<h2>{name} 포함 행정동</h2>
<p>{name} 생활권과 이어지는 주요 행정동입니다. 각 동을 클릭하면 가까운 역과 인접 동, 예약 전 확인사항을 확인할 수 있습니다.</p>
<ul>{dong_items}</ul>
</section>

<section id="stations">
<h2>{name} 가까운 지하철역</h2>
<p>{name} 생활권의 방문 동선 기준이 되는 지하철역입니다.</p>
<ul>{station_items}</ul>
</section>

<section id="zone">
<h2>{name} 관련 행정구·권역</h2>
<p>{name} 생활권은 {gu_links} 및 <a href="/zone/{zone_slug}/">{zone_name}</a> 권역과 연결됩니다. 전체 생활권은 <a href="/life/">생활권 안내</a>, 전체 행정구는 <a href="/district/">서울 25개 구 안내</a>에서 확인하세요.</p>
</section>

<section id="visit">
<h2>{name} 방문 예약 안내</h2>
{DISTRICTS[gu_slug]['character']}
<p>{name} 생활권은 건물 유형에 따라 출입 방식이 다릅니다. 오피스텔·업무 빌딩은 로비 방문자 등록과 엘리베이터 카드를, 주거 단지는 공동현관과 주차를, 호텔·숙소는 객실과 출입 절차를 미리 확인하면 방문이 원활합니다. 목적별 상세는 <a href="/purpose/">이용 목적별 안내</a>를 참고하세요.</p>
<p>예약 시 정확한 주소(건물명·동·호수)와 희망 시간, 연락처를 알려주시면 도착 안내가 빠릅니다. 예약 방법은 <a href="/reservation/">예약 안내</a>, 방문 전 점검은 <a href="/check/">이용 전 확인사항</a>에서 확인할 수 있습니다.</p>
</section>

{price_table()}

<section id="source">
<h2>{name} 안내 정보 및 출처</h2>
<p><strong>작성·운영</strong>: {BRAND} 고객센터 · <a href="tel:{PHONE}">{PHONE}</a> (연중무휴 24시간 상담). 본 페이지는 {name} 생활권 방문 예약 전 확인을 돕기 위한 안내입니다.</p>
<p><strong>지역 정보 참고</strong>: <a href="https://ko.wikipedia.org/wiki/{gu_name}" target="_blank" rel="noopener">위키백과 {gu_name}</a> · <a href="/about/">운영 정보</a> · <a href="/check/">이용 전 확인사항</a></p>
</section>
"""


def _make_life_page(entry):
    name, slug = entry[0], entry[1]
    return {
        "path": f"life/{slug}/",
        "title": f"{name} 출장마사지·홈타이｜서울 생활권 방문 안내",
        "desc": f"{name} 생활권 출장마사지·홈타이 예약 전 행정동, 가까운 역을 확인하세요.",
        "h1": f"{name} 생활권 출장마사지",
        "breadcrumb": [("서울", "/"), ("생활권 안내", "/life/"), (name, "")],
        "body": _life_body(entry),
        "noindex": False,
    }


# 생활권 인덱스
_life_cards = "".join(
    f'<a href="/life/{slug}/" class="card"><h3>{name}</h3>'
    f'<p>{DISTRICTS[gu_slug]["name"]} 생활권</p><span class="card-arrow">→</span></a>'
    for name, slug, gu_slug, *_ in LIFE
)
LIFE_INDEX = {
    "path": "life/",
    "title": "서울 생활권 출장마사지｜생활권별 홈타이 안내",
    "desc": "서울 생활권별 출장마사지·홈타이 안내. 강남, 홍대, 여의도, 성수 생활권 확인.",
    "h1": "서울 생활권별 안내",
    "breadcrumb": [("서울", "/"), ("생활권 안내", "")],
    "noindex": False,
    "body": f"""
<section id="intro">
<h2>생활권 기준으로 보는 법</h2>
<p>생활권은 행정구·행정동·역세권을 연결하는 허브입니다. 같은 구 안에서도 생활권에 따라 이용 목적과 방문 동선이 다르므로, 행정구 안내와 함께 생활권 기준으로 확인하면 더 정확합니다. 아래에서 서울 주요 생활권을 클릭해 포함 행정동과 가까운 역을 확인하세요.</p>
</section>
<section id="zones">
<h2>권역별 대표 생활권</h2>
<p>서울 5대 권역의 대표 생활권을 기준으로 가까운 행정구와 역을 함께 확인할 수 있습니다.</p>
<ul>{"".join(f'<li><a href="/zone/{z["slug"]}/">{z["name"]}</a> — {", ".join(z["life"][:4])} 등</li>' for z in ZONES)}</ul>
</section>
<section id="list">
<h2>서울 주요 생활권</h2>
<p>아래 생활권을 클릭하면 포함 행정동, 가까운 역, 관련 행정구, 방문 예약 안내가 담긴 상세 페이지로 이동합니다.</p>
<div class="card-grid">{_life_cards}</div>
</section>
{price_table()}
"""
}

PAGES = [LIFE_INDEX] + [_make_life_page(e) for e in LIFE]
