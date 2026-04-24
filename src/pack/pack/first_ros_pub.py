#!/usr/bin/env pyhton3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.msg import String

class class_pub(Node):
    def __init__(self):
        super().__init__("ros2_pub_node")
        self.pub=self.create_publisher(String,"topic1",25)
        self.publisher_msg()
    
    def publisher_msg(self):
        msg=String()
        msg.data="Hey i am publish data 1"
        self.pub.publish(msg)
        print(msg)


def main(args=None):
    rclpy.init(args=args)
    node=class_pub()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ =="__main__":
    main()