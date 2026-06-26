#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 (빙·네이버·얀덱스 등 공유 엔드포인트).

사용법:
  python tools/indexnow.py                 # sitemap.xml 의 전체 URL 통보(첫 일괄)
  python tools/indexnow.py URL [URL ...]   # 특정 URL만 통보(글 올릴 때마다)

IndexNow 는 한 번 제출하면 참여 검색엔진(Bing, Naver, Yandex, Seznam)에 공유됩니다.
구글은 IndexNow 미참여 → sitemap/Search Console 또는 Indexing API 사용(tools/google_indexing.py).
"""
import json
import os
import re
import sys
import urllib.request
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

BASE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", BASE).split("/")[0]
KEY_LOCATION = f"{BASE}/{INDEXNOW_KEY}.txt"

# IndexNow 공유 엔드포인트(제출 시 참여 엔진 전체에 전파) + 개별 엔드포인트
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://searchadvisor.naver.com/indexnow",
]


def read_sitemap_urls():
    sm = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sitemap.xml")
    if not os.path.exists(sm):
        sys.exit("sitemap.xml 이 없습니다. 먼저 python3 build.py 를 실행하세요.")
    with open(sm, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def submit(urls):
    if not INDEXNOW_KEY:
        sys.exit("INDEXNOW_KEY 가 비어 있습니다. content/site.py 를 확인하세요.")
    # IndexNow 1회 최대 10,000 URL
    payload = json.dumps({
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls[:10000],
    }).encode("utf-8")

    print(f"통보 대상: {len(urls)} URL  (host={HOST})")
    for ep in ENDPOINTS:
        req = urllib.request.Request(
            ep, data=payload,
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                print(f"  [{r.status}] {ep}")
        except urllib.error.HTTPError as e:
            # 200/202 외 코드도 정상 수신인 경우가 있어 본문까지 표기
            print(f"  [{e.code}] {ep}  {e.read().decode('utf-8', 'ignore')[:120]}")
        except Exception as e:  # 네트워크 등
            print(f"  [ERR] {ep}  {e}")


if __name__ == "__main__":
    arg_urls = [u for u in sys.argv[1:] if u.startswith("http")]
    urls = arg_urls if arg_urls else read_sitemap_urls()
    submit(urls)
