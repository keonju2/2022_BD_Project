import pandas as pd
import os


path="./kakao"
file_list = os.listdir(path)
total_data=pd.DataFrame()
for filename in file_list:
    data = pd.read_excel(path+'/'+filename,header=0)
    data = pd.DataFrame(data)
    total_data = total_data.append(data)


print(total_data.shape)
print(total_data.columns)
pd.to_csv('카카오_뉴스_목록.csv')