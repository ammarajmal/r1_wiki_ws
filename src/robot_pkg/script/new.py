#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

def number_callback(data):
    """Callback function to handle received numbers"""
    number = data.data
    rospy.loginfo("Received number: %d", number)

def number_subscriber():
    """Function to initialize the subscriber"""
    rospy.init_node('number_subscriber', anonymous=True)
    rospy.Subscriber('number', Int16, number_callback)
    rospy.spin()

if __name__ == '__main__':
    number_subscriber()
