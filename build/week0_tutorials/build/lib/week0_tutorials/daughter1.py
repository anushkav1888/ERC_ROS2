import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('Daughter_rover_1')
        self.publisher_ = self.create_publisher(Float32, 'topic_1', 10)
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        msg.data = 23.33
        self.publisher_.publish(msg)
        self.get_logger().info('Published: %f'%(msg.data))

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
