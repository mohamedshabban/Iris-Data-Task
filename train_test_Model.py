'''2,3,1,3'''
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from tkinter import messagebox

Modified_Data = None
training_set = None
testing_set = None
weights = None
np_weights = None


def testing(x1, x2, cl1, cl2):
    (d1, d2) = (float(x1), float(x2))
    Arr = [d1, d2]
    output = predict(Arr)
    if output == 0:
        messagebox.showinfo("Output", cl1)
    else:
        messagebox.showinfo("Output", cl2)

def net_input(X):
    return np.dot(X, np_weights[1:]) + np_weights[0]

'predict by np array'
def Boundary_predict(X):
    return np.where(net_input(X) >= 0.0, 1, 0)

'predict by normal array'
def predict(X):
    out = float((X[0] * weights[1]) + (X[1] * weights[2]) + weights[0])
    if out >= 0.0:
        out = 1
    else:
        out = 0
    return out


def split_data(data, f1, f2, c1, c2):
    global Modified_Data, training_set, testing_set
    Modified_Data = pd.DataFrame.copy(data)
    training_set = []
    testing_set = []

    outputs = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
    features = ["X1", "X2", "X3", "X4"]
    for i in outputs:
        if i != c1 and i != c2:
            Modified_Data = Modified_Data[Modified_Data.Class != i]
    for i in features:
        if i != f1 and i != f2:
            Modified_Data.drop([i], axis=1, inplace=True)
    (s1, s2) = (None, None)
    try:
        s1 = Modified_Data.loc[0,:]
        s1 = 0
        try:
            s2 = Modified_Data.loc[50,:]
            s2 = 50
        except:
            s2 = 100
    except:
        s1 = 50
        s2 = 100

    train1 = random.sample(range(s1, s1 + 50), 30)
    train2 = random.sample(range(s2, s2 + 50), 30)
    for i in range(30):
        training_set.append(train1[i])
    for i in range(30):
        training_set.append(train2[i])

    for i in range(s1, s1 + 50):
        if i not in train1 and i not in train2:
            testing_set.append(i)
    for i in range(s2, s2 + 50):
        if i not in train1 and i not in train2:
            testing_set.append(i)


def fit_data(f1, f2, c1, c2, eta, epochs, bias):
    mp = dict()
    mp[c1] = 0
    mp[c2] = 1
    global weights, np_weights
    weights = []
    random_generator = np.random.RandomState(1)
    np_weights = random_generator.normal(loc=0.0, scale=0.001, size=3)
    if int(bias) == 0:
        np_weights[0] = 0.0
    for i in np_weights:
        weights.append(float(i))
    for i in range(int(epochs)):
        for j in training_set:
            x1 = float(Modified_Data.loc[j, f1])
            x2 = float(Modified_Data.loc[j, f2])
            x_in = [x1, x2]
            actual_output = float(mp[Modified_Data.loc[j, 'Class']])
            predicted_output = float(predict(x_in))

            'update weights as normal array for testing'
            upd = float(float(eta) * (actual_output - predicted_output))
            weights[0] = float(weights[0] + upd)
            weights[1] = float(weights[1] + (upd * x_in[0]))
            weights[2] = float(weights[2] + (upd * x_in[1]))

            'updata weights as np array for boundary line'
            np_weights[0] = float(np_weights[0] + upd)
            np_weights[1] = float(np_weights[1] + (upd * x_in[0]))
            np_weights[2] = float(np_weights[2] + (upd * x_in[1]))


def test_data(f1, f2, c1, c2):
    mp = dict()
    mp[c1] = 0
    mp[c2] = 1

    expected = []
    predicted = []
    accuracy = 0
    for i in testing_set:
        x1 = float(Modified_Data.loc[i, f1])
        x2 = float(Modified_Data.loc[i, f2])
        x_in = [x1, x2]
        output = Modified_Data.loc[i, 'Class']
        expected.append(output)
        actual_output = float(mp[Modified_Data.loc[i, 'Class']])
        predicted_output = float(predict(x_in))
        if predicted_output == 0:
            predicted.append(c1)
        else:
            predicted.append(c2)
        if actual_output == predicted_output:
            accuracy = accuracy + 1

    print("Accuracy = " + str(float(accuracy / 40) * 100) + "%")
    print("confusion matrix :")
    class1 = 20
    class2 = 20
    for i in range(40):
        if i < 20:
            if expected[0] != predicted[i]:
                class1 -= 1
        else:
            if expected[20] != predicted[i]:
                class2 -= 1

    print ("   c1", "   c2" )
    print("c1  " + str(class1) + "   " + str(20-class1))
    print("c2  " + str(20 - class2) + "   " + str(class2))

    Boundary_line(c1)


def Boundary_line(c1):
    X = Modified_Data.iloc[0:100, [0, 1]].values
    y = Modified_Data.iloc[0:100, 2].values
    y = np.where(y == c1, 0, 1)
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, 0.02),
                           np.arange(x2_min, x2_max, 0.02))
    z = Boundary_predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=[cmap(idx)],
                    marker=markers[idx], label=cl)
    plt.xlabel('sepal length [cm]')
    plt.ylabel('petal length [cm]')
    plt.legend(loc='upper left')
    plt.show()
