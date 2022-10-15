import cv2
from urllib.request import urlopen
import numpy as np
import datetime

def show_img():
    img = cv2.imread(r'C:\1.png')

    cv2.namedWindow('Display window', cv2.WINDOW_NORMAL)
    cv2.imshow('Display window', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_video():
    cap = cv2.VideoCapture(r'C:\1.mp4', cv2.CAP_ANY)
    cv2.namedWindow('Display window', cv2.WINDOW_NORMAL)
    while(True):
        ret, frame = cap.read()
        if not (ret):
            break
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

def readIPWriteTOFile():
    video = cv2.VideoCapture(0)
    ok, img = video.read()
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter("output.mov", fourcc, 25, (w, h))
    while (True):
        ok, img = video.read()

        if ok:
            font = cv2.FONT_HERSHEY_SIMPLEX

            dt = str(datetime.datetime.now())

            frame = cv2.putText(img, dt,
                                (0, 30),
                                font, 0.5,
                                (0, 0, 0),
                                2, cv2.LINE_8)

        cv2.imshow('img', img)
        video_writer.write(img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()

def readWeb():
    cap = cv2.VideoCapture(r'output.mov', cv2.CAP_ANY)
    cv2.namedWindow('Display window', cv2.WINDOW_NORMAL)
    while (True):
        ret, frame = cap.read()
        if not (ret):
            break
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

def show_from_telephone():
    url = 'http://10.176.71.110:8080/shot.jpg'
    imgResp = urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)

    w = len(img[0])
    h = len(img)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter("output_from_telephone.mov", fourcc, 25, (w, h))

    while True:
        imgResp = urlopen(url)
        imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
        img = cv2.imdecode(imgNp, -1)
        cv2.imshow('test', img)
        video_writer.write(img)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()



def main():
    # show_img
    # show_video()
    readIPWriteTOFile()
    # show_from_telephone()


if __name__ == "__main__":
    main()

