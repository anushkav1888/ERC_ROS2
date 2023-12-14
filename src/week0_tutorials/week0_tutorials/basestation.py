import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String
from geometry_msgs.msg import Point
from week0_tutorials.msg import RoverStatus  # Update with your actual package name

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('Basestation')
        self.a = None
        self.b = None
        self.c = None

        # Add a subscriber to the RoverStatus topic
        self.rover_status_subscription = self.create_subscription(
            RoverStatus,
            'rover_status',
            self.rover_status_callback,
            10)

        self.subscription1 = self.create_subscription(
            Float32,
            'topic_1',
            self.listener_callback1,
            10)
        self.subscription2 = self.create_subscription(
            Point,
            'topic_2',
            self.listener_callback2,
            10)
        self.subscription3 = self.create_subscription(
            String,
            'topic_3',
            self.listener_callback3,
            10)

    def listener_callback1(self, msg):
        self.get_logger().info('Pressure reported is %f', msg.data)

    def listener_callback2(self, msg):
        self.get_logger().info('Received Point: x={}, y={}, z={}'.format(msg.x, msg.y, msg.z))

    def listener_callback3(self, msg):
        self.c = msg.data
        self.process_and_log_result(self.c)

    def rover_status_callback(self, msg):
        self.get_logger().info('Received RoverStatus: ID=%d, Battery=%f, Location=(%f, %f, %f), Health=%s',
                               msg.rover_id, msg.battery_level,
                               msg.current_location.position.x, msg.current_location.position.y,
                               msg.current_location.position.z, msg.health_status)

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
