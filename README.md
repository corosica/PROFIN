# PROFIN

PROFIN 금융 프로젝트

PROFIN 이란?
- PROFIT + FIN = PROFIN 이득보는 재태크 앱

프로젝트 로드뷰
- 싸피 출신 개발자 최차윤은 드디어 취업에 성공 했습니다.
- 결혼 후 자가마련을 위해 재테크 계획을 세우려고 합니다.
- 그런데, 신입사원이라 은행에 갈 시간이 없어 금융 정보를 한 곳에 알 수 있는 웹 애플리케이션을 직접 만들어 보려고 합니다.


구현(필수)
- 메인 페이지 ( 연결통로 )
- 회원 커스터마이징 ( 유저관련 )
- 예적금 금리 비교 (API)
- 환율 계산기 (API/데이터이용)
- 근처 은행 검색 (API)
- 커뮤니티(게시판) (게시판관련)
- 프로필 페이지 (유저관련)
- 금융 상품 추천 알고리즘 (API/기존데이터)

### 구상
![구상 틀](<구상 틀(최초).png>)
#### API 관련
1. 예금,적금 데이터 API
        - https://finlife.fss.or.kr/finlife/main/contents.do?menuNo=700029
        - 금융감독원 홈페이지
        
        - 전체조회
            - 필터링
        - 개별 상세조회
            - 북마크(좋아요기능,가입하기)
        - 관리자 기능
            - 금리 수정 => 메일로 발송(email필수)
            - (django.core.mail)  네이버, Twilio 등을 활용합니다
    2. 환율 계산기
        - https://www.koreaexim.go.kr/ir/HPHKIR020M01?apino=2&viewtype=C&searchselect=&searchword
        - API활용 
        - 계산하는 로직 넣기
        - 나라선택(밑으로 내려가는 선택창?)
    3. 근처 은행 검색
        - https://apis.map.kakao.com/
        - 카카오맵 API
### ERD(DB 관계도)
![ERD2](<ERD2.png>)


### 계획(일자)


SERFIN  => 이름 후보 (서핑 + FIN)
I. 팀원 정보 및 업무 분담 내역
II. 설계 내용(아키텍처 등) 및 실제 구현 정도
III. 데이터베이스 모델링(ERD)
IV. 금융 상품 추천 알고리즘에 대한 기술적 설명
V. 서비스 대표 기능들에 대한 설명
VI. 기타(느낀 점, 후기 등)

## 버전관리


## 진행사항



## 추가
- 플로우차트/스토리보드 활용

===
- 완성한 후 작성할 것
## 개요

## 서비스 소개

## 서비스 화면

## 주요 기능

## ERD

## 알고리즘

## 작업 진행상황
- 05/08 
    - 기본계획 작성
    - 구현 필요한 내용 정리(필요 API 및 필수 구현 내용)
    - ERD에 들어가야 할 내용 간단 정리

- 05/09 
    - ERD/기본 웹 틀(UI/UX)
    - ERD - erdcloud 사용
    - 어플리케이션 기본 틀 제작(UI/UX) - oven 사용
    - 기존 구상 현황 명시적으로 변경할 것(플로우차트/스토리보드 활용)
    - 로고 제작

- 05/12
    - gitignore, requirements 작성 및 CORS에러 방지 corsheader 작성
    - 유저 정보 및 수정 페이지 ERD에 맞춰서 정정
    - 비밀번호 변경 페이지 작성
    - 근처 은행 검색 페이지 작성

- 05/13
    - 플로우 차트 
    - 메인 페이지 -> 커뮤니티 작성
    - 메인 페이지 -> 환율 계산기 작성

    - 카카오 오븐
    - 이용자 서비스 ->환율 계산기 페이지 작성

- 5/14
    - 게시판 CRUD 기능 구현
    - 환율 계산기를 위한 API사용 구현
    - vue 기본 프로젝트 생성
    
- 05/16
    - 예금 정보 API 활용 데이터 저장 및 조회기능 구현
    - 회원가입, 로그인 기능 구현
    - 이슈 : 로그인 여부가 새로고침 할 때 사라짐(Token값)
    - 메인, 커뮤니티 등 기본 페이지 구현

- 05/17
    - (이슈 해결) JWT 토큰 사용하여 로그인 유지 기능 구현
    - 게시글 상세 페이지(삭제/수정/뒤로가기, 댓글 생성/삭제) 구현
    - 지도 입력 View 및 주변은행 출력 API 구현
    - 카카오 맵 API 기본 출력 구현

- 05/19
    - 카카오맵 API로 지도 구현
    - 로그인/회원가입/로그아웃 로직 구현
    - Carousel(이하 회전목마) 구현
    - 프로필, 환율 페이지 구현
    - 메인 페이지, 카카오맵, 게시판, 유저 기본 css 

- 05/20
    - 메인페이지/유저정보/로그인/회원가입/환율 계산기 css 추가
    - 회원가입, 유저정보(닉네임, 성별등 추가) 로직 수정 + vue에서 추가
    - 네비바 드롭다운 형식으로 변경
    - 커뮤니티 작성자 닉네임으로 나타나게 구현
    - 금융상품 전체 목록 불러오기 구현
    - 커뮤니티 게시글 10개 단위로 끊기 구현
    - 커뮤니티 게시판 검색 기능(작성자, 제목) 추가
    - 게시판(작성, 수정, 상세)/카카오 맵/ css 깔끔하게
    - FAQ 페이지 작성
    - 금융 데이터 정리 및 내림차순/오름차순 정리 구현

- 05/21




## 팀원 소개 및 소감
 - 총괄 팀장: GPT
 - 팀장 : 정진우
 - 팀원 : 정유진
