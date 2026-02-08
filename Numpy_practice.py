import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Original Array:\n", arr)

normalized = arr / np.max(arr)
print("Normalized Array:\n", normalized)

row_mean = np.mean(arr, axis=1)
print("Row-wise Mean:", row_mean)
