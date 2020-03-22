cmake_minimum_required(VERSION 3.5)

project(BoostExample LANGUAGES CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

include(GNUInstallDirs)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} CONAN_PKG::boost)
target_compile_options(${PROJECT_NAME}
    PRIVATE
        -Wall -Wextra -Wpedantic -Wconversion -Wcast-qual -Wshadow
)

install(TARGETS ${PROJECT_NAME}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)