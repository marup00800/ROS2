#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

    
class move_turtle(Node):
    def __init__(self):
        super().__init__("node_turtle")
        self.pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.call)

    def call(self):
        msg = Twist()
        msg.linear.x = 0.2 #Move forward
        msg.angular.z = -0.3 #Move left
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = move_turtle()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()