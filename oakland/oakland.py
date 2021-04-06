import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
import seaborn as sns


# %matplotlib inline

def draw(data, cl, xlabel):
    num = 7
    data = data.values
    counter = Counter(data[:, cl])
    frequency = counter.most_common()  # 取前n项
    num_list = []
    name_list = []
    for i in range(num):
        num_list.append(int(frequency[i][1]))
        name_list.append(str(frequency[i][0]))
    fig, ax = plt.subplots()
    b = ax.bar(name_list, num_list)
    plt.bar(range(len(num_list)), num_list, color='blue', tick_label=name_list)
    for a, b in zip(name_list, num_list):
        ax.text(a, b + 1, b, ha='center', va='bottom')
    plt.title('补全前')
    plt.xlabel(xlabel)
    plt.ylabel('频数')
    plt.show()


# 数据摘要
def abstract(path):
    data = pd.read_csv(path, header=0, index_col=0, engine='python', encoding='utf-8')
    print(data.describe())  # 五数概括、有效个数、平均值等
    data = data.values
    for i in range(data.shape[1]):  # 对所有列进行频数的统计
        counter = Counter(data[:, i])
        print(counter.most_common(5))  # 取前n项


# 数据可视化
def visual(path):
    data = pd.read_csv(path, header=0, index_col=0, engine='python', encoding='utf-8')

    # 绘制盒图
    data['points'].plot.box(title="数据可视化")
    plt.grid(linestyle="--")
    plt.show()
    data['price'].plot.box(title="数据可视化")
    plt.grid(linestyle="--")
    plt.show()

    # 绘制直方图
    plt.hist(x=data['points'], bins=10, edgecolor='black')
    plt.xlabel('points')
    plt.ylabel('频数')
    plt.title('直方图')
    plt.show()
    # plt.hist(x=data['price'], bins=10, edgecolor='black')
    # plt.xlabel('price')
    # plt.ylabel('频数')
    # plt.title('直方图')
    # plt.show()

    # plt.hist(x=data['country'], bins=10, edgecolor='black')
    # plt.xlabel('country')
    # plt.ylabel('频数')
    # plt.title('直方图')
    # plt.show()


# 将缺失部分剔除
def na_drop(path):
    data = pd.read_csv(path, header=0, index_col=0, engine='python', encoding='utf-8')
    drop = data.dropna()  # 将缺失值所在行剔除
    print(drop.shape[0])
    draw(drop)

    return drop


# 用最高频率值来填补缺失值
def na_max(path):
    data = pd.read_csv(path, header=0, index_col=0, engine='python', encoding='utf-8')
    data = data.values
    max_time = []  # 每个属性最大频数的值
    # 确定每个属性最大频数的值
    for cl in range(data.shape[1]):
        counter = Counter(data[:, cl])
        counter = counter.most_common()  # 排序，返回类型为list，list的每个元素为内容和频数
        if counter[0][0] == counter[0][0]:  # 如果最大频数不为空值
            max_time.append(counter[0][0])
            # print(str(counter[0][0])+'非空')
        else:  # 如果最大频数为空值
            max_time.append(counter[1][0])
            # print(str(counter[1][0]) + '空')
        # print(list(counter.keys())[0])

    # 对每个属性的空值进行替换
    data_max = pd.DataFrame(data)
    for cl in range(data.shape[1]):
        data_max[cl] = data_max[cl].fillna(max_time[cl])
        # print(max_time[cl])

    plt.hist(x=data_max[3], bins=10, edgecolor='black')
    plt.xlabel('points')
    plt.ylabel('频数')
    plt.title('直方图')
    plt.show()
    return data_max


path = 'C:/Users/xue/Desktop/课程_研一下/数据挖掘/课后作业/4/oakland-crime-statistics-2011-to-2016/records-for-2016.csv'
# abstract(path)   # 数据摘要
# visual(path)  # 数据可视化
# na_drop(path)  # 将缺失部分剔除
# na_max(path)  # 用最高频率值来填补缺失值

data = pd.read_csv(path, header=0, engine='python', encoding='utf-8')
draw(data, 3, 'Area Id')
draw(data, 4, 'Beat')

print('Over')
