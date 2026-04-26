#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class ascii_sub(Node):
    def __init__(self):
        super().__init__("node_ascii_sub")
        self.sub=self.create_subscription(String, "topic_ascii", self.sub, 10)

    def sub(self,msg):
        val = msg.data
        print("Received:", val)
        
        for char in val:
            ascii_val = ord(char)
            print(f"{char} → {ascii_val}")
            
def main(args=None):
    rclpy.init(args=args)
    node = ascii_sub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()