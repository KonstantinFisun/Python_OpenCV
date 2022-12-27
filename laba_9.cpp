#include <opencv2/opencv.hpp>
#include <iostream>
#include <time.h>

 
using namespace cv;
using namespace std;
 
int main( int argc, char** argv ) {
  cout << getNumThreads() << endl;
 
  VideoCapture cap("http://10.80.246.179:8080/video"); //захват webcam
 
  int ret;
  ret = cap.set(3, 320); // Установка ширины
  ret = cap.set(4, 240); // Установка высоты
 
  if ( !cap.isOpened() )  // Если не запускается webcam
  {
       cout << "Cannot open the web cam" << endl;
       return -1;
  }
 
  namedWindow("Control", WINDOW_NORMAL); // Выводим окно
 
 
 // Установка минимальных и максимальных параметров
  int iLowH = 140;
  int iHighH = 179;
 
  int iLowS = 150; 
  int iHighS = 255;
 
  int iLowV = 60;
  int iHighV = 255;
 
  //Create trackbars in "Control" window
  createTrackbar("LowH", "Control", &iLowH, 179); //Тональность (0 - 179)
  createTrackbar("HighH", "Control", &iHighH, 179);
 
  createTrackbar("LowS", "Control", &iLowS, 255); //Насышенность (0 - 255)
  createTrackbar("HighS", "Control", &iHighS, 255);
 
  createTrackbar("LowV", "Control", &iLowV, 255);//Яркость (0 - 255)
  createTrackbar("HighV", "Control", &iHighV, 255);
 
  int iLastX = -1; // Инициализация горизонтальной позиции
  int iLastY = -1; // Инициация вертикальной позиции
 
  // Захват первого кадра с камеры
  Mat imgTmp;
  cap.read(imgTmp); 
 
  // Создание черного изображения с размером фрейма
  Mat imgLines = Mat::zeros( imgTmp.size(), CV_8UC3 );;
 
 // Установка времени
  time_t start,end;
  time (&start);
 
  // Количество фреймов
  int frames = 0;
 
 
  while (true) {
  	
  	Mat imgOriginal; // Новый кадр
 
        bool bSuccess = cap.read(imgOriginal); // Считываем новый кадр
	// Не удалось считать кадр
	if (!bSuccess) {      
 	    cout << "Cannot read a frame from video stream" << endl;
	    break;
	}
  	Mat imgHSV;
 
  	cvtColor(imgOriginal, imgHSV, COLOR_BGR2HSV); // Перевод кадра в HSV
 
  	// Пороговое изображение
  	Mat imgThresholded;
 
  
  	inRange(imgHSV, Scalar(iLowH, iLowS, iLowV), Scalar(iHighH, iHighS, iHighV), imgThresholded); //Детектим объект(255), если он соответствует параметрам
 
 	// Морфологические операторы
	  //Размытие изображения(min)
	  erode(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)) ); // Вход, выход, ядро
	  // Расширение изображение(max)
	  dilate( imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)) ); 
	 
	  // Расширение изображение(max)
	  dilate( imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)) ); 
	  //Размытие изображения(min)
	  erode(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)) );
	  
	  // Считаем момент для изображения
	  Moments oMoments = moments(imgThresholded);
	 
	  double dM01 = oMoments.m01; // Получаем значение по вертикали
	  double dM10 = oMoments.m10; // Получаем значение по горизонтали
	  double dArea = oMoments.m00; // Получаем площадь объекта
	 
	  // Считаем, если область имеет разрем больше 10000
	  if (dArea > 10000)
	  {
	   // Вычисляем позицию объекта
	   int posX = dM10 / dArea; // Вычисляем позицию по горизонтали
	   int posY = dM01 / dArea; // Вычисляем позицию по вертикали      
	 
	   if (iLastX >= 0 && iLastY >= 0 && posX >= 0 && posY >= 0)
	   {
	    // Рисуем линии от предыдущей точки до текущей 
	    //line(imgLines, Point(posX, posY), Point(iLastX, iLastY), Scalar(0,0,255), 2);
	    rectangle(imgLines, Point(posX-50, posY-150), Point(iLastX+50, iLastY+150), Scalar(0,255,0), 2);
	   }
	 
	   iLastX = posX;
	   iLastY = posY;
	  }
	 
	    imshow("Thresholded Image", imgThresholded); // Вывод порога
	 
	    imgOriginal = imgOriginal + imgLines;
	    imshow("Original", imgOriginal); // Вывод оригинального изображения с полученным объектом
	 
	    if (waitKey(30) == 27) //Если был нажат Esc
	    {
		  cout << "esc key is pressed by user" << endl;
		  break; 
	    }
	 
	    frames++;
}
 
  time (&end);
  double dif = difftime (end,start);
  printf("FPS %.2lf seconds.\r\n", (frames / dif));
 
  return 0;
}
