#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 
from example_interfaces.msg import String

class class_pub(Node):
    def __init__(self):
        super().__init__("ros2_pub_node2")
        self.pub = self.create_publisher(String, "topic12", 25)
        self.timer = self.create_timer(0.2, self.publisher_msg)
    
    def publisher_msg(self):
        msg = String()
        msg.data = "Hey i am publish data 12"
        self.pub.publish(msg)
        print(msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = class_pub()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()