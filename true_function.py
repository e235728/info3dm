import numpy as np 
import matplotlib.pyplot as plt

def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

x = 0
y = true_function(x)
print(y)

# x の定義域
x = np.linspace(-1, 1, 1000)

y = true_function(x)

# フォント設定
import matplotlib
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

# グラフの描画
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='true_function', color='blue')
plt.title('y = sin(pi * x * 0.8) * 10')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()  # 凡例を表示
plt.grid(True)

# 画像として保存
plt.savefig("ex1.1.png")
plt.close()