#include <opencv2/opencv.hpp>
#include <iostream>
using namespace std;
using namespace cv;

int main( int argc, char** argv ) {

 Mat image, new_imageHSV;
 //Read image
 image = imread("1.jpg" , 1);

 // Изображение не открылось
 if(! image.data ) {
  cout << "Невозможно открыть файл" << endl ;
  return -1;
 }
 // Размер изображения
 int width = image.cols, height = image.rows;
 
 // Перевод изображения в HSV
 cvtColor(image, new_imageHSV, COLOR_BGR2HSV);
	
 // Центральный пиксель берем цветовой тон
 int c = (int)new_imageHSV.at<Vec3b>(height/2,width/2)[0];
 cout << c << endl; // Вывод центрального пикселя
 // Определение цвета
 Scalar color;
 if(c >= 0 && c < 30 || c >= 150 && c < 180)
 color = Scalar(0,0,255); // Голубой
 else if(c >= 30 && c < 90)
 color = Scalar(0,255,0); // Зеленый
 else if(c >= 90 && c < 150)
 color = Scalar(255,0,0); // Красный

 // Рисуем треугольник
 int w = 50, h = 300;
 int x = (width-w)/2, y = (height-h)/2;
 rectangle(image, Rect(x, y, w, h), color, -1);

 x = (width-h)/2, y = (height-w)/2;
 rectangle(image, Rect(x, y, h, w), color, -1);

 namedWindow( "HSV", WINDOW_NORMAL);
 resizeWindow("HSV", (width*((700*100)/height))/100, 700);
 imshow( "HSV", new_imageHSV);

 namedWindow( "Center", WINDOW_NORMAL);
 resizeWindow("Center", (width*((700*100)/height))/100, 700);
 imshow( "Center", image);

 waitKey(0);
 return 0;
}
