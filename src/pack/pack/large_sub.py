#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
from example_interfaces.msg import Float32MultiArray

class class_sub(Node):
    def __init__(self):
        super().__init__("node2")
        self.sub=self.create_subscription(Float32MultiArray,"topicLarge",self.sub,10)

    def sub(self,msg):
        val = msg.data
        length=len(val)
        large=val[0]
        i=1
        while i < length:
            if large<val[i]:
                large=val[i]
            i=i+1
        print("Largest Element is : " + str(large))


def main(args=None):
    rclpy.init(args=args)
    node = class_sub()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()