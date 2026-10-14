# 알고케어 유저 후기 TV

사무실 TV에 고객 후기 멘트를 롤링으로 띄우는 페이지입니다. 저장소 루트(`index.html`, `reviews.js`)가 GitHub Pages로 배포됩니다.

TV 주소: https://algo-care.github.io/algocare-review/

## 후기 추가·수정
1. `reviews.json` 맨 앞에 후기를 추가합니다. 후기 하나에 좋은 멘트를 0~5개 넣습니다(좋은 멘트가 없으면 비워도 됩니다).
2. `python3 build.py`를 실행해 `reviews.js`를 다시 만듭니다. 멘트 50개를 넘으면 제출일이 가장 오래된 후기부터 빠집니다.
3. 커밋하고 푸시하면 TV 화면에 6시간 안에 반영됩니다.

필요한 패키지: `pip3 install segno`

## 출처
#00_혜택신청알림 채널의 "알고케어 SNS 리뷰 이벤트 신청"으로 들어온 블로그·인스타그램 후기입니다. 고객 이름과 연락처는 저장하지 않습니다.

## 자동 갱신
매주 월요일 09:00 클라우드 루틴 「후기 TV 주간 갱신」이 #00_혜택신청알림의 새 "알고케어 SNS 리뷰 이벤트 신청"을 읽어 후기 원문에서 좋은 멘트를 뽑고, `reviews.json`에 추가한 뒤 `build.py`를 돌려 main에 커밋합니다. 사무실 웰컴보드(`algo-care/welcome-board`)는 같은 날 09:30에 이 저장소의 `reviews.json`을 받아 갑니다.
