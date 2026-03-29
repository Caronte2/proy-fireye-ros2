import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf_transformations import quaternion_from_euler

class InitialPosePublisher(Node):
    def __init__(self):
        super().__init__('initial_pose_publisher')
        self.publisher_ = self.create_publisher(PoseWithCovarianceStamped, '/initialpose', 10)

        # Publica cada vez que se lanza el nodo
        self.publish_initial_pose()

    def publish_initial_pose(self):
        msg = PoseWithCovarianceStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'map'  # Muy importante que sea 'map'

        # Posición inicial del robot
        msg.pose.pose.position.x = 0.0  # Cambia según tu mapa
        msg.pose.pose.position.y = 0.0
        msg.pose.pose.position.z = 0.0

        # Orientación inicial (en radianes)
        yaw = 0.0  # Cambia según hacia donde quieras que mire el robot
        q = quaternion_from_euler(0, 0, yaw)
        msg.pose.pose.orientation.x = q[0]
        msg.pose.pose.orientation.y = q[1]
        msg.pose.pose.orientation.z = q[2]
        msg.pose.pose.orientation.w = q[3]

        # Covarianza (puedes usar valores por defecto)
        msg.pose.covariance = [0.0]*36

        self.publisher_.publish(msg)
        self.get_logger().info(f'Published initial pose: x={msg.pose.pose.position.x}, y={msg.pose.pose.position.y}, yaw={yaw}')

def main(args=None):
    rclpy.init(args=args)
    node = InitialPosePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()