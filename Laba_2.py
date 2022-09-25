import math

import cv2
import numpy as np

def gauss(n, sigma, img):

    # Для сравнения
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Для расчетов
    newGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Высота и ширина картинки
    heigth = len(img)
    width = len(img[0])

    # Центр свертки
    a = b = n // 2

    # Сумма элементов матрицы свертки
    sum = 0

    # Заполняем матрицу свертки нуулями
    gauss_matrix = [[0] * n for i in range(n)]

    # Заполнить матрицу свертки значениями функции Гаусса с мат. ожиданием, равным координатам центра матрицы
    for x in range(n):
        for y in range(n):
            gauss_matrix[x][y] = (1 / (2 * np.pi * sigma ** 2 )) * np.exp (-((((x - a) ** 2 ) + ((y - b) ** 2)) / 2 * sigma ** 2) )
            sum += gauss_matrix[x][y]


    # Нормируем матрицу
    for x in range(n):
        for y in range(n):
            gauss_matrix[x][y] /= sum

    # Выбираем границы обхода
    h_start = a
    w_start = a
    h_finish = heigth - a
    w_finish  = width - a

    # Операция свертки
    for i in range(h_start,h_finish):
        for j in range(w_start, w_finish):
            newVal = 0
            for k in range(n):
                for l in range(n):
                    newVal = newVal + gauss_matrix[k][l] * newGray[i - a + k][j - a + l]
            newGray[i][j] = newVal


def main():
    img = cv2.imread(r'2.jpg')

    n = 7
    sigma = 1
    gauss(n,sigma,img)

if __name__ == "__main__":
    main()