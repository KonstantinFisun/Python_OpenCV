import matplotlib.pyplot as plt
import cv2

# Загрузка изображения
def open_img(img_path):
    carplate_img = cv2.imread(img_path)
    carplate_img = cv2.cvtColor(carplate_img, cv2.COLOR_BGR2RGB)
    # Убрать оси
    plt.axis('off')
    plt.imshow(carplate_img)
    #plt.show()

    return carplate_img

# Извелечение координат номера изображения
# Возвращает список с координатами
def carplate_extract(image, carplate_haar_cascade):
    # Обнаружевание объектов разных размеров на входном изображении
    # Возвращает список из границ прямоугольника
    # Параметры: Изображение, насколько уменьшается изображение в каждом масштабе, качество обнаружения объектов
    carplate_rects = carplate_haar_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

    # Выделяем полученный объект
    for x, y, w, h in carplate_rects:
        carplate_img = image[y+15:y+h-10, x+15:x+w-20]

    return carplate_img

# Увеличивает изображение для лучшего распознавания
# Координаты и насколько увеличиваем изображение
# Получаем новое изображение
def enlarge_img(image, scale_percent):
    # Получаем новвый размер
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    # Сохраняем кортеж
    dim = (width, height)
    # Убрать оси
    plt.axis('off')
    # Изменяем размер изображения
    resized_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

    return resized_image


def main():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # Открытие изображения
    carplate_img_rgb = open_img(img_path='car.jpg')
    # Загрузка предобученной модели
    carplate_haar_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

    # Извлекаем координаты
    carplate_extract_img = carplate_extract(carplate_img_rgb, carplate_haar_cascade)
    # Увеличиваем изображение
    carplate_extract_img = enlarge_img(carplate_extract_img, 150)
    plt.imshow(carplate_extract_img)
    plt.show()

    # Преобразование в оттенки серого
    carplate_extract_img_gray = cv2.cvtColor(carplate_extract_img, cv2.COLOR_RGB2GRAY)
    plt.axis('off')
    plt.imshow(carplate_extract_img_gray, cmap='gray')
    plt.show()


# Точка входа в программу
if __name__ == '__main__':
    main()