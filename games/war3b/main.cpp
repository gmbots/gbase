#include <iostream>
#include <fmt/core.h>
#include <opencv2/opencv.hpp>
//#include "services/dmsoft.h"

int main() {
//    runDm();
    auto img = cv::imread(R"(C:\Users\ysh35\Pictures\2.bmp)");

    cv::imshow("Demo", img);
    std::cout << "Hello, World!" << std::endl;
    fmt::print("Hello world");


    cv::waitKey(0);
    return 0;

}
