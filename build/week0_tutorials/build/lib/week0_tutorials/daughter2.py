import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('Daughter_rover_2')
        self.publisher_ = self.create_publisher(Point, 'topic_2', 10)
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Point()
        msg.x = 9.2
        msg.y = 38.9
        msg.z = 0.9
        self.publisher_.publish(msg)
        self.get_logger().info('Published: x=%f, y=%f, z=%f' % (msg.x, msg.y, msg.z))

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
