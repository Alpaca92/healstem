from datetime import date

import pandas as pd

# 택배
parcel = pd.read_excel('로젠택배_매트출고_바코드입력.xlsx', '택배', header=8)

# 전역변수
TODAY = str(date.today())
products = {
'의자': 0,
'싱글': 0,
'슈퍼': 0,
'110v의자': 0,
'110v싱글': 0,
'110v슈퍼': 0,
'의카': 0,
'싱카': 0,
'슈카': 0,
'프로틴': 0,
'메가힐링': 0,
'샤워기': 0,
'수전': 0,
'간장': 0,
'된장': 0,
'샴푸': 0,
'세탁': 0,
'2종': 0,
'4종': 0,
'크림': 0,
'세럼': 0,
'미스트': 0,
'카밍젤': 0,
'클렌징': 0,
'선크림': 0,
'코스메틱접지': 0,
'코스메틱카달로그': 0,
}

target = parcel.loc[parcel['날짜'] == '2022-05-10', ['물품명']]

for i in target.index:
  product_name = target['물품명'][i]
  split_list = product_name.split(',')
  
  products += split_list
  
print(products)
