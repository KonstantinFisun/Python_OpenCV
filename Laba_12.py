import os
from tensorflow import keras

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Dropout
from keras.utils import np_utils

def main():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train / 255
    x_test = x_test / 255

    y_train_cat = keras.utils.to_categorical(y_train, 10)
    y_test_cat = keras.utils.to_categorical(y_test, 10)

    model = keras.Sequential([Flatten(input_shape=(28, 28, 1)), Dense(128, activation='relu'), Dense(10, activation='softmax')])

    print(model.summary())  # вывод структуры НС в консоль

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train, y_train_cat, batch_size=32, epochs=5, validation_split=0.2)
    model.evaluate(x_test, y_test_cat)

    print("Распознавание цифр на картинках\n")
    n = int(input("Введите номер картинки из тестовой базы MNIST или -1 для выхода из программы: "))

    while n != -1:
        x = np.expand_dims(x_test[n], axis=0)
        res = model.predict(x)
        print("Вектор выходов: ", res)
        print("Распознана цифра " + str(np.argmax(res)))
        plt.imshow(x_test[n], cmap=plt.cm.binary)
        plt.show()
        n = int(input("Введите номер картинки из тестовой базы MNIST или -1 для выхода из программы: "))

if __name__ == "__main__":
    main()
