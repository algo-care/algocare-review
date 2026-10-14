#!/usr/bin/env python3
"""reviews.json → reviews.js

후기(post) 하나에 멘트(quote)가 여러 개. 멘트 하나가 TV 한 장이다.
멘트가 MAX_QUOTES 를 넘으면 제출일이 가장 오래된 후기부터 통째로 뺀다.
원문 링크는 segno 로 QR(SVG) 을 미리 그려 넣는다.  pip3 install segno
"""
import io, json, pathlib

import segno

ROOT = pathlib.Path(__file__).resolve().parent
MAX_QUOTES = 50


def qr_svg(url: str) -> str:
    buf = io.BytesIO()
    segno.make(url, error='m').save(
        buf, kind='svg', border=2, xmldecl=False, svgns=False, nl=False, omitsize=True,
        dark='#211d1d', light='#fff', svgclass='segno', lineclass='qrline',
    )
    return buf.getvalue().decode()


def main() -> None:
    posts = json.loads((ROOT / 'reviews.json').read_text(encoding='utf-8'))
    posts = [p for p in posts if p.get('quotes')]
    while sum(len(p['quotes']) for p in posts) > MAX_QUOTES and len(posts) > 1:
        posts.remove(min(posts, key=lambda p: p.get('submitted', '')))  # 가장 오래된 후기 제거
    items = [
        {
            'kind': q.get('kind', 'praise'),
            'text': q['text'].strip(),
            'author': p['author'],
            'platform': p['platform'],
            'date': p.get('submitted', '')[:10],
            'url': p['url'],
            'qr': qr_svg(p['url']),
        }
        for p in posts for q in p['quotes']
    ]
    out = 'window.REVIEWS = ' + json.dumps(items, ensure_ascii=False, indent=1) + ';\n'
    (ROOT / 'reviews.js').write_text(out, encoding='utf-8')
    print(f'후기 {len(posts)}건 → 멘트 {len(items)}개 → reviews.js')


if __name__ == '__main__':
    main()
