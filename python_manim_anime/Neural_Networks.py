import numpy as np

def sigmoid(x):
    #  激活函数
    return 1/(1+np.exp(-x))

def mse_loss(y_true,y_pred):
    #  损失函数
    return np.mean(((y_true - y_pred)**2))

class Neuron:
    def __init__(self,weights,bias):
        self.weights = weights
        self.bias = bias
        
    def feedforward(self,inputs):
        #层与层之间通过加权求和的方式输出到下一层
        output = np.dot(self.weights,inputs)+self.bias
        return sigmoid(output)
    
class NeuralNetwork:
     
    def __init__(self):
        weights =  np.array([0,1])
        bias = 0
        
        self.h1 = Neuron(weights,bias)
        self.h2 = Neuron(weights,bias)
        self.o1 = Neuron(weights,bias)
    
    def feedout(self,x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)
        
        out_o1 = self.o1.feedforward(np.array([out_h1,out_h2]))
        
        return out_o1

x = np.array([2,3])
y_true = np.array([1,0,0,1])
y_pred = np.array([0,0,0,0])
network = NeuralNetwork()
y = network.feedout(x)
y_loss = mse_loss(y_true,y_pred)
print(y,y_loss)
