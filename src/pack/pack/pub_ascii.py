#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class ascii_pub(Node):
    def __init__(self):
        super().__init__("node_ascii_pub")
        self.pub=self.create_publisher(String, "topic_ascii", 10)
        self.time=self.create_timer(0.5, self.publisher_msg)

    def publisher_msg(self):
        msg = String()
        msg.data = "Marup Hossain"
        self.pub.publish(msg)
        print(msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = ascii_pub()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()
