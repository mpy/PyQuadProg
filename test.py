import numpy as np
from PyQuadProg import PyQuadProg


G = np.array([[11., 0], [0, 12]])
CE = np.array([[1.], [1]])
CI = np.array([[1.], [1]])

g0 = np.array([10., 20])
ce0 = np.array([-5.])
ci0 = np.array([10])
x = np.array([2., 2])


qp = PyQuadProg(G, g0, CE, ce0, CI, ci0)

print qp.x

