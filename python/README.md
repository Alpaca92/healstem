# 재고관리 자동화를 위한 메뉴얼

[download link](https://github.com/Alpaca92/healstem/archive/refs/heads/master.zip)

## 바코드 입력 엑셀 물품명 셀 작성

1. 각 물품의 구분은 반드시 `,`으로 한다

```
ex. -홍길동 싱3,싱카3,의2,의카2,슈3,김철수님 개인물품,@김영희 미15(12/31 주문)
```

2. 행사 등으로 인한 수량은 괄호안에 세부내용을 작성한다

```
⭕ ex. 메20(18+2)
❌ ex. 메18+2
```

3. 줄임말은 반드시 아래의 표와 같이 작성한다

|물품명|줄임말|
|:---:|:----:|
|의자|의|
|싱글|싱|
|슈퍼|슈|
|110v의자|110v의|
|110v싱글|110v싱|
|110v슈퍼|110v슈|
|의카|의카|
|싱카|싱카|
|슈카|슈카|
|프로틴|프|
|메가힐링|메|
|샤워기|샤|
|수전|수|
|간장|간|
|된장|된|
|샴푸|샴|
|세탁|세|
|2종|2종|
|4종|4종|
|크림|크|
|세럼|세럼|
|미스트|미|
|카밍젤|카|
|클렌징|클|
|선크림|선|
|코스메틱접지|접지|
|코스메틱카달로그|카달로그|

## \*references

- [pandas](https://pandas.pydata.org/)

- [Assertions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Assertions)

- [How to write to an existing excel file without overwriting data (using pandas)?](https://stackoverflow.com/questions/20219254/how-to-write-to-an-existing-excel-file-without-overwriting-data-using-pandas)

- [정규표현식 python re r' (raw string)](https://newpower.tistory.com/116)

- [Regular Expressions: Search in list](https://stackoverflow.com/questions/3640359/regular-expressions-search-in-list)

- [search()](https://www.w3schools.com/python/gloss_python_regex_match.asp)

- [filter()](https://www.w3schools.com/python/ref_func_filter.asp)

- [[JavaScript] 정규표현식 - 문자열에 한글 있는지 검사하기](https://eblee-repo.tistory.com/40)

- [Python 정규 표현식으로 추출하기 4가지 사용 방법](https://ponyozzang.tistory.com/279)

- [Python - 문자를 숫자로 변환 (String to Integer, Float)](https://codechacha.com/ko/python-convert-string-to-integer/)

- [[파이썬] 파이썬 Dictionary, get(), keys(), values(), items() 사용법, 파이썬 mapping type - 공부하는 도비](https://yang-wistory1009.tistory.com/38)

















