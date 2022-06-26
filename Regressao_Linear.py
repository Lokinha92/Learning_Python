import matplotlib.pyplot as plt
import numpy as np



x = [-1., -0.77777778, -0.55555556, -0.33333333, -0.11111111, -0.11111111,
    0.333333333, 0.55555556, 0.77777778, 1.]

y = [-1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49406657, 1.14972239,
    1.64228553, 2.1749824, 2.64773614, 2.95684202]

x = np.array(x).reshape(-1, 1)
y = np.array(y).reshape(-1, 1)

xum = np.hstack((x, np.ones(x.shape))) 

beta = np.linalg.pinv(xum).dot(y)

# PARA Y = aX + b
print('a: ', beta[0][0])
print('b: ', beta[1][0])

plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label = 'Dados originais')
plt.plot(x, xum.dot(beta), label = 'Regressão Linear')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('REGRESSÃO LINEAR - PRÁTICA')
plt.grid()
plt.show()