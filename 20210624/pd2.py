import pandas as pd
#
# with open('html_source.txt',encoding='utf-8')as f:
#     temp = f.read()
#
# splitted = temp.split('<div class="inner_number">')
# splitted.pop(0)
# arr=[]
#
# for split in splitted:
#     arr.append(split.split('</div>')[0])
#
# pd_arr = pd.Series(arr)
#
# print(pd_arr)

# import pandas as pd
# # div_class 'inner number' div로 read split  위의 파일을 읽고 해당 위치에 있는 글 번호를 출력
# f = open("html_source.txt", "r", encoding='utf-8')
# temp = f.read()
# split= temp.split('<a class="article" ')
# split.pop(0)
# print(split)
# list1 = []
# list2 = []
# for i in split:
#     list1.append(i.split('</a>')[0])
# print(list1)
# for i in list1:
#     if '</span>' in i:
#         list2.append(i.split('</span>')[1].strip())
#     else:
#         list2.append(i.split(';">')[1].strip())
# print(list2)
# sr = pd.Series(list2)
# print(sr)

# import pandas as pd
#
# with open('html_source.txt', encoding='utf-8') as f:
#     temp = f.read()
#
# article_div = '<a class="article"'
#
# splitted = temp.split(article_div)
# splitted.pop(0)
# arr=[]
#
# for split in splitted:
#     arr.append(split.split('</a>')[0].split('>')[-1]
#                .replace('\n','')
#                .replace('\t','')
#                .replace(' ','')
#                .strip())


# pd_arr=pd.Series(arr)
#
# print(pd_arr)

# with open("html_source.txt", "r", encoding='utf-8') as f:
#   temp = f.read()
# article_div= '<a class="article"'
# split = temp.split(article_div)
# split.pop(0)
# arr = []
# for split in split:
#   arr.append(split.split('</a>')[0].split('>')[-1].replace('\n','').replace('\t','').replace(' ','').strip())
#
# pd_arr=pd.Series(arr)
# print(pd_arr)

f= open('../20160624/html_source.txt', 'r', encoding='UTF-8')

source = f.read()
f.close()

splits = source.split('"class="article"')
splits.pop(0)
title_list = []

for split in splits:
    title_list.append(split.split('</a')[0].split('>')[-1]
                      .replace('\n','')
                      .replace('\t','')
                      .strip())

series = pd.Series(title_list)

print(series)

del(title_list[0])

df = pd.DataFrame({'글번호': number_list,
                   '제목': title_list})

df.set_index('글번호', inplace=True)

print(df)

