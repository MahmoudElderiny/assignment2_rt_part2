cmake_minimum_required(VERSION 3.5)
project(robot_urdf)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)           # Add rclpy dependency for Python nodes
find_package(geometry_msgs REQUIRED)   # Add geometry_msgs dependency for Twist messages

# Install directories
install(DIRECTORY
  launch urdf config worlds
  DESTINATION share/${PROJECT_NAME}/
)

# Install the Python node
install(
  PROGRAMS
  scripts/robot_controller.py  # Path to your Python node script
  DESTINATION lib/${PROJECT_NAME}       # Install to the lib folder under project name
)

# Testing (optional)
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

# Mark the package as ament-compatible
ament_package()

