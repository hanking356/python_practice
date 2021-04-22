#데이터를 2차원 데이터의 형태인 테이블로 읽어오려면 pandas라이브러리 필요
import pandas as pd
import numpy as np

df = pd.read_csv("../data/2010.csv")
print(df)
