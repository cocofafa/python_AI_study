import pandas as pd

test_data = {'이름' : ['상수', '지수', '영우', '연주','우제'],
             '국어' : [85,12,13,51,11],
             '수학' : [22,33,44,55,66],
             '체육' : [22,33,44,55,66] }



df = pd.DataFrame(test_data, index=[2,3,1,4])

df_1 =df.sort_index()

print(df_1)

