from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
from Draw_Figure import Draw_Iris_Dataset
from train_test_Model import split_data
from train_test_Model import fit_data
from train_test_Model import test_data
from train_test_Model import testing

data = pd.read_csv('IrisData.txt')

def UI():
    window = Tk()
    window.geometry("1000x250")
    window.title("Perceptron Algorithm")
    'window.configure(background="white")'
    f1_label = Label(window, text="Feature #1", fg="white", font=("Helvetica", 10))
    f1_label.configure(background="blue")
    f1_label.place(x=20, y=20)
    f1_combo = ttk.Combobox(window, values=["X1", "X2", "X3", "X4"])
    f1_combo.place(x=100, y=20)

    f2_label = Label(window, text="Feature #2", fg="white", font=("Helvetica", 10))
    f2_label.configure(background="blue")
    f2_label.place(x=300, y=20)
    f2_combo = ttk.Combobox(window, values=["X1", "X2", "X3", "X4"])
    f2_combo.place(x=380, y=20)

    c1_label = Label(window, text="Class #1", fg="white", font=("Helvetica", 10))
    c1_label.configure(background="blue")
    c1_label.place(x=20, y=70)
    c1_combo = ttk.Combobox(window, values=["Iris-setosa", "Iris-versicolor", "Iris-virginica"])
    c1_combo.place(x=100, y=70)

    c2_label = Label(window, text="Class #2", fg="white", font=("Helvetica", 10))
    c2_label.configure(background="blue")
    c2_label.place(x=300, y=70)
    c2_combo = ttk.Combobox(window, values=["Iris-setosa", "Iris-versicolor", "Iris-virginica"])
    c2_combo.place(x=380, y=70)

    learning_rate_label = Label(window, text="Learning Rate", fg="white", font=("Helvetica", 8))
    learning_rate_label.configure(background="gray")
    learning_rate_label.place(x=20, y=120)
    learning_rate_textbox = Entry(window)
    learning_rate_textbox.place(x = 110, y = 120)

    epoch_label = Label(window, text="Epochs", fg="white", font=("Helvetica", 8))
    epoch_label.configure(background="gray")
    epoch_label.place(x=300, y=120)
    epoch_textbox = Entry(window)
    epoch_textbox.place(x=380, y=120)

    var = IntVar()
    bias_check = Checkbutton(window, text="Bias", font=("Helvetica", 10), variable=var)
    bias_check.configure(background="white")
    bias_check.place(x=250, y=170)

    test_label = Label(window, text="Testing Phase", fg="white", font=("Helvetica", 10))
    test_label.configure(background="blue")
    test_label.place(x=650, y=20)

    test1 = Label(window, text="X1", fg="white", font=("Helvetica", 10))
    test1.configure(background="blue")
    test1.place(x=650, y=50)
    test1_textbox = Entry(window)
    test1_textbox.place(x=690, y=50)

    test2 = Label(window, text="X2", fg="white", font=("Helvetica", 10))
    test2.configure(background="blue")
    test2.place(x=650, y=80)
    test2_textbox = Entry(window)
    test2_textbox.place(x=690, y=80)

    test_button = Button(window, text="Test!", font=("Helvetica", 10), command=lambda: testing(test1_textbox.get(), test2_textbox.get(), c1_combo.get(), c2_combo.get()))
    test_button.place(x=750, y=120)
    test_button.config(height=1, width=10)

    def run():
        (feature1, feature2, class1, class2, eta, epochs, bias) = (None, None, None, None, None, None, None)
        feature1 = f1_combo.get()
        feature2 = f2_combo.get()
        class1 = c1_combo.get()
        class2 = c2_combo.get()
        eta = learning_rate_textbox.get()
        epochs = epoch_textbox.get()
        bias = var.get()
        if feature2 == feature1:
            messagebox.showinfo("Error", "Equal Features")
        if class2 == class1:
            messagebox.showinfo("Error", "Equal Classes")
        if feature2 != feature1 and class2 != class1:
            messagebox.showinfo("Info", "Done")
            split_data(data, feature1, feature2, class1, class2)
            fit_data(feature1, feature2, class1, class2, eta, epochs, bias)
            test_data(feature1, feature2, class1, class2)

    run_button = Button(window, text="Run!", font=("Helvetica", 10), command=run)
    run_button.place(x=450, y=200)
    run_button.config(height=1, width=15)

    window.mainloop()


if __name__ == "__main__":
    Draw_Iris_Dataset(data)
    UI()
