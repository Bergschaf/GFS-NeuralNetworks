import numpy as np
import os


def load_train_data():
    # check if mnist_train.csv and mnist_test.csv exist
    if not os.path.isfile("mnist_train.csv") or not os.path.isfile("mnist_test.csv"):
        print("mnist_train.csv or mnist_test.csv not found")
        exit(420)
        # os.system("wget https://pjreddie.com/media/files/mnist_train.csv")
        # os.system("wget https://pjreddie.com/media/files/mnist_test.csv")

    train_csv = np.loadtxt("mnist_train.csv", delimiter=",", skiprows=1)
    train_labels = train_csv[:, 0]
    train_data = train_csv[:, 1:]

    #test_csv = np.loadtxt("mnist_test.csv", delimiter=",", skiprows=1)
    #test_labels = test_csv[:, 0]
    #test_data = test_csv[:, 1:]
    #test_data = test_data / 255
    #test_labels = test_labels.astype(int)
    train_data = train_data / 255
    train_labels = train_labels.astype(int)
    return train_data, train_labels


def load_test_data():
    if not os.path.isfile("mnist_train.csv") or not os.path.isfile("mnist_test.csv"):
        print("mnist_train.csv or mnist_test.csv not found")
        exit(420)
        # os.system("wget https://pjreddie.com/media/files/mnist_train.csv")
        # os.system("wget https://pjreddie.com/media/files/mnist_test.csv")

    # train_csv = np.loadtxt("mnist_train.csv", delimiter=",", skiprows=1)
    # train_labels = train_csv[:, 0]
    # train_data = train_csv[:, 1:]

    test_csv = np.loadtxt("mnist_test.csv", delimiter=",", skiprows=1)
    test_labels = test_csv[:, 0]
    test_data = test_csv[:, 1:]
    test_data = test_data / 255
    test_labels = test_labels.astype(int)
    return test_data, test_labels

if __name__ == '__main__':
    arr1 = np.array([[13,3,2],[3,3,2]])
    print(arr1.T)