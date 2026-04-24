#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class class_sub(Node):
    def __init__(self):
        super().__init__("node_sub")
        self.sub = self.create_subscription(String, "topic12", self.sub, 25)

    def sub(self, msg):
        val = msg.data
        print(val)


def main (args=None):
    rclpy.init(args=args)
    node = class_sub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ =="__main__":
    main()