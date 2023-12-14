import rclpy
from rclpy.node import Node
from week0_tutorials.msg import rover_communication  # Update with your actual package name

class RoverStatusPublisher(Node):

    def __init__(self):
        super().__init__('rover_status_publisher')
        self.publisher_ = self.create_publisher(rover_communication, 'rover_status', 10)
        self.timer = self.create_timer(1.0, self.publish_status)
        self.rover_id = 1
        self.battery_level = 90.5
        self.current_location = {'x': 1.0, 'y': 2.0, 'z': 0.0}
        self.health_status = 'Normal'

    def publish_status(self):
        msg = rover_communication()
        msg.rover_id = self.rover_id
        msg.battery_level = self.battery_level
        msg.current_location.position.x = self.current_location['x']
        msg.current_location.position.y = self.current_location['y']
        msg.current_location.position.z = self.current_location['z']
        msg.health_status = self.health_status

        self.publisher_.publish(msg)
        self.get_logger().info('Published RoverStatus: ID=%d, Battery=%f, Location=(%f, %f, %f), Health=%s',
                               msg.rover_id, msg.battery_level,
                               msg.current_location.position.x, msg.current_location.position.y,
                               msg.current_location.position.z, msg.health_status)

def main(args=None):
    rclpy.init(args=args)
    rover_status_publisher = RoverStatusPublisher()
    rclpy.spin(rover_status_publisher)
    rover_status_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
