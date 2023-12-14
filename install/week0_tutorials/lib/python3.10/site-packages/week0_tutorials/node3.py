import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('Basestation')
        self.a = None
        self.b = None

        self.subscription1 = self.create_subscription(
            String,
            'topic_1',
            self.listener_callback1,
            10)
        self.subscription2 = self.create_subscription(
            String,
            'topic_2',
            self.listener_callback2,
            10)
        self.subscription2 = self.create_subscription(
            String,
            'topic_3',
            self.listener_callback3,
            10)


    def listener_callback1(self, msg):
        self.a = msg.data
        self.process_and_log_result()

    def listener_callback2(self, msg):
        self.b = msg.data
        self.process_and_log_result()
    def listener_callback3(self, msg):
        self.b = msg.data
        self.process_and_log_result()
    def process_and_log_result(self):
        if self.a is not None and self.b is not None:
            result = self.a + self.b
            self.get_logger().info(result)
            # Reset the values to None for the next iteration
            self.a = None
            self.b = None

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
