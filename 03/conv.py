import torch
from torch import nn



if __name__ == "__main__":
    tensor = torch.ones((32, 3, 128, 128))
    print("1: ", tensor.shape)

    conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, padding=1)
    out2 = conv(tensor)
    print("2: ",out2.shape)

    conv = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=3, stride=2, padding=1)
    out3 = conv(tensor)
    print("3: ",out3.shape)

    conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=5, padding=2)
    out2_2 = conv(tensor)
    print("2-2: ",out2_2.shape)
    conv = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=5, stride=2, padding=2)
    out3_2 = conv(tensor)
    print("3-2: ",out3_2.shape)