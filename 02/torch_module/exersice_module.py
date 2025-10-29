import torch
from torch import nn

class MyModule(nn.Module):
    def __init__(self, mytensor: torch.Tensor, elem_add, elem_multiply):
        super().__init__()
        self.mytensor = mytensor
        self.elem_add = elem_add
        self.elem_multiply = elem_multiply

    def forward(self, x):
        problem2_out = x + self.mytensor
        problem3_out = problem2_out + self.elem_add
        problem4_out = problem3_out * self.elem_multiply
        return problem2_out,problem3_out,problem4_out

if __name__ == "__main__":
    tensor = MyModule(torch.ones((3,3)), 4, 6)
    p2out, p3out, p4out = tensor(torch.full((3,3), 2))

    print(repr(p2out))
    print(repr(p3out))
    print(repr(p4out))