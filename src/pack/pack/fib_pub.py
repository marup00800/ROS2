#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 
from example_interfaces.msg import Int32


class class_pub(Node):
    def __init__(self):
        super().__init__("node_fib")
        self.pub2=self.create_publisher (Int32, "topic_fib", 10)
        self.timer=self.create_timer(0.5, self.call) 

    def call(self):
        val=Int32()
        val.data= int(input("Enter a value"))
        self.pub2.publish(val)       


def main(args=None):
    rclpy.init(args=args)
    node=class_pub()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()