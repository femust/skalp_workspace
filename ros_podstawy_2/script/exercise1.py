#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    # START
    # 2 lines init node and publisher
    rospy.init_node("vel_publisher")
    velocity_publisher=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    # END

    vel_msg = Twist();

    # Receiveing the user's input
    print("Poruszmy robota")
    speed = input("Podaj predkosc:")
    distance = input("Podaj dystans:")
    isForward = input("Przod/Tyl (1,0): ")  # True or False

    # Checking if the movement is forward or backwards
    if (isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    # Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        # Obecny czas
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while (current_distance < distance):
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = speed * (t1 - t0)

        # Zatrzymanie robota, gdy juz dotarl do pozycji
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass