# 서울 출장마사지 사이트

서울특별시 전지역 방문 관리 서비스(출장마사지·홈타이) 안내 정적 사이트입니다.
행정구·행정동·지하철역·생활권 통합형 구조로 설계되었습니다.

**상호**: 간다 GO
**예약전화**: 0508-202-4719

## 구조

- **정적 HTML 사이트** — 어느 호스팅(Cloudflare Pages, GitHub Pages, Netlify)에서든 그대로 서빙
- **build.py** + **content/** — 페이지를 Python으로 정의하고 정적 HTML 생성
- **생성물** — 각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`

```
build.py                    # 빌드 스크립트
content/
  site.py                  # 상호·전화·도메인·메뉴
  seoul_data.py            # 5대 권역 + 25개 구 데이터(고유 콘텐츠)
  main.py                  # 서울 메인 (/seoul/)
  zones.py                 # 5대 권역 허브
  districts.py             # 25개 행정구 + 행정구 인덱스
  info.py                  # 예약·확인·고객센터·개인정보 + 역/생활권 인덱스 + 루트 리다이렉트
assets/
  style.css                # 프리미엄 다크 + 오렌지/샴페인골드 + Pretendard + 오버레이
  nav.js                   # 모바일 네비게이션
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수와 색인 여부 리포트가 출력됩니다.

## URL 구조

- 메인: `/seoul/` (루트 `/`는 `/seoul/`로 리다이렉트)
- 권역: `/seoul/zone/{zone}-area/` (강남권·서남권·동북권·서북권·도심권)
- 행정구: `/seoul/{gu-slug}/` (예: `/seoul/gangnam-gu/`)
- 행정구 인덱스: `/seoul/district/`
- 지하철역 인덱스: `/seoul/station/` · 생활권 인덱스: `/seoul/life/`
- 정보: `/seoul/reservation/`, `/seoul/check/`, `/seoul/support/`, `/seoul/support/privacy/`

URL에는 chuljangmassage·hometai·massage를 붙이지 않으며, 메뉴명에 "출장마사지"를 반복하지 않습니다.

## SEO 운영 원칙

- 본문 1,200자 미만 페이지는 자동 `noindex` (단계적 색인)
- 5대 권역 허브를 먼저 두고 → 25개 구 → 행정동·역·생활권으로 확장
- 지하철역은 역명 기준 1개 URL, 환승역도 노선별로 쪼개지 않음, 출구별 페이지 없음
- 번호동은 대표동으로 묶음 (역삼1·2동 → 역삼동)
- 같은 본문에서 지역명만 바꾸는 방식 금지 (구·권역별 고유 본문)
- 예약 전 확인사항, 개인정보 처리 기준, 불법·선정적 서비스 불가 안내 포함
- JSON-LD 스키마: Organization, HealthAndBeautyBusiness, FAQPage, BreadcrumbList, WebPage
- 푸터에 공식·공공 정보 권위 링크(서울시청·서울교통공사·보건복지부·한국소비자원) — E-E-A-T

## 개발 현황

### 1차 구축 완료 (32페이지 색인)
- ✅ 서울 메인 페이지 (5대 권역·25개 구·역세권·이용목적·FAQ·참고자료)
- ✅ 5대 권역 허브 (강남·서남·동북·서북·도심)
- ✅ 25개 행정구 페이지 (구별 고유 본문 + 예약·방문 팁)
- ✅ 행정구 인덱스
- ✅ 정보 페이지 (예약·확인·고객센터·개인정보)
- ✅ 지하철역/생활권 인덱스 허브
- ✅ 프리미엄 팔레트 + 컴포넌트 오버레이 CSS
- ✅ 푸터 오렌지 버튼(웹사이트 제작문의·제휴문의, 텔레그램) + 공식 정보 링크

### 2차 확장 예정 (단계적 색인)
- 🔄 핵심 행정동 70개 페이지 (`/seoul/{gu}/{dong}/`, 본문 1,500자+)
- 🔄 핵심 지하철역 45개 페이지 (`/seoul/station/{station}/`)
- 🔄 핵심 생활권 24개 페이지 (`/seoul/life/{area}/`)
- 🔄 이용 목적별 안내 6개 페이지

## 배포 전 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행
3. Google Search Console에 `sitemap.xml` 제출
4. GSC 노출·문의 데이터를 보고 행정동·역·생활권 페이지 2차 작성
