cmake_minimum_required(VERSION 3.17)
project(war3b)

set(CMAKE_CXX_STANDARD 20)

add_executable(war3b main.cpp)


find_package(fmt CONFIG REQUIRED)
find_package( OpenCV REQUIRED )


include_directories( ${OpenCV_INCLUDE_DIRS} )


link_directories( ${OpenCV_LIB_DIR} )
target_link_libraries( war3b ${OpenCV_LIBS} fmt::fmt )