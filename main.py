import re
from datetime import date
from re import search
from unicodedata import name

import pandas as pd

# 택배
df = pd.read_excel('로젠택배_매트출고_바코드입력.xlsx', '택배', header=8)

# 전역변수
TODAY = str(date.today())
result = {
  '의': {
    'regex': '\B의\d+',
    'name':'의자',
    'amount': 0
  },
  '싱': {
    'regex': '\B싱\d+',
    'name':'싱글',
    'amount': 0
  },
  '슈': {
    'regex': '\B슈\d+',
    'name':'슈퍼',
    'amount': 0
  },
  '110v의': {
    'regex': '110v의\d+',
    'name':'110v의자',
    'amount': 0
  },
  '110v싱': {
    'regex': '110v싱\d+',
    'name':'110v싱글',
    'amount': 0
  },
  '110슈': {
    'regex': '110v슈\d+',
    'name':'110v슈퍼',
    'amount': 0
  },
  '의카': {
    'regex': '의카\d+',
    'name':'의카',
    'amount': 0
  },
  '싱카': {
    'regex': '싱카\d+',
    'name':'싱카',
    'amount': 0
  },
  '슈카': {
    'regex': '슈카\d+',
    'name':'슈카',
    'amount': 0
  },
  '프': {
    'regex': '프\d+',
    'name':'프로틴',
    'amount': 0
  },
  '메': {
    'regex': '메\d+',
    'name':'메가힐링',
    'amount': 0
  },
  '샤': {
    'regex': '샤\d+',
    'name':'샤워기',
    'amount': 0
  },
  '수': {
    'regex': '수\d+',
    'name':'수전',
    'amount': 0
  },
  '간': {
    'regex': '간\d+',
    'name':'간장',
    'amount': 0
  },
  '된': {
    'regex': '된\d+',
    'name':'된장',
    'amount': 0
  },
  '샴': {
    'regex': '샴\d+',
    'name':'샴푸',
    'amount': 0
  },
  '세': {
    'regex': '세\d+',
    'name':'세탁',
    'amount': 0
  },
  '2종': {
    'regex': '2종\d+',
    'name':'2종',
    'amount': 0
  },
  '4종': {
    'regex': '4종\d+',
    'name':'4종',
    'amount': 0
  },
  '크': {
    'regex': '크\d+',
    'name':'크림',
    'amount': 0
  },
  '세럼': {
    'regex': '세럼\d+',
    'name':'세럼',
    'amount': 0
  },
  '미': {
    'regex': '미\d+',
    'name':'미스트',
    'amount': 0
  },
  '카': {
    'regex': '^카\d+|[^가-힣]카\d+',
    'name':'카밍젤',
    'amount': 0
  },
  '클': {
    'regex': '클\d+',
    'name':'클렌징',
    'amount': 0
  },
  '선': {
    'regex': '선\d+',
    'name':'선크림',
    'amount': 0
  },
  '접지': {
    'regex': '접지\d+',
    'name':'코스메틱접지',
    'amount': 0
  },
  '카달로그': {
    'regex': '카달\d+',
    'name':'코스메틱카달로그',
    'amount': 0
  }
}

def get_products():
  products = []
  target = df.loc[df['날짜'] == '2022-05-09', ['물품명']]
  
  for i in target.index:
    product_name = target['물품명'][i]
    split_list = product_name.split(',')

    products += split_list
  
  return products
  
def update_amount(key, product):
  regex = result[key]['regex']
  is_included = search(regex, product)
  
  if is_included:
    word = is_included.group()
    amount = int(search(r'\d+', word).group())
    
    result[key]['amount'] += amount
    
def init():
  keys = list(result.keys())
  
  for product in get_products():
    for key in keys:
      update_amount(key, product)

init()

# code check
keys = list(result.keys())

for key in keys:
  print(f'{result[key]}')

