cmake_minimum_required(VERSION 3.22)
project(game)

add_definitions("-std=c++20")

file(GLOB SOURCES "src/*.cpp")

find_package(SDL2)

set(CMAKE_TOOLCHAIN_FILE ./conan/conan_toolchain.cmake)

add_executable(game ${SOURCES})
target_link_libraries(game SDL2::SDL2)