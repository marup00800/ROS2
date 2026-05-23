#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from interface1.msg import Cus1
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup

class class_cus1(Node):
    def __init__(self):
        super().__init__('node1_cus')
        self.sub = self.create_subscription(Cus1, 'topic_cus', self.callback, 10)
        self.pub = self.create_publisher(Cus1, 'topic_cus1', 10)
        callback_groups = MutuallyExclusiveCallbackGroup()
        self.timer = self.create_timer(0.5, self.publisher1, callback_groups)
        self.length = 0
        

    def callback(self, msg):
        val = msg.sh
        print(val)
        self.length = len(val)
    
    def publisher1(self):
        f = Cus1()
        f.le = self.length
        self.pub.publish(f)

def main(args=None):
    rclpy.init(args=args)
    node = class_cus1()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()