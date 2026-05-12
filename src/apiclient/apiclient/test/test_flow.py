##ros2 run apiclient test_flow
import rclpy
from rclpy.node import Node
import requests


class TestFlow(Node):
    def __init__(self):
        super().__init__('test_flow')

        self.get_logger().info("🧪 FLOW TEST (INSERT + GET)")

        # 1. INSERT
        payload = {
            "tipo_nombre": "Incendio",
            "confianza": 0.95,
            "x": 5,
            "y": 8,
            "descripcion": "FLOW TEST"
        }

        try:
            post = requests.post(
                "http://localhost:3000/api/alerta",
                json=payload,
                timeout=2
            )
            self.get_logger().info(f"INSERT: {post.json()}")

            # 2. GET
            get = requests.get(
                "http://localhost:3000/api/alertas",
                timeout=2
            )
            self.get_logger().info(f"GET: {get.json()}")

        except Exception as e:
            self.get_logger().error(str(e))


def main(args=None):
    rclpy.init(args=args)
    node = TestFlow()
    rclpy.spin_once(node, timeout_sec=1)
    node.destroy_node()
    rclpy.shutdown()