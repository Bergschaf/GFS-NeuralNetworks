import numpy as np
from data import *

Weights = [np.random.rand(784, 16) - 0.5, np.random.rand(16, 16) - 0.5, np.random.rand(16, 10) - 0.5]


def _positive_sigmoid(x):
    return 1 / (1 + np.exp(-x))


def _negative_sigmoid(x):
    # Cache exp so you won't have to calculate it twice
    exp = np.exp(x)
    return exp / (exp + 1)


def sigmoid(x):
    positive = x >= 0
    # Boolean array inversion is faster than another comparison
    negative = ~positive

    # empty contains junk hence will be faster to allocate
    # Zeros has to zero-out the array after allocation, no need for that
    # See comment to the answer when it comes to dtype
    result = np.empty_like(x, dtype=float)
    result[positive] = _positive_sigmoid(x[positive])
    result[negative] = _negative_sigmoid(x[negative])

    return result


def sigmoid_derivative(x):
    return sigmoid(x) * (1.0 - sigmoid(x))


activation_function = sigmoid
activation_function_derivative = sigmoid_derivative
learning_rate = -0.5


def get_output(input, Weights):
    output = input
    Layer_outputs = []
    for weight in Weights:
        output = np.dot(output, weight)
        output = activation_function(output)
        Layer_outputs.append(np.copy(output))
    return output


def get_full_output(input, Weights):
    Layer_outputs = [input]
    Net_outputs = []
    output = input
    for weight in Weights:
        output = np.dot(output, weight)
        Net_outputs.append(np.copy(output))
        output = activation_function(output)
        Layer_outputs.append(np.copy(output))
    return output, Layer_outputs, Net_outputs


def get_prediction(input, Weights):
    output = get_output(input, Weights)
    return np.argmax(output)


def get_loss(input, label: int, Weights):
    label_np = np.zeros(10)
    label_np[label] = 1
    output = get_output(input, Weights)
    return np.sum((output - label_np) ** 2)


def get_network_error(test_data, test_labels, Weights):
    error = 0
    for i in range(len(test_data)):
        error += get_loss(test_data[i], test_labels[i], Weights)
    return error / len(test_data)


def train(epochs, train_data, train_labels, Weights, batch_size=100):
    for epoch in range(epochs):
        batch = np.random.choice(len(train_data), batch_size)
        Avg_Weight_Deltas = [np.zeros(weight.shape) for weight in Weights]

        for b in batch:
            input = train_data[b]
            label = train_labels[b]
            output, Layer_outputs, Net_outputs = get_full_output(input, Weights)
            label_np = np.zeros(10)
            label_np[label] = 1
            error = output - label_np
            Weights_delta = [np.zeros(weight.shape) for weight in Weights]

            # run backprop for the last layer
            x = error * activation_function_derivative(Net_outputs[-1])
            x_t = np.tile(x, (len(Net_outputs[-2]), 1))
            Weights_delta[-1] = x_t * np.tile(Layer_outputs[-2], (len(Layer_outputs[-1]), 1)).T

            for i in range(len(Net_outputs) - 2, -1, -1):
                new_x = np.zeros(len(Net_outputs[i]))
                for j in range(len(x)):
                    new_x[j] = sum(Weights[i + 1][j] * x)
                x = new_x * activation_function_derivative(Net_outputs[i])
                x_t = np.tile(x, (len(Layer_outputs[i]), 1))
                Weights_delta[i] = x_t * np.tile(Layer_outputs[i], (len(Net_outputs[i]), 1)).T

            for i in range(len(Weights)):
                Avg_Weight_Deltas[i] += Weights_delta[i] / batch_size

        for i in range(len(Weights)):
            Weights[i] += Avg_Weight_Deltas[i] * learning_rate
        #print(epoch, get_network_error(train_data[:100], train_labels[:100], Weights))
        print(epoch)
        if epoch % 50 == 0:
            print(get_network_error(train_data[:1000], train_labels[:1000], Weights))
            print(epoch)
            for i in range(10):
                print(get_prediction(train_data[i], Weights), train_labels[i])  #


def save(Weights, filename):
    for  i in range(len(Weights)):
        with open(filename + str(i), 'wb') as f:
            np.save(f, Weights[i])


def load(filename):
    new_weights = []
    for i in range(len(Weights)):
        with open(filename + str(i), 'rb') as f:
            new_weights.append(np.load(f))
    return new_weights



if __name__ == '__main__':
    train_data, train_labels = load_train_data()

    for j in range(100):
        print(get_network_error(train_data, train_labels, Weights))
        print(train(2000, train_data, train_labels, Weights))
        print(get_network_error(train_data, train_labels, Weights))
        for i in range(10):
            print(get_prediction(train_data[i], Weights), train_labels[i])

        save(Weights, f'weights2_{j}.npy')
