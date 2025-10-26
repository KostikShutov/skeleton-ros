import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String


class ExecuteCommandNode(Node):
    def __init__(self):
        super().__init__('execute_command_node')
        self.subscription = self.create_subscription(String, 'commands', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    try:
        with rclpy.init(args=args):
            execute_command_node = ExecuteCommandNode()
            rclpy.spin(execute_command_node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
