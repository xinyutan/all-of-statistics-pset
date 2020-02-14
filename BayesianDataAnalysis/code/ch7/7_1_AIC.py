import torch

# data
x = torch.tensor([[-0.86, -0.30, -0.05, 0.73]])  # Dose x (log g/ml)
n = torch.tensor([[5, 5, 5, 5]], dtype=torch.float)  # Number of animals
y = torch.tensor([[0, 1, 3, 5]], dtype=torch.float)  # Number of deaths

x_ = torch.cat((torch.ones_like(x), x), dim=0)

# alpha, beta
param = torch.tensor([[4.0, 5.0]], requires_grad=True)


def NLL(param, x_, n, y):
    """the negative log likelihood"""
    nlogp = n * torch.log(1.0 + torch.exp(-torch.matmul(param, x_))) + torch.matmul(param, x_) * (n - y)
    return torch.sum(nlogp)


optim_steps = 5000
optimizer = torch.optim.SGD([param], 1e-2)

for ii in range(optim_steps):
    optimizer.zero_grad()
    loss = NLL(param, x_, n, y)
    if ii % 500 == 0:
        print('Step # {}, loss: {}'.format(ii, loss.item()))
    loss.backward()
    optimizer.step()

print("MLE result: alpha = {}, beta = {}".format(param[0][0], param[0][1]))
