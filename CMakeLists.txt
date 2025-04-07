cmake_minimum_required(VERSION 3.10)
project(EmbeddedProject C CXX)

set(CMAKE_C_STANDARD 99)
set(CMAKE_CXX_STANDARD 11)

# For debugging
message(STATUS "C Compiler: ${CMAKE_C_COMPILER}")
message(STATUS "C++ Compiler: ${CMAKE_CXX_COMPILER}")

# Collect all component source and include files
file(GLOB_RECURSE COMPONENT_SOURCES "components/*/src/*.c")
file(GLOB COMPONENT_INCLUDES RELATIVE ${CMAKE_SOURCE_DIR} "components/*/include")
include_directories(${COMPONENT_INCLUDES})

# Also include top-level include folder
include_directories(include)

# Main source
set(SOURCES src/main.c ${COMPONENT_SOURCES})

# Build main executable
add_executable(main ${SOURCES})

# Enable testing
enable_testing()
find_package(GTest REQUIRED)

# Collect all test files
file(GLOB_RECURSE TEST_SOURCES "components/*/test/*.cpp" "tests/*.cpp")

# Build test runner
add_executable(runTests ${TEST_SOURCES} ${COMPONENT_SOURCES})
target_include_directories(runTests PRIVATE ${COMPONENT_INCLUDES} include)
target_link_libraries(runTests GTest::GTest GTest::Main pthread)

add_test(NAME AllTests COMMAND runTests)
