import pandas as pd
from pyecharts.charts import Line
import os
import re
from pyecharts import options as opts
from jieba import analyse
from pyecharts.charts import Bar
import jieba

from collections import Counter
import numpy

# 读取文华主题数据
path = "./讲话思想数据库/文化/"
file_paths = []
datas = pd.DataFrame()
pattern = r"\d{4}-\d{2}-\d{2}"

for root, dor, files in os.walk(path):
    for file in files:
        # print(file)
        text = pd.read_csv(path + file)
        text = text.to_string(index=False)
        # print(text)
        date = re.findall(pattern, text)
        if date:
            new_data = pd.DataFrame({"date": date, "text": text})
            # 转化为时间
            new_data["date"] = pd.to_datetime(new_data["date"])
            datas = pd.concat([datas, new_data], ignore_index=True)
# print(datas)
# 按照年份进行聚合
datas["year"] = datas["date"].dt.year
df_group = datas.groupby("year").agg({"text": "".join})
# print(df_group.index)

with open("./cn_stopwords.txt", "r", encoding="utf-8") as f:
    stopwords = [line.strip() for line in f.readlines()]
punctuation = [
    "■",
    "：",
    "？",
    "...",
    "-",
    "（",
    "）",
    "(",
    ")",
    "[",
    "]",
    "/",
    "<",
    ">",
    ".",
    "..",
    "x",
    " ",
    "\n",
    "\u3000",
    "u3000",
]
for i in range(100):
    i = f"{i}"
    stopwords.append(i)
    i = "0" + i
    stopwords.append(i)
# print(stopwords)

keyword_count_list = []
keywords = ["中国", "社会主义", "文化", "青年", "科技", "全国", "创新", "冬奥会"]
# 先分词
filter_list = []
for text in df_group.values:
    seg = list(jieba.cut(str(text), cut_all=False))
    filter = [
        word
        for word in seg
        if word not in stopwords and word not in punctuation and len(word) != 1
    ]
    # print('filter:',filter)
    word_count = Counter(filter)
    # print(1,word_count)
    keyword_count = []
    count_dict = {}

    for keyword in keywords:
        flag = 0
        if keyword in word_count:
            # count = {keyword: word_count[keyword]}
            count_dict[keyword] = word_count[keyword]
            flag = 1

        if flag == 0:
            count_dict[keyword] = 0
        # count_dict.update(count)
    print(count_dict)
    keyword_count.append(count_dict)
    keyword_count_list.append(keyword_count)
    # print(keyword_count)
print("key:", keyword_count_list)

# filter_list.append(filter)

# print(filter_list)

line = Line()
line.add_xaxis(keywords)
# print(df_group.index)
years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
year = 2013
color_list = [
    "red",
    "blue",
    "green",
    "LightSlateBlue",
    "purple",
    "black",
    "orange",
    "pink",
    "gray",
    "cyan",
]
for i, keyword_list in enumerate(keyword_count_list):
    # print(keyword_list)
    for keyword in keyword_list:
        # print(keyword)
        keyword = [value for key, value in keyword.items()]
        print(keyword)

    line.add_yaxis(
        years[i],
        keyword,
        markpoint_opts=opts.MarkPointOpts(symbol_size=30),
        is_connect_nones=True,
        color=color_list[i],
        linestyle_opts=opts.LineStyleOpts(width=2),
    )


line.set_global_opts(
    title_opts=opts.TitleOpts(title="主题词词频", pos_right=400, pos_top=15),
    legend_opts=opts.LegendOpts(
        pos_right=100, pos_top=60, border_color=color_list),
)
line.render("aaa.html")
