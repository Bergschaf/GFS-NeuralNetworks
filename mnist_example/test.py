from network import *
from PIL import Image


def generate_PNG(data, label, filename):
    image = Image.fromarray(data.reshape(28, 28) * 255).convert("RGB")
    image.save(f"{filename}_{label}.png")


if __name__ == '__main__':
    weights = load("weights.npy")
    train_data, train_labels = load_test_data()
    print(get_network_error(train_data, train_labels, weights))
    for i in range(10):
        generate_PNG(train_data[i], train_labels[i], f"test{i}")
        print(get_prediction(train_data[i], weights), train_labels[i])
