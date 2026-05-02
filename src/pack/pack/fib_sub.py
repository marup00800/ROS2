#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int32 

class class_sub(Node):
    def __init__(self):
        super().__init__("node_fib_sub")
        self.subscription = self.create_subscription(
            Int32,
            "topic_fib",
            self.callback,
            10
        )

    def callback(self, msg):
        val = msg.data
        print(f"Received: {val}")

        for i in range(val + 1):
            print(self.fib(i))

    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)


def main(args=None):
    rclpy.init(args=args)
    node = class_sub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()