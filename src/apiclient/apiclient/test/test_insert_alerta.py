## ros2 run apiclient test_insert_alerta
import rclpy
from rclpy.node import Node
import requests


class TestInsertAlerta(Node):
    def __init__(self):
        super().__init__('test_insert_alerta')

        self.get_logger().info("🧪 INSERT ALERTA TEST")

        payload = {
            "tipo_nombre": "Incendio",
            "confianza": 0.92,
            "x": 10,
            "y": 20,
            "descripcion": "TEST INSERT ROS2"
        }

        try:
            res = requests.post("http://localhost:3000/api/alerta", json=payload, timeout=2)
            self.get_logger().info(f"RESPUESTA: {res.json()}")
        except Exception as e:
            self.get_logger().error(str(e))


def main(args=None):
    rclpy.init(args=args)
    node = TestInsertAlerta()
    rclpy.spin_once(node, timeout_sec=1)
    node.destroy_node()
    rclpy.shutdown()