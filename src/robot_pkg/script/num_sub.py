#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

def callback(msg):
    """function to print the received message
    """
    rospy.loginfo("Received %d", msg.data)

def number_subscriber():
    """function to subscribe to the topic 'number'
    """
    rospy.init_node('number_subscriber', anonymous=True)
    rospy.Subscriber('number', Int16, callback)
    rospy.spin()
if __name__ == '__main__':
    number_subscriber()