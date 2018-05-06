#!/usr/bin/env python
import rospy
from geometry_msgs.msg import ####

def move():
    # START
    # 2 lines init node and publisher

    velocity_publisher=
    # END

    vel_msg = ####

    # Receiveing the user's input
    print("Poruszmy robota")
    speed = input("Podaj predkosc:")
    distance = input("Podaj dystans:")
    isForward = input("Przod/Tyl (1,0): ")  # True or False

    # Checking if the movement is forward or backwards
    if (isForward):
        vel_msg.#### = abs(speed)
    else:
        vel_msg.#### = -abs(speed)
    # Since we are moving just in x-axis
    vel_msg.#### = 0
    vel_msg.#### = 0
    vel_msg.#### = 0
    vel_msg.#### = 0
    vel_msg.#### = 0

    while not rospy.is_shutdown():

        # Obecny czas
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while (current_distance < distance):
            velocity_publisher.publish(####)
            t1 = rospy.Time.now().to_sec()
            current_distance = speed * (t1 - t0)

        # Zatrzymanie robota, gdy juz dotarl do pozycji
        vel_msg.linear.x = 0
        velocity_publisher.publish(####)

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass