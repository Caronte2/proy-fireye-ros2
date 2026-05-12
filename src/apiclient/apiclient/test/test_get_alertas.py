## ros2 run apiclient test_get_alertas
import rclpy
from rclpy.node import Node
import requests


class TestGetAlertas(Node):
    def __init__(self):
        super().__init__('test_get_alertas')

        self.get_logger().info("🧪 GET ALERTAS TEST")

        try:
            res = requests.get("http://localhost:3000/api/alertas", timeout=2)
            self.get_logger().info(f"RESPUESTA: {res.json()}")
        except Exception as e:
            self.get_logger().error(str(e))


def main(args=None):
    rclpy.init(args=args)
    node = TestGetAlertas()
    rclpy.spin_once(node, timeout_sec=1)
    node.destroy_node()
    rclpy.shutdown()