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

    # Возвращаем
    return newGray


def display_images_kort(imgarray):
    rows = len(imgarray)  # Длина кортежа или списка
    cols = len(imgarray[
                   0])  # Если imgarray - это список, вернуть количество каналов первого изображения в списке, если это кортеж, вернуть длину первого списка, содержащегося в кортеже
    # print("rows=", rows, "cols=", cols)

    # Масштабируемость
    scale = 0.3

    # Определить, является ли тип imgarray [0] списком
    # Список, указывающий, что imgarray является кортежем и должен отображаться вертикально
    rowsAvailable = isinstance(imgarray[0], list)

    # Ширина и высота первой картинки
    width = imgarray[0][0].shape[1]
    height = imgarray[0][0].shape[0]
    # print("width=", width, "height=", height)

    # Если входящий кортеж
    for x in range(0, rows):
        for y in range(0, cols):
            # Обойти кортеж, если это первое изображение, не преобразовывать
            if imgarray[x][y].shape[:2] == imgarray[0][0].shape[:2]:
                imgarray[x][y] = cv2.resize(imgarray[x][y], (0, 0), None, scale, scale)
            # Преобразуйте другие матрицы к тому же размеру, что и первое изображение, и коэффициент масштабирования будет масштабироваться
            else:
                imgarray[x][y] = cv2.resize(imgarray[x][y], (imgarray[0][0].shape[1], imgarray[0][0].shape[0]),
                                            None, scale, scale)

    # Создайте пустой холст того же размера, что и первое изображение
    imgBlank = np.zeros((height, width, 3), np.uint8)
    hor = [imgBlank] * rows  # Тот же размер, что и первое изображение, и столько же горизонтальных пустых изображений, сколько кортеж содержит список
    for x in range(0, rows):
        # Расположить x-й список в кортеже по горизонтали
        hor[x] = np.hstack(imgarray[x])
    ver = np.vstack(hor)  # Объединить разные списки по вертикали

    cv2.namedWindow('Display window', cv2.WINDOW_NORMAL)
    cv2.imshow('Display window', ver)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def display_images_list(imgarray):
    rows = len(imgarray)  # Длина кортежа или списка
    cols = len(imgarray[
                   0])  # Если imgarray - это список, вернуть количество каналов первого изображения в списке, если это кортеж, вернуть длину первого списка, содержащегося в кортеже
    # print("rows=", rows, "cols=", cols)

    # Масштабируемость
    scale = 1


    # Ширина и высота первой картинки
    width = imgarray[0].shape[1]
    height = imgarray[0].shape[0]
    # print("width=", width, "height=", height)

    # Операция трансформации, как и раньше
    for x in range(0, rows):
        if imgarray[x].shape[:2] == imgarray[0].shape[:2]:
            imgarray[x] = cv2.resize(imgarray[x], (0, 0), None, scale, scale)
        else:
            imgarray[x] = cv2.resize(imgarray[x], (imgarray[0].shape[1], imgarray[0].shape[0]), None, scale, scale)
    # Расположить список по горизонтали
    hor = np.hstack(imgarray)
    ver = hor

    cv2.namedWindow('Display window', cv2.WINDOW_NORMAL)
    cv2.imshow('Display window', ver)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def dis(imgarray):
    scale = 0.5

    rows = len(imgarray)  # Длина кортежа или списка
    cols = len(imgarray[
                   0])  # Если imgarray - это список, вернуть количество каналов первого изображения в списке, если это кортеж, вернуть длину первого списка, содержащегося в кортеже
    print("rows= ", rows, "cols=", cols)

    # Определить, является ли тип imgarray [0] списком
    # Список, указывающий, что imgarray является кортежем и должен отображаться вертикально
    rowsAvailable = isinstance(imgarray[0], list)

    # Ширина и высота первой картинки
    width = imgarray[0][0].shape[1]
    height = imgarray[0][0].shape[0]
    print("width=", width, "height=", height)

    # Если входящий кортеж
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                # Обойти кортеж, если это первое изображение, не преобразовывать
                if imgarray[x][y].shape[:2] == imgarray[0][0].shape[:2]:
                    imgarray[x][y] = cv2.resize(imgarray[x][y], (0, 0), None, scale, scale)
                # Преобразуйте другие матрицы к тому же размеру, что и первое изображение, и коэффициент масштабирования будет масштабироваться
                else:
                    imgarray[x][y] = cv2.resize(imgarray[x][y], (imgarray[0][0].shape[1], imgarray[0][0].shape[0]),
                                                None, scale, scale)
                # Если изображение в оттенках серого, преобразовать его в цветное отображение
                if len(imgarray[x][y].shape) == 2:
                    imgarray[x][y] = cv2.cvtColor(imgarray[x][y], cv2.COLOR_GRAY2BGR)

        # Создайте пустой холст того же размера, что и первое изображение
        imgBlank = np.zeros((height, width, 3), np.uint8)
        hor = [
                  imgBlank] * rows  # Тот же размер, что и первое изображение, и столько же горизонтальных пустых изображений, сколько кортеж содержит список
        for x in range(0, rows):
            # Расположить x-й список в кортеже по горизонтали
            hor[x] = np.hstack(imgarray[x])
        ver = np.vstack(hor)  # Объединить разные списки по вертикали


    # Если входящий - это список
    else:
        # Операция трансформации, как и раньше
        for x in range(0, rows):
            if imgarray[x].shape[:2] == imgarray[0].shape[:2]:
                imgarray[x] = cv2.resize(imgarray[x], (0, 0), None, scale, scale)
            else:
                imgarray[x] = cv2.resize(imgarray[x], (imgarray[0].shape[1], imgarray[0].shape[0]), None, scale, scale)
            if len(imgarray[x].shape) == 2:
                imgarray[x] = cv2.cvtColor(imgarray[x], cv2.COLOR_GRAY2BGR)
        # Расположить список по горизонтали
        hor = np.hstack(imgarray)
        ver = hor

    cv2.namedWindow('Display window', cv2.WINDOW_NORMAL)
    cv2.imshow('Display window', ver)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Реализовать фильтр Гаусса средствами языка python
def task_1(img,n,sigma):
    # Изначальное изображение
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Фильтр Гаусса
    newGray = gauss(n, sigma, img)

    display_images_list([gray, newGray])

# Применить данный фильтр для двух разных значений среднего квадратичного отклонения
# и двух разных размерностей матрицы свертки, сравнить результаты для ОДНОГО изображения
def task_2(img):
    # Изначальное изображение
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    newGray_1 = gauss(5,0.5,img)
    newGray_2 = gauss(7, 0.5, img)
    newGray_3 = gauss(3, 0.3, img)
    newGray_4 = gauss(3, 0.7, img)

    display_images_list([gray, newGray_1, newGray_2, newGray_3, newGray_4])

#   Реализовать размытие Гаусса встроенным методом
#   библиотеки OpenCV, сравнить результаты с Вашей реализацией.
def task_3(img, n, sigma):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Встроенный метод
    img_blur = cv2.GaussianBlur(gray, (n, n), sigma)

    # Моя реализация
    image_my_blur = gauss(n, sigma, img)

    Blankimg = np.zeros((200, 200), np.uint8)  # Размер может быть принудительно преобразован любой функцией
    dis(([gray, gray], [img_blur, image_my_blur]))

def main():
    img = cv2.imread(r'2.jpg')
    n = 5
    sigma = 0.5
    # task_1(img,n,sigma)
    # task_2(img)
    task_3(img, n,sigma)



if __name__ == "__main__":
    main()