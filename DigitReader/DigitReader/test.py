# test

import random
import numpy as np
from sklearn.decomposition import PCA

reducer = PCA(n_components=10)

data = [float(random.randint(1, 30)) for i in range(20)]
print(data)
data = reducer.fit_transform(np.array(data))
print(data)

