#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtleSimControl:
    def __init__(self):
        pub_topic = '/turtle1/cmd_vel'
        sub_topic = '/turtle1/pose'
        
        self.pub = rospy.Publisher(pub_topic, Twist, queue_size=10)
        self.sub = rospy.Subscriber(sub_topic, Pose, self.pose_callback)
        self.velocity_msg = Twist()
        self.publish_rate = rospy.Rate(10)
        
    def pose_callback(self, msg):
        self.velocity_msg.linear.x = 4.0
        self.velocity_msg.angular.z = 1.0
        self.pub.publish(self.velocity_msg)
        self.publish_rate.sleep()
if __name__ == '__main__':
    rospy.init_node('turtlesim_control')
    control = TurtleSimControl()
    rospy.spin()