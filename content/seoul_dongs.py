# 서울 행정동 페이지 — 구별 행정동 전체 생성(클릭 가능, 고유 본문)
#
# 도어웨이 리스크 관리:
#  - 각 페이지는 "지역명만 바꾼 복제"가 아니라, 해당 동의 고유 설명 +
#    같은 구의 '인접 행정동(설명 포함)' 목록(페이지마다 집합이 다름) +
#    가까운 역·생활권·구 특성을 조합해 페이지마다 실제로 다른 본문을 만든다.
#  - 1차에는 모든 행정동 페이지를 noindex,follow 로 둔다(단계적 색인).
#    얇은 위치 페이지가 대량 색인되어 사이트 단위 품질 신호를 떨어뜨리는
#    도어웨이 위험을 피하고, 본문이 1,500자 이상으로 보강된 동부터 색인한다.
from .seoul_data import DISTRICTS, DISTRICT_ORDER, _zone_of

# 행정동 이름 → URL 슬러그 (구 경로 하위라 구 간 중복은 무방)
DONG_SLUGS = {
    # 강남구
    "역삼동": "yeoksam", "논현동": "nonhyeon", "삼성동": "samseong", "청담동": "cheongdam",
    "압구정동": "apgujeong", "신사동": "sinsa", "대치동": "daechi", "도곡동": "dogok",
    "개포동": "gaepo", "수서동": "suseo",
    # 서초구
    "서초동": "seocho", "반포동": "banpo", "잠원동": "jamwon", "방배동": "bangbae",
    "양재동": "yangjae", "내곡동": "naegok",
    # 송파구
    "잠실동": "jamsil", "방이동": "bangi", "석촌동": "seokchon", "송파동": "songpa",
    "삼전동": "samjeon", "가락동": "garak", "문정동": "munjeong", "장지동": "jangji",
    "위례동": "wirye", "거여동": "geoyeo",
    # 강동구
    "천호동": "cheonho", "성내동": "seongnae", "길동": "gil", "둔촌동": "dunchon",
    "명일동": "myeongil", "암사동": "amsa", "강일동": "gangil",
    # 마포구
    "서교동": "seogyo", "합정동": "hapjeong", "상수동": "sangsu", "연남동": "yeonnam",
    "망원동": "mangwon", "공덕동": "gongdeok", "아현동": "ahyeon", "도화동": "dohwa",
    "상암동": "sangam", "성산동": "seongsan",
    # 서대문구
    "신촌동": "sinchon", "연희동": "yeonhui", "홍제동": "hongje", "홍은동": "hongeun",
    "남가좌동": "namgajwa", "북가좌동": "bukgajwa", "충현동": "chunghyeon", "천연동": "cheonyeon",
    # 은평구
    "불광동": "bulgwang", "응암동": "eungam", "역촌동": "yeokchon", "녹번동": "nokbeon",
    "갈현동": "galhyeon", "구산동": "gusan", "대조동": "daejo", "진관동": "jingwan",
    "수색동": "susaek", "증산동": "jeungsan",
    # 영등포구
    "여의도동": "yeouido", "영등포동": "yeongdeungpo", "당산동": "dangsan", "문래동": "mullae",
    "양평동": "yangpyeong", "신길동": "singil", "대림동": "daerim", "도림동": "dorim",
    # 구로구
    "구로동": "guro", "신도림동": "sindorim", "가리봉동": "garibong", "고척동": "gocheok",
    "개봉동": "gaebong", "오류동": "oryu", "항동": "hang",
    # 금천구
    "가산동": "gasan", "독산동": "doksan", "시흥동": "siheung",
    # 강서구
    "마곡동": "magok", "발산동": "balsan", "화곡동": "hwagok", "등촌동": "deungchon",
    "가양동": "gayang", "염창동": "yeomchang", "공항동": "gonghang", "방화동": "banghwa",
    # 양천구
    "목동": "mok", "신정동": "sinjeong", "신월동": "sinwol",
    # 관악구
    "신림동": "sillim", "봉천동": "bongcheon", "남현동": "namhyeon", "난곡": "nangok", "난향": "nanhyang",
    "낙성대": "nakseongdae",
    # 동작구
    "노량진동": "noryangjin", "상도동": "sangdo", "흑석동": "heukseok", "사당동": "sadang",
    "대방동": "daebang", "신대방동": "sindaebang",
    # 성동구
    "성수동": "seongsu", "왕십리": "wangsimni", "행당동": "haengdang", "마장동": "majang",
    "금호동": "geumho", "옥수동": "oksu", "응봉동": "eungbong", "용답동": "yongdap",
    # 광진구
    "화양동": "hwayang", "자양동": "jayang", "구의동": "guui", "광장동": "gwangjang",
    "중곡동": "junggok", "군자동": "gunja", "능동": "neung",
    # 동대문구
    "청량리동": "cheongnyangni", "회기동": "hoegi", "이문동": "imun", "전농동": "jeonnong",
    "답십리동": "dapsimni", "장안동": "jangan", "휘경동": "hwigyeong",
    # 중랑구
    "면목동": "myeonmok", "상봉동": "sangbong", "중화동": "junghwa", "묵동": "muk",
    "망우동": "mangu", "신내동": "sinnae",
    # 노원구
    "상계동": "sanggye", "중계동": "junggye", "하계동": "hagye", "공릉동": "gongneung", "월계동": "wolgye",
    # 도봉구
    "창동": "chang", "쌍문동": "ssangmun", "방학동": "banghak", "도봉동": "dobong",
    # 강북구
    "수유동": "suyu", "미아동": "mia", "번동": "beon", "우이동": "ui", "인수동": "insu",
    # 성북구
    "성신여대": "sungshin", "길음동": "gireum", "돈암동": "donam", "정릉동": "jeongneung",
    "안암동": "anam", "종암동": "jongam", "석관동": "seokgwan",
    # 종로구
    "종로1·2·3·4가동": "jongno-ga", "사직동": "sajik", "혜화동": "hyehwa", "이화동": "ihwa",
    "가회동": "gahoe", "부암동": "buam", "청운효자동": "cheongun-hyoja", "창신동": "changsin",
    # 중구
    "명동": "myeongdong", "소공동": "sogong", "회현동": "hoehyeon", "을지로동": "euljiro",
    "필동": "pil", "신당동": "sindang", "약수동": "yaksu", "장충동": "jangchung", "중림동": "jungnim",
    # 용산구
    "한남동": "hannam", "이태원동": "itaewon", "한강로동": "hangangno", "이촌동": "ichon",
    "후암동": "huam", "남영동": "namyeong", "청파동": "cheongpa", "보광동": "bogwang", "서빙고동": "seobinggo",
}


def get_dong_slug(name):
    return DONG_SLUGS.get(name)


def _dong_body(gu_slug, d, name, desc):
    gu_name = d["name"]
    zone_slug, zone_name = _zone_of(gu_slug)

    # 인접 행정동 — 자기 자신 제외(페이지마다 집합·설명이 달라 고유성 확보)
    siblings = [(n, s) for (n, s) in d["dongs"] if n != name]
    sib_items = "".join(
        f'<li><a href="/{gu_slug}/{DONG_SLUGS[n]}/"><strong>{n}</strong></a> — {s}</li>'
        for (n, s) in siblings if n in DONG_SLUGS
    )
    stations_txt = ", ".join(d["stations"][:5])
    life_items = "".join(f'<li><a href="/life/">{l}</a></li>' for l in d["life"])

    return f"""
<section id="intro">
<h2>{name} 출장마사지·홈타이 방문 안내</h2>
<p>{name}은(는) {gu_name} {desc}입니다. {name} 일대로 출장마사지·홈타이를 예약할 때는 정확한 방문 주소와 건물 유형, 예약 가능 시간을 먼저 확인하면 방문이 한결 수월합니다.</p>
{d['character']}
</section>

<section id="stations">
<h2>{name}에서 가까운 지하철역</h2>
<p>{name} 방문 시 동선의 기준이 되는 {gu_name}의 가까운 지하철역은 {stations_txt} 등입니다. 가장 가까운 역을 기준으로 예약 시간과 이동 동선을 정하면 편리합니다.</p>
</section>

<section id="nearby">
<h2>{name} 인접 행정동 안내</h2>
<p>{name}과(와) 생활권이 이어지는 {gu_name}의 인접 행정동입니다. 함께 확인하면 방문 가능 범위를 넓게 볼 수 있습니다.</p>
<ul>{sib_items}</ul>
</section>

<section id="area">
<h2>{name}이(가) 속한 생활권</h2>
<p>{name}은(는) {gu_name}(<a href="/zone/{zone_slug}/">{zone_name}</a>) 생활권에 속합니다. <a href="/{gu_slug}/">{gu_name} 출장마사지·홈타이 안내</a>에서 전체 행정동과 역세권, 생활권을 확인할 수 있습니다.</p>
<ul class="link-cloud">{life_items}</ul>
</section>

<section id="check">
<h2>{name} 예약 전 확인사항</h2>
<p>방문 가능 주소와 건물 유형, 예약 가능 시간, 건물 출입 방식, 결제 방식을 먼저 확인하세요. 자세한 사항은 <a href="/check/">이용 전 확인사항</a>과 <a href="/reservation/">예약 안내</a>를 참고하시고, 개인정보 처리 기준은 <a href="/support/privacy/">개인정보처리방침</a>에서 확인할 수 있습니다.</p>
<p>{gu_name} {name} 지역은 건전한 방문 관리 서비스만 제공하며, 불법·선정적 서비스 요청에는 어떤 경우에도 응하지 않습니다.</p>
</section>
"""


def _make_dong_page(gu_slug, d, name, desc):
    slug = DONG_SLUGS[name]
    zone_slug, zone_name = _zone_of(gu_slug)
    gu_name = d["name"]
    return {
        "path": f"{gu_slug}/{slug}/",
        "title": f"{name} 출장마사지·홈타이｜{gu_name} 생활권 방문 안내",
        "desc": f"{gu_name} {name} 출장마사지·홈타이 예약 전 가까운 역과 인접 동을 확인하세요.",
        "h1": f"{gu_name} {name} 출장마사지",
        "breadcrumb": [("서울", "/"), (gu_name, f"/{gu_slug}/"), (name, "")],
        "body": _dong_body(gu_slug, d, name, desc),
        # 도어웨이 위험 차단: 1차에는 색인 제외(크롤·링크는 허용), 보강 후 단계적 색인
        "noindex": True,
    }


PAGES = []
for _gu in DISTRICT_ORDER:
    _d = DISTRICTS[_gu]
    for _name, _desc in _d["dongs"]:
        if _name in DONG_SLUGS:
            PAGES.append(_make_dong_page(_gu, _d, _name, _desc))

# 슬러그 누락 점검(빌드 시 조용한 누락 방지)
_missing = sorted({n for _gu in DISTRICT_ORDER for (n, _) in DISTRICTS[_gu]["dongs"]} - set(DONG_SLUGS))
if _missing:
    raise SystemExit(f"[seoul_dongs] DONG_SLUGS 누락: {_missing}")
