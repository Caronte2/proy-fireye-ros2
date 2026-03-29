#!/usr/bin/env python3
import math

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry


class DangerZoneDetector(Node):
    def __init__(self):
        super().__init__('danger_zone_detector')

        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        self.fire_center = (0.0, 0.0)
        self.gas_center = (-5.0, -5.0)
        self.fire_radius = 2.0
        self.gas_radius = 2.0

        self.fire_detected = False
        self.gas_detected = False

        self.get_logger().info('DangerZoneDetector iniciado.')

    def odom_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        fire_distance = math.sqrt((x - self.fire_center[0]) ** 2 + (y - self.fire_center[1]) ** 2)
        gas_distance = math.sqrt((x - self.gas_center[0]) ** 2 + (y - self.gas_center[1]) ** 2)

        in_fire = fire_distance <= self.fire_radius
        in_gas = gas_distance <= self.gas_radius

        if in_fire and not self.fire_detected:
            self.fire_detected = True
            self.get_logger().warn('FUEGO DETECTADO')

        if not in_fire and self.fire_detected:
            self.fire_detected = False
            self.get_logger().info('Salida de zona de fuego')

        if in_gas and not self.gas_detected:
            self.gas_detected = True
            self.get_logger().warn('GAS DETECTADO')

        if not in_gas and self.gas_detected:
            self.gas_detected = False
            self.get_logger().info('Salida de zona de gas')


def main(args=None):
    rclpy.init(args=args)
    node = DangerZoneDetector()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

