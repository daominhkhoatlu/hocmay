# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt
import math
y=1
Y = np.array([[ 	
448.524 + y,
509.248 + y,
535.104 + y,
551.432 + y,
623.418 + y,
625.992 + y,
655.248 + y,
701.377 + y,
748.918 + y,
757.881 + y,
831.004 + y,
855.409 + y,
866.707 + y,
902.545 + y,
952.261 + y,
995.531 + y,
1069.78 + y,
1074.42 + y,
1103.88 + y,
1138.69 + y,
1153.13 + y,
1240.27 + y,
1251.9 + y,
1287.97 + y,
1320.47 + y,
1374.92 + y,
1410.16 + y,
1469.69 + y,
1478.54 + y,
1515.28 + y,
]]).T
# Visualize data
x=15
X=np.array([[30 + x,
32.4138 + x,	
34.8276 + x	,
37.2414 + x	,
39.6552 + x	,
42.069 + x,
44.4828 + x,	
46.8966 + x	,
49.3103 + x	,
51.7241 + x	,
54.1379 + x,
56.5517 + x	,
58.9655 + x	,
61.3793 + x	,
63.7931 + x,
66.2069 + x	,
68.6207 + x	,
71.0345 + x	,
73.4483 + x	,
75.8621 + x,
78.2759 + x	,
80.6897 + x	,
83.1034 + x	,
85.5172 + x	,
87.931 + x	,
90.3448 + x	,
92.7586 + x	,
95.1724 + x	,
97.5862 + x	,
100 + x	,
]]).T

plt.plot(X, Y, 'ro')
plt.axis([ 60, 130,460, 1527])

plt.xlabel('Diện tích ')
plt.ylabel('Giá Đất')
plt.show()
# Building Xbar 
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)

# Calculating weights of the fitting line 
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, Y)
w = np.dot(np.linalg.pinv(A), b)
print('w = ', w)
# Preparing the fitting line 
w_0 = w[0][0]
w_1 = w[1][0]
print(w_0,w_1)
x0 = np.linspace(60,130, 2)
y0 = w_0 + w_1*x0
# Drawing the fitting line 
plt.plot(X.T, Y.T, 'ro')     # data 
plt.plot(x0, y0)               # the fitting line
plt.axis([ 60, 130,460, 1527])
plt.xlabel('Diện tích')
plt.ylabel('Giá đất')
plt.show()
#tinh toan du lieu
x_0=float(input("Nhập diện tích của mảnh đất muốn dự đoán:"))
w_x=math.sqrt(math.pow(w_0,2)+math.pow(w_1,2))
y_0 = w_0 + w_1*x_0+w_x
print("Giá đất của mảnh đất có diện tích %s là:"%(x_0),y_0)