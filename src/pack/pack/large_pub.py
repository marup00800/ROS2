#!/usr/bin/env python3
import rclpy    
from rclpy.node import Node
from example_interfaces.msg import Float32MultiArray

class class_pub(Node):
    def __init__(self):
        super().__init__("node1")
        self.pub=self.create_publisher(Float32MultiArray,"topicLarge", 10)
        #self.publisher_msg()
        self.time=self.create_timer(0.2, self.publisher_msg)

    def publisher_msg(self):
        msg = Float32MultiArray()
        msg.data = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
        self.pub.publish(msg)
        print(list(msg.data))

def main(args=None):
    rclpy.init(args=args)
    node = class_pub()
    rclpy.spin(node)
    rclpy.shutdown()



if __name__ == "__main__":
    main()