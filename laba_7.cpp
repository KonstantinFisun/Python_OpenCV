#include <stdio.h>
#include <opencv2/opencv.hpp>

int main(int argc, char** argv)
{
cv::capture* capture = cv::createFileCapture("f.avi");

if( !capture )
{
return -1;
}

cv::iplImage* bgr_frame = cv::queryFrame( capture );
double fps = cv::GetCaptureProperty( capture, CV_CAP_PROP_FPS);
cv::Size size = cv::Size((int)cv::GetCaptureProperty( capture, CV_CAP_PROP_FRAME_WIDTH),
(int)cv::GetCaptureProperty( capture, CV_CAP_PROP_FRAME_HEIGHT));
cv::VideoWriter* writer = cv::CreateVideoWriter("1.avi", CV_FOURCC('M','J','P','G'), fps, size);
IplImage* logpolar_frame = cvCreateImage( size, IPL_DEPTH_8U, 3);

while( (bgr_frame=cvQueryFrame(capture)) != NULL )
{
cv::LogPolar( bgr_frame, logpolar_frame, cv::Point2D32f(bgr_frame->width/2, bgr_frame->height/2),
40, CV_INTER_LINEAR+CV_WARP_FILL_OUTLIERS );
cv::WriteFrame( writer, logpolar_frame );
}

cv::ReleaseVideoWriter( &writer );
cv::ReleaseImage( &logpolar_frame );
cv::ReleaseCapture( &capture );
return(0);
}
