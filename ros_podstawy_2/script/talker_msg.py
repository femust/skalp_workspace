#!/usr/bin/env python

import rospy

from ros_podstawy_2.msg import skalp

def talker():
    pub = rospy.Publisher('chatter_msg', skalp, queue_size=10)
    rospy.init_node('talker_msg')
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str=skalp()
        hello_str.first_name = "Andrzej"
        hello_str.last_name = "Reinke"
        hello_str.age = 25
        hello_str.my_score = 88
        print(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass