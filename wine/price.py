# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
fig, ax = plt.subplots()
# 补全前
num_list = [7860, 7056, 5988, 5955, 5449, 5255, 4950, 4479, 4273, 4194]
name_list = ['20.0', '15.0', '18.0', '25.0', '30.0', '10.0', '12.0', '13.0', '16.0', '35.0']
b = ax.bar(name_list, num_list)
plt.bar(range(len(num_list)), num_list, color='blue', tick_label=name_list)
for a, b in zip(name_list, num_list):
    ax.text(a, b + 1, b, ha='center', va='bottom')
plt.title('补全前')
plt.xlabel('price')
plt.ylabel('频数')
plt.show()
