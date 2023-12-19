import jieba
import pandas as pd
from pyecharts.charts import WordCloud
from pyecharts import options as opts
from collections import Counter
import operator
from functools import reduce
from pyecharts.globals import SymbolType
import os
from concurrent.futures import ThreadPoolExecutor


def process_data(file_path):
    try:
        data = pd.read_csv(file_path)
        data = f'{data}'
        return data
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return ""


path = "./讲话思想数据库/"
file_paths = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".txt"):
            file_paths.append(os.path.join(root, file))
            # print(file_paths)
            # ./讲话思想数据库/党建/1.txt
# data_list = []

with ThreadPoolExecutor(max_workers=10) as executor:
    data_list = list(executor.map(process_data, file_paths))
data_list = reduce(operator.add, data_list)

# 停用词
with open("./cn_stopwords.txt", "r", encoding="utf-8") as f:
    stopwords = [line.strip() for line in f.readlines()]
punctuation = [
    "■",
    "：",
    "？",
    '...',
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
    ' ',
    '\n',
    '\u3000',
]
for i in range(100):
    i = f"{i}"
    stopwords.append(i)
    i = "0" + i
    stopwords.append(i)
# print(stopwords)

# 先分词
seg_list = list(jieba.cut(data_list, cut_all=False))
# 删除词的长度为1的词
# 删除停用词
filter_list = [
    word for word in seg_list if word not in stopwords and word not in punctuation and len(word) != 1
]
# print(' '.join(filter_list))

# 统计词频
# ds = pd.Series(filter_list).value_counts()
word_counts = Counter(filter_list)
print(word_counts)
# print(ds[:20])

# 生成词云
# 使用pyecharts绘制词云

c = (
    WordCloud(init_opts=opts.InitOpts(width="1500px", height="1500px"))
    .add(
        "",
        data_pair=[(word, count) for word, count in word_counts.items()],
        word_size_range=[20, 150],
        textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="WordCloud", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("wordcloud.html")
)
