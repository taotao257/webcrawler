import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact

url = "https://raw.githubusercontent.com/GrandmaCan/ML/main/Resgression/Salary_Data.csv"

data = pd.read_csv(url)
x = data["YearsExperience"]
y = data["Salary"]

w = 10
b = 0
y_pred = w * x + b
cost = (y - y_pred) ** 2
#print(cost) 距離平方
cost.sum() / len(x)

def compute_cost(x, y, w, b):
    y_pred = w * x + b
    cost = (y - y_pred) ** 2
    cost.sum() / len(x)
    return cost

costs = []
for w in range(-100, 100):
    compute_cost(x, y, w, 0)
    costs.append(cost)

plt.scatter(range(-100, 101), costs)
plt.show()



