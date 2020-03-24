cmake_minimum_required(VERSION 3.5)

project(BoostExample LANGUAGES CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

include(GNUInstallDirs)

option(ENABLE_WERROR "Treat compiler warnings as errors" ON)
if(ENABLE_WERROR)
    add_compile_options(-Werror)
endif()
add_compile_options(-Wall -Wextra -Wpedantic -Wconversion -Wcast-qual -Wshadow)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} CONAN_PKG::boost)

install(TARGETS ${PROJECT_NAME}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)