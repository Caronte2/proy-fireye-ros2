import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MoveRobot(Node):
    def __init__(self):
        super().__init__('move_robot')

        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        timer_period = 0.1  # 每0.1秒发一次（关键！！）
        self.timer = self.create_timer(timer_period, self.move)

    def move(self):
        msg = Twist()

        # 👉 让机器人前进（你可以改）
        msg.linear.x = 0.3
        msg.angular.z = 0.0

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MoveRobot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
