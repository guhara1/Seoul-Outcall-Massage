# 서울 지하철역 개별 페이지 (45개) + 역 인덱스 — 고유 본문, 전부 색인
# 환승역도 역명 기준 1개 URL, 출구별 페이지 없음.
from .seoul_data import DISTRICTS, ZONES, _zone_of
from .seoul_dongs import DONG_SLUGS
from .site import BRAND, PHONE

# name, slug, lines, gu_slug, dongs[name], (life_name, life_slug), note(고유 1문장)
STATIONS = [
    ("강남역", "gangnam-station", "2호선·신분당선", "gangnam-gu", ["역삼동", "서초동"], ("강남·역삼", "gangnam-yeoksam"),
     "강남역은 테헤란로 업무지구와 강남대로 상권의 중심으로 평일·주말 모두 유동 인구가 많습니다."),
    ("역삼역", "yeoksam-station", "2호선", "gangnam-gu", ["역삼동", "논현동"], ("강남·역삼", "gangnam-yeoksam"),
     "역삼역은 테헤란로 오피스와 역삼동 주거형 오피스텔이 함께 있어 낮과 밤의 방문 동선이 다릅니다."),
    ("선릉역", "seolleung-station", "2호선·수인분당선", "gangnam-gu", ["삼성동", "대치동"], ("삼성·선릉", "samseong-seolleung"),
     "선릉역은 2호선과 수인분당선이 만나는 환승역으로 테헤란로 업무권의 한 축입니다."),
    ("삼성역", "samseong-station", "2호선", "gangnam-gu", ["삼성동"], ("삼성·선릉", "samseong-seolleung"),
     "삼성역은 코엑스·무역센터 전시·업무권의 중심으로 행사 시즌 혼잡을 감안해 예약하는 것이 좋습니다."),
    ("잠실역", "jamsil-station", "2호선·8호선", "songpa-gu", ["잠실동", "방이동"], ("잠실·송파", "jamsil-songpa"),
     "잠실역은 롯데월드타워·석촌호수 상권과 대단지가 맞닿은 송파의 환승 중심입니다."),
    ("석촌역", "seokchon-station", "8호선·9호선", "songpa-gu", ["석촌동", "삼전동"], ("잠실·송파", "jamsil-songpa"),
     "석촌역은 8·9호선 환승역으로 석촌호수와 주거권을 함께 끼고 있습니다."),
    ("문정역", "munjeong-station", "8호선", "songpa-gu", ["문정동", "가락동"], ("문정·가락", "munjeong-garak"),
     "문정역은 법조타운과 지식산업센터가 모인 업무 생활권의 거점입니다."),
    ("홍대입구역", "hongik-univ-station", "2호선·경의중앙선·공항철도", "mapo-gu", ["서교동", "연남동"], ("홍대·합정", "hongdae-hapjeong"),
     "홍대입구역은 상권·숙소·공항철도가 만나는 서북부 최대 유동 거점입니다."),
    ("합정역", "hapjeong-station", "2호선·6호선", "mapo-gu", ["합정동", "서교동"], ("홍대·합정", "hongdae-hapjeong"),
     "합정역은 2·6호선 환승역으로 홍대 상권과 망원 주거권 사이의 거점입니다."),
    ("공덕역", "gongdeok-station", "5호선·6호선·경의중앙선·공항철도", "mapo-gu", ["공덕동", "아현동"], ("공덕·마포", "gongdeok-mapo"),
     "공덕역은 네 개 노선이 만나는 다중 환승 거점으로 오피스·주거가 함께 있습니다."),
    ("여의도역", "yeouido-station", "5호선·9호선", "yeongdeungpo-gu", ["여의도동"], ("여의도·영등포", "yeouido-yeongdeungpo"),
     "여의도역은 금융 업무가의 중심으로 평일 낮 오피스 수요가 집중됩니다."),
    ("영등포역", "yeongdeungpo-station", "1호선", "yeongdeungpo-gu", ["영등포동"], ("여의도·영등포", "yeouido-yeongdeungpo"),
     "영등포역은 타임스퀘어와 전통 상권이 맞닿은 1호선 거점입니다."),
    ("당산역", "dangsan-station", "2호선·9호선", "yeongdeungpo-gu", ["당산동", "양평동"], ("문래·당산", "mullae-dangsan"),
     "당산역은 2·9호선 환승역으로 여의도와 문래 사이 주거·환승권입니다."),
    ("신림역", "sillim-station", "2호선·신림선", "gwanak-gu", ["신림동"], ("신림·서울대입구", "sillim-snu"),
     "신림역은 원룸·상권이 밀집한 관악의 최대 생활 거점입니다."),
    ("서울대입구역", "seoul-nat-univ-station", "2호선", "gwanak-gu", ["봉천동"], ("신림·서울대입구", "sillim-snu"),
     "서울대입구역은 봉천 주거권과 상권이 어우러진 2호선 거점입니다."),
    ("건대입구역", "konkuk-univ-station", "2호선·7호선", "gwangjin-gu", ["화양동", "자양동"], ("건대·광진", "konkuk-gwangjin"),
     "건대입구역은 대학가 상권과 2·7호선 환승이 만나는 동부 거점입니다."),
    ("구의역", "guui-station", "2호선", "gwangjin-gu", ["구의동"], ("건대·광진", "konkuk-gwangjin"),
     "구의역은 강변 환승권과 주거가 가까운 2호선 역입니다."),
    ("왕십리역", "wangsimni-station", "2호선·5호선·경의중앙선·수인분당선", "seongdong-gu", ["행당동", "마장동"], ("성수·왕십리", "seongsu-wangsimni"),
     "왕십리역은 네 개 노선이 만나는 성동의 대표 다중 환승 거점입니다."),
    ("성수역", "seongsu-station", "2호선", "seongdong-gu", ["성수동"], ("성수·왕십리", "seongsu-wangsimni"),
     "성수역은 카페·창업 상권으로 빠르게 성장한 2호선 거점입니다."),
    ("서울숲역", "seoulforest-station", "수인분당선", "seongdong-gu", ["성수동"], ("성수·왕십리", "seongsu-wangsimni"),
     "서울숲역은 서울숲과 주상복합이 맞닿은 수인분당선 역입니다."),
    ("용산역", "yongsan-station", "1호선·경의중앙선", "yongsan-gu", ["한강로동"], ("용산·서울역", "yongsan-seoul-station"),
     "용산역은 주상복합·업무 빌딩과 철도가 만나는 도심 관문입니다."),
    ("서울역", "seoul-station", "1호선·4호선·경의중앙선·공항철도", "jung-gu", ["중림동"], ("용산·서울역", "yongsan-seoul-station"),
     "서울역은 철도·공항철도가 모이는 도심 최대 교통 거점으로 호텔이 밀집해 있습니다."),
    ("이태원역", "itaewon-station", "6호선", "yongsan-gu", ["이태원동", "한남동"], ("한남·이태원", "hannam-itaewon"),
     "이태원역은 외국인 상권과 숙소가 발달한 6호선 거점입니다."),
    ("한강진역", "hangangjin-station", "6호선", "yongsan-gu", ["한남동"], ("한남·이태원", "hannam-itaewon"),
     "한강진역은 한남동 고급 주거·문화권과 가까운 6호선 역입니다."),
    ("사당역", "sadang-station", "2호선·4호선", "dongjak-gu", ["사당동"], ("노량진·동작", "noryangjin-dongjak"),
     "사당역은 2·4호선 환승과 광역버스가 모이는 남부 환승 거점입니다."),
    ("노량진역", "noryangjin-station", "1호선·9호선", "dongjak-gu", ["노량진동"], ("노량진·동작", "noryangjin-dongjak"),
     "노량진역은 학원가와 1·9호선 환승이 만나는 동작의 거점입니다."),
    ("구로디지털단지역", "guro-digital-complex-station", "2호선", "guro-gu", ["구로동"], ("구디·가디", "gd-gd"),
     "구로디지털단지역은 IT·업무 오피스텔이 밀집한 2호선 거점입니다."),
    ("가산디지털단지역", "gasan-digital-complex-station", "1호선·7호선", "geumcheon-gu", ["가산동"], ("구디·가디", "gd-gd"),
     "가산디지털단지역은 지식산업센터와 아울렛이 모인 1·7호선 환승 거점입니다."),
    ("신도림역", "sindorim-station", "1호선·2호선", "guro-gu", ["신도림동"], ("구디·가디", "gd-gd"),
     "신도림역은 1·2호선이 만나는 서남부 최대 환승 상권 거점입니다."),
    ("고속터미널역", "express-bus-terminal-station", "3호선·7호선·9호선", "seocho-gu", ["반포동"], ("잠실·송파", "jamsil-songpa"),
     "고속터미널역은 세 개 노선과 터미널·상권이 만나는 서초의 환승 거점입니다."),
    ("교대역", "seoul-edu-univ-station", "2호선·3호선", "seocho-gu", ["서초동"], ("강남·역삼", "gangnam-yeoksam"),
     "교대역은 법조타운과 2·3호선 환승이 만나는 서초의 업무 거점입니다."),
    ("양재역", "yangjae-station", "3호선·신분당선", "seocho-gu", ["양재동"], ("강남·역삼", "gangnam-yeoksam"),
     "양재역은 3호선·신분당선 환승과 양재 업무·주거권이 만나는 역입니다."),
    ("마곡역", "magok-station", "5호선", "gangseo-gu", ["마곡동"], ("마곡·발산", "magok-balsan"),
     "마곡역은 마곡지구 신업무·주거권의 5호선 거점입니다."),
    ("발산역", "balsan-station", "5호선", "gangseo-gu", ["발산동", "마곡동"], ("마곡·발산", "magok-balsan"),
     "발산역은 마곡 업무권과 화곡 주거권 사이의 5호선 역입니다."),
    ("화곡역", "hwagok-station", "5호선", "gangseo-gu", ["화곡동"], ("마곡·발산", "magok-balsan"),
     "화곡역은 빌라 밀집 주거권을 끼고 있는 강서의 5호선 생활 거점입니다."),
    ("목동역", "mok-dong-station", "5호선", "yangcheon-gu", ["목동"], ("목동·양천", "mokdong-yangcheon"),
     "목동역은 목동 학원가와 대단지를 끼고 있는 5호선 거점입니다."),
    ("오목교역", "omokgyo-station", "5호선", "yangcheon-gu", ["목동", "신정동"], ("목동·양천", "mokdong-yangcheon"),
     "오목교역은 목동 상권과 방송가가 가까운 5호선 역입니다."),
    ("연신내역", "yeonsinnae-station", "3호선·6호선", "eunpyeong-gu", ["불광동", "갈현동"], ("연신내·은평", "yeonsinnae-eunpyeong"),
     "연신내역은 3·6호선 환승과 상권이 모인 은평의 중심 거점입니다."),
    ("불광역", "bulgwang-station", "3호선·6호선", "eunpyeong-gu", ["불광동"], ("연신내·은평", "yeonsinnae-eunpyeong"),
     "불광역은 3·6호선 환승역으로 연신내 상권과 이어집니다."),
    ("노원역", "nowon-station", "4호선·7호선", "nowon-gu", ["상계동"], ("노원·상계", "nowon-sanggye"),
     "노원역은 4·7호선 환승과 상계 상권·대단지가 만나는 동북부 거점입니다."),
    ("상봉역", "sangbong-station", "7호선·경의중앙선·경춘선", "jungnang-gu", ["상봉동", "망우동"], ("상봉·중랑", "sangbong-jungnang"),
     "상봉역은 환승과 터미널 상권이 모인 중랑의 거점입니다."),
    ("종로3가역", "jongno-3-ga-station", "1호선·3호선·5호선", "jongno-gu", ["종로1·2·3·4가동"], ("종로·광화문", "jongno-gwanghwamun"),
     "종로3가역은 1·3·5호선이 만나는 도심 최대 환승 거점입니다."),
    ("광화문역", "gwanghwamun-station", "5호선", "jongno-gu", ["사직동"], ("종로·광화문", "jongno-gwanghwamun"),
     "광화문역은 도심 업무 빌딩이 밀집한 5호선 거점입니다."),
    ("명동역", "myeongdong-station", "4호선", "jung-gu", ["명동"], ("명동·을지로", "myeongdong-euljiro"),
     "명동역은 관광·호텔 상권의 중심인 4호선 거점입니다."),
    ("을지로입구역", "euljiro-1-ga-station", "2호선", "jung-gu", ["을지로동"], ("명동·을지로", "myeongdong-euljiro"),
     "을지로입구역은 업무·상권이 맞닿은 2호선 도심 거점입니다."),
]

STATION_SLUGS = {name: slug for name, slug, *_ in STATIONS}


# 행정동 이름 → 실제 소속 구(인접 역이 다른 구의 동을 가리킬 수 있어 정확히 해석)
DONG_TO_GU = {}
for _gs, _d in DISTRICTS.items():
    for _n, _ in _d["dongs"]:
        DONG_TO_GU.setdefault(_n, _gs)


def _dong_links(gu_slug, dongs):
    out = []
    for n in dongs:
        g = DONG_TO_GU.get(n, gu_slug)
        gu_name = DISTRICTS[g]["name"]
        if n in DONG_SLUGS:
            out.append(f'<li><a href="/{g}/{DONG_SLUGS[n]}/">{gu_name} {n}</a></li>')
        else:
            out.append(f"<li>{gu_name} {n}</li>")
    return "".join(out)


def _station_body(entry):
    name, slug, lines, gu_slug, dongs, (life_name, life_slug), note = entry
    gu_name = DISTRICTS[gu_slug]["name"]
    zone_slug, zone_name = _zone_of(gu_slug)
    dong_phrase = "·".join(dongs)
    return f"""
<section id="intro">
<h2>{name} 출장마사지·홈타이 안내</h2>
<p>{name}은(는) {lines}이(가) 지나는 {gu_name}의 지하철역으로, {dong_phrase} 일대와 가깝습니다. {note}</p>
<p>{name} 기준으로 출장마사지·홈타이를 예약할 때는 역세권 기준으로 가까운 행정동과 생활권을 확인하면 방문 동선을 잡기 쉽습니다. 정확한 주소와 건물 유형, 예약 가능 시간을 먼저 알려주시면 방문이 원활합니다.</p>
</section>

<section id="lines">
<h2>{name} 노선·환승 안내</h2>
<p>{name}은(는) {lines} 노선이 지납니다. 환승역도 노선별로 나누지 않고 역명 기준 하나로 안내하며, 출구별 페이지는 따로 만들지 않습니다. 방문 시 도착 출구와 건물 출입구를 분명히 정해두면 동선이 빠릅니다.</p>
</section>

<section id="nearby">
<h2>{name} 인접 행정동</h2>
<p>{name}에서 가까운 행정동입니다. 각 동을 클릭하면 인접 동과 예약 전 확인사항을 확인할 수 있습니다.</p>
<ul>{_dong_links(gu_slug, dongs)}</ul>
</section>

<section id="life">
<h2>{name} 관련 생활권</h2>
<p>{name}은(는) <a href="/life/{life_slug}/">{life_name}</a> 생활권과 연결되며, <a href="/{gu_slug}/">{gu_name} 출장마사지·홈타이 안내</a>와 <a href="/zone/{zone_slug}/">{zone_name}</a> 권역에서 더 넓은 범위를 확인할 수 있습니다.</p>
</section>

<section id="visit">
<h2>{name} 방문 예약 안내</h2>
{DISTRICTS[gu_slug]['character']}
<p>{name} 인근으로 방문할 때는 건물 유형에 따라 출입 방식이 다릅니다. 오피스텔·업무 빌딩은 로비 방문자 등록과 엘리베이터 카드를, 주거 단지는 공동현관과 주차를, 호텔·숙소는 객실과 출입 절차를 미리 확인하면 방문이 원활합니다. 목적별 상세는 <a href="/purpose/">이용 목적별 안내</a>를 참고하세요.</p>
<p>예약 시 {name} 기준 정확한 주소(건물명·동·호수)와 희망 시간, 연락처를 알려주시면 도착 안내가 빠릅니다. 예약 방법은 <a href="/reservation/">예약 안내</a>, 방문 전 점검은 <a href="/check/">이용 전 확인사항</a>에서 확인할 수 있습니다.</p>
</section>

<section id="source">
<h2>{name} 안내 정보 및 출처</h2>
<p><strong>작성·운영</strong>: {BRAND} 고객센터 · <a href="tel:{PHONE}">{PHONE}</a> (연중무휴 24시간 상담). 본 페이지는 {name} 일대 방문 예약 전 확인을 돕기 위한 역세권 안내입니다.</p>
<p><strong>지역 정보 참고</strong>: <a href="https://ko.wikipedia.org/wiki/{gu_name}" target="_blank" rel="noopener">위키백과 {gu_name}</a> · <a href="/station/">지하철역 안내</a> · <a href="/check/">이용 전 확인사항</a></p>
</section>
"""


def _make_station_page(entry):
    name, slug = entry[0], entry[1]
    gu_name = DISTRICTS[entry[3]]["name"]
    return {
        "path": f"station/{slug}/",
        "title": f"{name} 출장마사지·홈타이｜{gu_name} 역세권 방문 안내",
        "desc": f"{name} 출장마사지·홈타이 예약 전 인접 행정동과 생활권을 확인하세요.",
        "h1": f"{name} 출장마사지",
        "breadcrumb": [("서울", "/"), ("지하철역 안내", "/station/"), (name, "")],
        "body": _station_body(entry),
        "noindex": False,
    }


# 역 인덱스
_station_cards = "".join(
    f'<a href="/station/{slug}/" class="card"><h3>{name}</h3>'
    f'<p>{DISTRICTS[gu_slug]["name"]} · {lines}</p><span class="card-arrow">→</span></a>'
    for name, slug, lines, gu_slug, *_ in STATIONS
)
STATION_INDEX = {
    "path": "station/",
    "title": "서울 지하철역 출장마사지｜역세권별 홈타이 안내",
    "desc": "서울 주요 지하철역 출장마사지·홈타이 안내. 강남역, 잠실역, 홍대입구역 등 확인.",
    "h1": "서울 주요 지하철역별 안내",
    "breadcrumb": [("서울", "/"), ("지하철역 안내", "")],
    "noindex": False,
    "body": f"""
<section id="intro">
<h2>서울 역세권 기준으로 보는 법</h2>
<p>서울은 행정구가 명확하지만 실제 이동은 지하철역을 기준으로 움직이는 경우가 많습니다. 같은 강남구라도 강남역과 삼성역은 인접 생활권과 방문 동선이 다르므로, 역세권 기준으로 보면 가까운 행정동과 예약 동선을 잡기 쉽습니다. 환승역은 노선별로 나누지 않고 역명 기준 하나로 안내하며, 출구별 페이지는 만들지 않습니다.</p>
</section>
<section id="zones">
<h2>권역별 대표 역</h2>
<p>서울 5대 권역의 대표 역을 기준으로 인접 생활권과 행정구를 함께 확인할 수 있습니다.</p>
<ul>{"".join(f'<li><a href="/zone/{z["slug"]}/">{z["name"]}</a> — {", ".join(z["stations"][:4])} 등</li>' for z in ZONES)}</ul>
</section>
<section id="list">
<h2>서울 주요 지하철역</h2>
<p>아래 역을 클릭하면 노선·환승, 인접 행정동, 관련 생활권, 방문 예약 안내가 담긴 상세 페이지로 이동합니다.</p>
<div class="card-grid">{_station_cards}</div>
</section>
"""
}

PAGES = [STATION_INDEX] + [_make_station_page(e) for e in STATIONS]
