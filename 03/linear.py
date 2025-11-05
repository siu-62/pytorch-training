import torch
from torch import nn

if __name__ == "__main__":
    tensor = torch.ones((32, 1024))
    print("1: ", tensor.shape)

    fc = nn.Linear(in_features=1024, out_features=256)
    out2 = fc(tensor)
    print("2: ", out2.shape)

    fc = nn.Linear(in_features=1024, out_features=2048)
    out3 = fc(tensor)
    print("3: ", out3.shape)

    out4 = out2.reshape(32, 16, 16)
    print("4: ",out4.shape)