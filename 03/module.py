import torch
from torch import nn

class MyModule(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, tensor):
        conv = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=5, stride=8)
        norm = nn.BatchNorm2d(num_features=256)
        relu = nn.ReLU()
        fc = nn.Linear(in_features=256, out_features=64)

        out1 = conv(tensor)
        out2 = norm(out1)
        out3 = conv(out2)
        out4 = norm(out3)

if __name__ == "__main__":
    tensor = torch.ones(32, 3, 128, 128)
    Model = MyModule()

    out = Model(tensor)
    print("1: ",out.out1.shape)
    print("2: ",out.out2.shape)
    print("3: ",out.out3.shape)
    print("4: ",out.out4.shape)
