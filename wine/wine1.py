import pandas as pd
import numpy as np
from fancyimpute import KNN, SoftImpute, IterativeImputer, BiScaler
from collections import Counter
import matplotlib.pyplot as plt

# from sklearn.preprocessing import Imputer

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
import seaborn as sns


# %matplotlib inline

def draw(data, cl):
    num = 10
    wine_data = data.values
    counter = Counter(wine_data[:, cl])
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
    plt.xlabel('price')
    plt.ylabel('频数')
    plt.show()


# 数据摘要
def abstract(path):
    wine_data = pd.read_csv(path, header=0, index_col=0, engine='python', encoding='utf-8')
    print(wine_data.describe())  # 五数概括、有效个数、平均值等
    wine_data = wine_data.values
    for i in range(wine_data.shape[1]):  # 对所有列进行频数的统计
        counter = Counter(wine_data[:, i])
        print(counter.most_common(5))  # 取前n项


# 数据可视化
def visual(path):
    wine_data = pd.read_csv(path, header=0, index_col=0, engine='python', encoding='utf-8')

    # 绘制盒图
    wine_data['points'].plot.box(title="数据可视化")
    plt.grid(linestyle="--")
    plt.show()
    wine_data['price'].plot.box(title="数据可视化")
    plt.grid(linestyle="--")
    plt.show()

    # 绘制直方图
    plt.hist(x=wine_data['points'], bins=10, edgecolor='black')
    plt.xlabel('points')
    plt.ylabel('频数')
    plt.title('直方图')
    plt.show()
    # plt.hist(x=wine_data['price'], bins=10, edgecolor='black')
    # plt.xlabel('price')
    # plt.ylabel('频数')
    # plt.title('直方图')
    # plt.show()

    # plt.hist(x=wine_data['country'], bins=10, edgecolor='black')
    # plt.xlabel('country')
    # plt.ylabel('频数')
    # plt.title('直方图')
    # plt.show()


# 将缺失部分剔除
def na_drop(path):
    wine_data = pd.read_csv(path, header=0, index_col=0, engine='python', encoding='utf-8')
    wine_drop = wine_data.dropna()  # 将缺失值所在行剔除
    print(wine_drop.shape[0])
    draw(wine_drop)

    return wine_drop


# 用最高频率值来填补缺失值
def na_max(path):
    wine_data = pd.read_csv(path, header=0, index_col=0, engine='python', encoding='utf-8')
    wine_data = wine_data.values
    max_time = []  # 每个属性最大频数的值
    # 确定每个属性最大频数的值
    for cl in range(wine_data.shape[1]):
        counter = Counter(wine_data[:, cl])
        counter = counter.most_common()  # 排序，返回类型为list，list的每个元素为内容和频数
        if counter[0][0] == counter[0][0]:  # 如果最大频数不为空值
            max_time.append(counter[0][0])
            # print(str(counter[0][0])+'非空')
        else:  # 如果最大频数为空值
            max_time.append(counter[1][0])
            # print(str(counter[1][0]) + '空')
        # print(list(counter.keys())[0])

    # 对每个属性的空值进行替换
    wine_max = pd.DataFrame(wine_data)
    for cl in range(wine_data.shape[1]):
        wine_max[cl] = wine_max[cl].fillna(max_time[cl])
        # print(max_time[cl])

    plt.hist(x=wine_max[3], bins=10, edgecolor='black')
    plt.xlabel('points')
    plt.ylabel('频数')
    plt.title('直方图')
    plt.show()
    return wine_max


# 通过属性的相关关系来填补缺失值
def att_rel(path):
    wine_data = pd.read_csv(path, header=0, index_col=0, engine='python', encoding='utf-8')
    wine_data = wine_data.values
    im = Imputer(missing_values='NaN', strategy='mean', axis=0)
    att_data = im.fit_transform(wine_data[:, 4].reshape(-1, 1))
    draw(pd.DataFrame(att_data), 0)


# 通过数据对象之间的相似性来填补缺失值
def obj_sim(path):
    wine_data = pd.read_csv(path, header=0, index_col=0, engine='python', encoding='utf-8')
    wine_data = wine_data.values
    # t = BiScaler().fit_transform(wine_data[:, 4].reshape(-1, 1))
    # obj_data = SoftImpute().fit_transform(t)
    obj_data = IterativeImputer().fit_transform(wine_data[:, 4].reshape(-1, 1))
    draw(pd.DataFrame(obj_data), 0)


path = 'C:/Users/xue/Desktop/课程_研一下/数据挖掘/课后作业/4/wine-reviews/winemag-data_first150k.csv'
# abstract(path)   # 数据摘要
# visual(path)  # 数据可视化
# wine_drop = na_drop(path)  # 将缺失部分剔除
# wine_max = na_max(path)  # 用最高频率值来填补缺失值
# att_rel(path)
obj_sim(path)
print('Over')
