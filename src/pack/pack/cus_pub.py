#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from interface1.msg import Cus1

class class_cus(Node):
    def __init__(self):
        super().__init__('node_cus')
        self.pub2 = self.create_publisher(Cus1, 'topic_cus', 10)
        self.timer = self.create_timer(0.5, self.call)

    def call(self):
        val = Cus1()
        val.sh = "hello world"
        print(val)
        self.pub2.publish(val)


def main(args=None):
    rclpy.init(args=args)
    node = class_cus()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

