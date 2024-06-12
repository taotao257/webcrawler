import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

url = "https://raw.githubusercontent.com/GrandmaCan/ML/main/Resgression/Salary_Data.csv"
data = pd.read_csv(url)

x = data["YearsExperience"]
y = data["Salary"]

# 2 * x * (w * x + b - y)   w_gradient
# 2 * (w * x + b - y)       b_gradient
def compute_gradient(x, y, w, b):   
    w_gradient = x * (w * x + b - y).mean()
    b_gradient = (w * x + b - y).mean()
    return w_gradient, b_gradient

def compute_cost(x, y, w, b):
    y_pred = w * x + b
    cost = (y - y_pred) ** 2
    cost.sum() / len(x)
    return cost

w = 0; b = 0
learninig_rate = 0.001

def gradient_descent(x, y, w_init, b_init, learning_rate, cost_function, gradient_function, run_iter, p_iter = 1000):
    
    c_hist = []
    w_hist = []
    b_hist = []

    
    w = w_init
    b = b_init

    for i in range(run_iter):
        w_gradient, b_gradient = gradient_function(x, y, w, b)

        w = w - w_gradient * learninig_rate
        b = b - b_gradient * learninig_rate
        cost = cost_function(x, y, w, b)
        
        w_hist.append(w)
        b_hist.append(b)
        c_hist.append(cost)
        
        if i % p_iter == 0:
            print(f"Iteration {i:5} : Cost {cost: .2e}, w : {w: .2e}, b : {b: .2e}, w_gradient : {w_gradient: .2e}, b_gradient : {b_gradient: .2e}")
        
    return w, b, w_hist, b_hist, c_hist


#plt.plot(np.arrange(0, 20000), c_hist)
#plt.title("iteration vs cost")
#plt.xlabel("iteration")
#plt.ylabel("cost")
#plt.show()








