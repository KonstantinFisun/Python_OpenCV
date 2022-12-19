import cv2
import math
import matplotlib.pyplot as plt
from scipy. special import logsumexp
import numpy as np

def motion_detect():

    # Считываем видео из файла
    cap = cv2.VideoCapture(r'output.mov', cv2.CAP_ANY)

    # Прочитать первый кадр
    ret, frame = cap.read()

    # Перевести в черный белый цвет
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Применяем размытие Гаусса

    # Параметры фильтра Гаусса
    window_size = 5
    sigma = 5

    # Свертка изображения с помощью фильтра Гаусса
    new_frame = cv2.GaussianBlur(gray, (window_size,window_size), sigma)

    h = len(gray)
    w = len(gray[0])

    # Подготовка файла для записи
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter("result.mov", fourcc, 25, (w, h))

    # Подготовка окна
    cv2.namedWindow('Display window', cv2.WINDOW_NORMAL)


    # Цикл до завершения изображения
    while(True):
        cv2.imshow('frame', frame)

        # Скопировать старый кадр
        old_frame = new_frame

        # Считываем новый кадр
        ret, frame = cap.read()

        # Eсли чтение неуспешно, остановить цикл
        if not (ret):
            break

        # Перевести в черный белый цвет
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Свертка изображения с помощью фильтра Гаусса

        new_frame = cv2.GaussianBlur(gray, (window_size, window_size), sigma)


        # Найти разницу между двумя кадрами в отдельный фрейм
        frame_dif = cv2.absdiff(old_frame, new_frame)

        # print(old_frame[0][0],new_frame[0][0],frame_dif[0][0])

        # Провести операцию двоичного разделения для фрейма
        retval, frame_dif = cv2.threshold(frame_dif, 60, 127, cv2.THRESH_BINARY)

        # Найти контуры объектов для фрейма
        contours, hierarchy = cv2.findContours(frame_dif, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Пройтись по контурам объектов для фрейма, найти контур площадью большей, чем наперед заданный параметр
        for i in contours:
            if(200 < cv2.contourArea(i)):
                # Если нашли
                video_writer.write(frame)
                continue


        # Выход из цикла
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


def main():
    motion_detect()


if __name__ == "__main__":
    main()