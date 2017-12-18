import numpy as np
a1 = np.array([[0, 2, 3],
               [2, 3, 0]])
a = np.mat([[0, 2, 3],
            [2, 3, 0]])
print(np.nonzero(a))
print(np.nonzero(a1))