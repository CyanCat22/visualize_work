import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = r"D:\work\zufe\Visualize\第一次作业\used_cars.csv"
df = pd.read_csv(path)
df = df.set_index('brand')
# brands = df['brand']
# brand = list(set(brands))
# 总共六种品牌
# 选取的列为year, price,miles, brand
Hondas = df.loc['Honda']
Subarus = df.loc['Subaru']
Hyundais = df.loc['Hyundai']
Chevrolets = df.loc['Chevrolet']
Fords = df.loc['Ford']
Volkswagens = df.loc['Volkswagen']

fig, ax = plt.subplots()
Honda = ax.scatter(x=Hondas['price'], y=Hondas['year'], c='lightcoral', label = Hondas,  alpha=0.5, s=Hondas['miles']*0.01)
Ford = ax.scatter(x=Fords['price'], y=Fords['year'], c='y', label = Fords,  alpha=0.5, s=Fords['miles']*0.01)
Subaru = ax.scatter(x=Subarus['price'], y=Subarus['year'], c='gray', label = Subarus,  alpha=0.5, s=Subarus['miles']*0.01)
Hyundai = ax.scatter(x=Hyundais['price'], y=Hyundais['year'], c='red', label = Hyundais,  alpha=0.5, s=Hyundais['miles']*0.01)
Volkswagen = ax.scatter(x=Volkswagens['price'], y=Volkswagens['year'], c='aquamarine', label = Volkswagens,  alpha=0.5, s=Volkswagens['miles']*0.01)
Chevrolet = ax.scatter(x=Chevrolets['price'], y=Chevrolets['year'], c='royalblue', label = Chevrolets,  alpha=0.5, s=Chevrolets['miles']*0.01)

ax.set_xlabel('price', fontsize=15)
ax.set_ylabel('year', fontsize=15)
ax.set_title("userd_cars", fontsize = 15)

legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label='Hondas', markerfacecolor='lightcoral', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='Fords', markerfacecolor='y', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='Subarus', markerfacecolor='gray', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='Hyundais', markerfacecolor='red', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='Volkswagens', markerfacecolor='aquamarine', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='Chevrolets', markerfacecolor='royalblue', markersize=10)]
ax.legend(handles=legend_elements, loc='lower right', fontsize=10)

ax.grid(True)  # 加上网格线
fig.tight_layout() # 优化布局，自动调整尺寸和间距
plt.show()