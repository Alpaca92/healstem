from datetime import date

import pandas as pd

# 택배
parcel = pd.read_excel('로젠택배_매트출고_바코드입력.xlsx', '택배', header=8)

# 전역변수
TODAY = str(date.today())

target = parcel.loc[parcel['날짜'] == '2022-05-09', ['물품명']]

print(target)
