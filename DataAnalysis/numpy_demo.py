# encoding=utf-8

import numpy as np
from numpy.linalg import *

def main():
    lst = [[1,2,3], [4,5,6]]
    print type(lst) # <type 'list'>
    np_lst = np.array(lst)
    print type(np_lst)  # <type 'numpy.ndarray'>
    # 指定数据类型
    np_lst = np.array(lst, dtype=np.float)
    print np_lst.shape  # (2L, 3L)  两行3列
    print np_lst.ndim   # 维度
    print np_lst.dtype   # 数据类型
    print np_lst.itemsize   # 每个元素占的字节数
    print np_lst.size   # 元素的个数
    print np_lst.itemsize * np_lst.size # 整个np_lst所占的字节数

# numpy中常用的数组
def arrs():
    print np.zeros([2,4])   # 定义两行4列的数组 用0来初始化
    print np.ones([3,5]) # 定义两行4列的数组 用1来初始化
    print 'Rand:'
    print np.random.rand(2,3)   # 生成两行三列的随机数数组
    print np.random.rand()
    print 'RandInt:'
    print np.random.randint(1, 10, 3)   # 生成3个1-10之间的整数
    print 'Randn:'
    print np.random.randn(2, 4) # 生成2行4列标准正态分布的随机数
    print 'Choice:'
    print np.random.choice([10,20,30,40,50])    # 从指定列表中随机选取一个数
    print 'Distribute:'
    print np.random.beta(1, 10, 100)    # 生成100个1-10的beta分布

# numpy 数组操作
def arrOpts():
    lst = np.arange(1, 11)  # 生成1-10的numpy.ndarray类型数组
    np_lst = lst.reshape(2, -1)   # 将数组编程两行

    print np.exp(np_lst)
    print np.exp2(np_lst)
    print np.sqrt(np_lst)
    print np.log(np_lst)
    print np.log2(np_lst)
    print np.sin(np_lst)

    lst2 = np.array([
        [[1,2,3], [4,5,6]],
        [[7,8,9], [10,11,12]],
        [[13,14,15], [16,17,18]]
    ])

    print lst2.sum()
    print lst2.sum(axis=0)
    print lst2.sum(axis=1)
    print 'axis=2:'
    print lst2.sum(axis=2)
    print 'max:'
    print lst2.max(axis=2)
    print 'min:'
    print lst2.min(axis=2)

# 矩阵与线性方程组
def matrixOpt():
    print np.eye(3) # 生成3维的单位矩阵
    lst = np.array([[1., 2.],
                    [3., 4.]])
    print '矩阵的逆'
    print inv(lst)
    print '转置矩阵'
    print lst.transpose()
    print '行列式'
    print det(lst)
    print '特征值特征向量'
    print eig(lst) # 返回的元组第一个值是特征值 第二个值是特征向量

    res = np.array([[5.], [7.]])
    print '求解方程组  x + 2y = 5, 3x + 4y = 7'
    print solve(lst, res) # 求解方程组  x + 2y = 5, 3x + 4y = 7 ===>>> x = -3, y = 4

def otherOpt():
    print 'FFT:' # FFT 用于信号处理
    lst = np.array([1,1,1,1,1,1,1,1])
    print np.fft.fft(lst)

if __name__ == '__main__':
    otherOpt()
