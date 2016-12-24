﻿import numpy as np

num_points = 1000
vector_set=[]

for i in range(num_points):
    x1 = np.random.normal(0.0,0.55)
    y1 = x1*0.1 + 0.3 + np.random.normal(0.0,0.03)
    vector_set.append([x1,y1])

x_data = [v[0] for v in vector_set] # x축 Data
y_data = [v[1] for v in vector_set] # y축 Data

import matplotlib.pyplot as plt

#그래프 표시
plt.plot(x_data, y_data, 'ro')
plt.legend()
plt.show()  # hold된다.

import tensorflow as tf

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b  # W 와 b를 구할것이다.

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()


#실행을 위한 객체 생성
sess = tf.Session()
sess.run(init)

for step in range(8):
    sess.run(train)
    print(step, sess.run(W), sess.run(b))
    print(step, sess.run(loss))


#deep learning 그래픽 표시
plt.plot(x_data, y_data, 'ro')
plt.plot(x_data, sess.run(W)*x_data + sess.run(b))
plt.xlabel('x')
plt.xlim(-2,2)
plt.ylim(0.1, 0.6)
plt.ylabel('y')
plt.legend()
plt.show()
