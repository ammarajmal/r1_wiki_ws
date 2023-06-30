#!/usr/bin/env python3
# import contextlib
import rospy
from std_msgs.msg import Int16

# def number_publisher():
#     """function to generate and publish numbers
#         to the topic 'number'
#     """
#     pub = rospy.Publisher('number', Int16, queue_size=10)
#     rospy.init_node('number_publisher', anonymous=True)
#     rate = rospy.Rate(1)
#     number = 0
#     while not rospy.is_shutdown():
#         rospy.loginfo(number)
#         pub.publish(number)
#         number += 1
#         rate.sleep()

# if __name__ == '__main__':
#     with contextlib.suppress(rospy.ROSInterruptException):
#         number_publisher()

def publish_number(event):
    """_summary_

    Args:
        event (_type_): _description_
    """
    number = 5  # Your desired message data
    pub.publish(number)

if __name__ == '__main__':
    rospy.init_node('number_publisher', anonymous=True)
    pub = rospy.Publisher('number', Int16, queue_size=10)

    PUB_RATE = 1.0  # Desired publish rate in Hz
    rospy.Timer(rospy.Duration(1.0 / PUB_RATE), publish_number)

    rospy.spin()