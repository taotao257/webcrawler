import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact

url = "https://raw.githubusercontent.com/GrandmaCan/ML/main/Resgression/Salary_Data.csv"

data = pd.read_csv(url)
# print(data)
# y = w * x + b
#print(data["YearsExperience"]) 
x = data["YearsExperience"]
y = data["Salary"]

def plot_pred(w, b):
    y_pred = x * w + b

    plt.plot(x, y_pred, color = "blue", label = "predict_line")
    plt.scatter(x, y, marker = "x", color = "red", label = "real_data")
    plt.title("Human Resources")
    plt.xlabel("Years")
    plt.ylabel("Salary(thousands)")
    plt.xlim([0, 12])
    plt.ylim([-60, 140])
    plt.legend()

    plt.show()
#plot_pred(0,0)

interact(plot_pred, w = (-100, 100, 1), b = (-100, 100, 1))










