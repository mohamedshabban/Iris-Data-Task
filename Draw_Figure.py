import matplotlib.pyplot as plt

def Draw_Iris_Dataset(data):
    X1 = data['X1']
    X2 = data['X2']
    X3 = data['X3']
    X4 = data['X4']

    plt.figure('X1, X2')
    plt.scatter(X1[0:50], X2[0:50])
    plt.scatter(X1[50:100], X2[50:100])
    plt.scatter(X1[100:150], X2[100:150])
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.show()

    plt.figure('X1, X3')
    plt.scatter(X1[0:50], X3[0:50])
    plt.scatter(X1[50:100], X3[50:100])
    plt.scatter(X1[100:150], X3[100:150])
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.show()

    plt.figure('X1, X4')
    plt.scatter(X1[0:50], X4[0:50])
    plt.scatter(X1[50:100], X4[50:100])
    plt.scatter(X1[100:150], X4[100:150])
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.show()

    plt.figure('X2, X3')
    plt.scatter(X2[0:50], X3[0:50])
    plt.scatter(X2[50:100], X3[50:100])
    plt.scatter(X2[100:150], X3[100:150])
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.show()

    plt.figure('X2, X4')
    plt.scatter(X2[0:50], X4[0:50])
    plt.scatter(X2[50:100], X4[50:100])
    plt.scatter(X2[100:150], X4[100:150])
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.show()

    plt.figure('X3, X4')
    plt.scatter(X3[0:50], X4[0:50])
    plt.scatter(X3[50:100], X4[50:100])
    plt.scatter(X3[100:150], X4[100:150])
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.show()
