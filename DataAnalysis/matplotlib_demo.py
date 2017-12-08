# encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt

def test_1():
    # 定义x轴 从负pi到pi 256个点 包含最后一个点
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    # 定义余弦函数和正弦函数
    c, s = np.cos(x), np.sin(x)
    # 绘图
    plt.figure(1)
    plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-", label="cos", alpha=0.5)  # 自变量 应变量
    plt.plot(x, s, "r*", label="sin")  # 自变量 应变量
    plt.title('COS & SIN')
    plt.show()

if __name__ == '__main__':
    test_1()