import cv2
import numpy as np

digits = cv2.imread("../images/digits.png", cv2.IMREAD_GRAYSCALE)
test_digits = cv2.imread("../images/test_digits.png", cv2.IMREAD_GRAYSCALE)

rows = np.vsplit(digits, 50)
cells = []
for row in rows:
    row_cells = np.hsplit(row, 50)
    for cell in row_cells:
        cell = cell.flatten()
        cells.append(cell)
cells = np.array(cells, dtype=np.float32)

k = np.arange(10)
cells_labels = np.repeat(k, 250)


test_digits = np.vsplit(test_digits, 50)
test_cells = []
for d in test_digits:
    d = d.flatten()
    test_cells.append(d)
test_cells = np.array(test_cells, dtype=np.float32)


# KNN
knn = cv2.ml.KNearest_create()
knn.train(cells, cv2.ml.ROW_SAMPLE, cells_labels)
ret, result, neighbors, dist = knn.findNearest(test_cells, k=7)

k = np.arange(10)
test_labels = np.repeat(k, 5)
print("Test labels are: ", test_labels)

pre_result = np.int32(result.ravel())
print("Predicted labels are: ", pre_result)
correct = 0
for i, j in zip(pre_result, test_labels):
    if i == j:
        correct += 1
print("The test accuracy is: ", correct*100/50)
