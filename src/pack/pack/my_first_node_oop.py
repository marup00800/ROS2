#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class rosClass(Node):

    def __init__(self):
        super().__init__("xyz")
        print("My first oop111 Node")


def main(args=None):
    rclpy.init(args=args)
    node1 = rosClass()
    rclpy.spin(node1)
    rclpy.shutdown()


if __name__=="__main__":
    main()


