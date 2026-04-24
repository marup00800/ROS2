#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node1 = Node("Node1")
    node2 = Node("Node2")

    print("Hello, 2 Node Created")

    rclpy.spin(node1)
    rclpy.spin(node2)
    rclpy.destroy_node()
    rclpy.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()