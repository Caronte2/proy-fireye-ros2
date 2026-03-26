cmake_minimum_required(VERSION 3.8)
project(proy_fireye)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)

install(PROGRAMS
  scripts/danger_zone_detector.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
