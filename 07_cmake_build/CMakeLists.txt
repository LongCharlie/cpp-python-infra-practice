cmake_minimum_required(VERSION 3.15)
project(CmakePractice VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 1. 创建静态库 Target
add_library(math_utils STATIC src/math_utils.cpp)

# 2. 为库绑定头文件路径 (PUBLIC 传递机制)
target_include_directories(math_utils PUBLIC include)

# 3. 创建可执行文件 Target
add_executable(app_demo src/main.cpp)

# 4. 将库 Target 链接到可执行程序
target_link_libraries(app_demo PRIVATE math_utils)