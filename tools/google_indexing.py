#!/usr/bin/env python3
"""구글 Indexing API 통보 (구글은 IndexNow 미참여 → 별도 경로).

준비:
  1) Google Cloud 콘솔에서 프로젝트 생성 → "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드
  3) Google Search Console 에서 해당 사이트 속성에 서비스 계정 이메일을
     "소유자(Owner)" 권한으로 추가
  4) pip install google-auth requests

사용법:
  GOOGLE_SA_JSON=/path/to/service-account.json python tools/google_indexing.py
  GOOGLE_SA_JSON=... python tools/google_indexing.py URL [URL ...]

주의: Indexing API 는 공식적으로 JobPosting·BroadcastEvent 구조화 페이지를
위한 것입니다. 일반 페이지도 크롤 우선순위 통보에 흔히 쓰이나, 색인 보장은
sitemap + Search Console 이 기본입니다. (일 200건 쿼터)
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL  # noqa: E402

ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def read_sitemap_urls():
    sm = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sitemap.xml")
    if not os.path.exists(sm):
        sys.exit("sitemap.xml 이 없습니다. 먼저 python3 build.py 를 실행하세요.")
    with open(sm, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def main():
    sa = os.environ.get("GOOGLE_SA_JSON")
    if not sa or not os.path.exists(sa):
        sys.exit("GOOGLE_SA_JSON 환경변수에 서비스 계정 JSON 경로를 지정하세요.")
    try:
        from google.oauth2 import service_account
        import google.auth.transport.requests
        import requests
    except ImportError:
        sys.exit("의존성 누락: pip install google-auth requests")

    creds = service_account.Credentials.from_service_account_file(sa, scopes=SCOPES)
    creds.refresh(google.auth.transport.requests.Request())
    headers = {"Authorization": f"Bearer {creds.token}",
               "Content-Type": "application/json"}

    arg_urls = [u for u in sys.argv[1:] if u.startswith("http")]
    urls = arg_urls if arg_urls else read_sitemap_urls()
    print(f"구글 Indexing API 통보: {len(urls)} URL (일 쿼터 200건)")
    ok = 0
    for u in urls[:200]:
        body = {"url": u, "type": "URL_UPDATED"}
        r = requests.post(ENDPOINT, headers=headers, json=body, timeout=30)
        flag = "OK" if r.status_code == 200 else f"ERR {r.status_code}"
        if r.status_code == 200:
            ok += 1
        print(f"  [{flag}] {u}")
    print(f"완료: {ok}/{min(len(urls),200)} 성공")


if __name__ == "__main__":
    main()
