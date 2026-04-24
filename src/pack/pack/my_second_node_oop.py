#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class rosTest1(Node):
    def __init__(self):
        super().__init__("Test1_XYZ")
        print("RosTest1")

class rosTest2(Node):
    def __init__(self):
        super().__init__("Test2_XYZ")
        print("RosTest2")


def main(args=None):
    rclpy.init(args=args)
    node1 = rosTest1()
    node2 = rosTest2()
    rclpy.spin(node1)
    rclpy.spin(node2)
    rclpy.shutdown()
    rclpy.shutdown()



if __name__ == "__main__":
    main()