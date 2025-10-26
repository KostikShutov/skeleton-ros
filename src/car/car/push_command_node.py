import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String


class PushCommandNode(Node):
    def __init__(self):
        super().__init__('push_command_node')
        self.publisher_ = self.create_publisher(String, 'commands', 10)
        self.timer = self.create_timer(timer_period_sec=0.5, callback=self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    try:
        with rclpy.init(args=args):
            push_command_node = PushCommandNode()
            rclpy.spin(push_command_node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
