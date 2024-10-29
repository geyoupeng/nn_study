import numpy as np
from mpmath import sigmoid
class MLP:
    def __init__(self, num_input = 3, num_hidden = [3, 5], num_output = 2):
        self.num_input = num_input
        self.num_hidden = num_hidden
        self.num_output = num_output

        layers = [self.num_input] + self.num_hidden + [self.num_output]

        #initiate random weight
        self.weight = []
        for i in range(len(layers) - 1):
            w = np.random.rand(layers[i], layers[i + 1])
            self.weight.append(w)

        print(self.weight)

    def forward(self, X):

        activations = X
        for i in range(len(self.weight)):
            net_input = np.dot(activations, self.weight[i])

            activations = self._sigmoid(net_input)

        return activations

    def _sigmoid(self, X):
        return 1 / (1 + np.exp(-X))
if __name__ == '__main__':


    mlp = MLP()

    inputs = np.random.rand(mlp.num_input)
    outputs = mlp.forward(inputs)

    print("the inpur is :{}".format(inputs))
    print("the output is :{}".format(outputs))