import numpy as np
import torch

data = np.array([
[[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
[[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
[[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]
])

print("problem1:")
tensor = torch.from_numpy(data)
print(tensor.shape)

print("problem2:")
tensor_new = torch.permute(tensor,(2,0,1))
print(tensor_new)
print(tensor_new.shape)

print("problem3:")
tensor_sum = tensor_new.sum(dim=0)
print(tensor_sum)
print(tensor_sum.shape)

print("problem4:")
tensor_ave = torch.tensor_ave.float()