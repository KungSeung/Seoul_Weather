import requests
import json
import pandas as pd
from pandas import json_normalize

url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
params ={'serviceKey' : 'jPRnhgG9nfGV3YpAG1zMMuqURtlBKlGdZbJ3hCtFuL6CZwcQ+eYHHiJJ1qBD1FAROnRJUu0IHtZowSyVWdPx8A==', 
         'pageNo' : '1', 'numOfRows' : '300', 'dataType' : 'JSON', 
         'dataCd' : 'ASOS', 'dateCd' : 'DAY', 
         'startDt' : '20240101', 'endDt' : '20240922', 'stnIds' : '108' }

response = requests.get(url, params=params)
decoded_content = response.content.decode('utf-8')

# JSON으로 파싱
data = json.loads(decoded_content)

# 'items'의 'item'에 접근
items = data['response']['body']['items']['item']

df = json_normalize(items)
df.to_csv('2024_seoul_weather.csv', index=False)