cmake_minimum_required(VERSION 2.8.3)
project(ros_podstawy_2)

find_package(catkin REQUIRED COMPONENTS
 message_generation
)

add_message_files(
  FILES
  skalp.msg
)

generate_messages(
  DEPENDENCIES
#  std_msgs
)

catkin_package(
  CATKIN_DEPENDS message_runtime
)

#include_directories(
# include
#  ${catkin_INCLUDE_DIRS}
#)

