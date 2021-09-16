import numpy as np

mask_size_y = 8
mask_size_x = 10

arr = np.ones((mask_size_y, mask_size_x))
np.savetxt('./mask.csv', arr,delimiter=",")
