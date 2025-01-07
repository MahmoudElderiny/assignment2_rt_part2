import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.move_robot)
        self.counter = 0

    def move_robot(self):
        msg = Twist()
        if self.counter < 20:
            # Move forward
            msg.linear.x = 0.5
            msg.angular.z = 0.0
        elif self.counter < 40:
            # Rotate
            msg.linear.x = 0.0
            msg.angular.z = 0.5
        else:
            # Reset counter
            self.counter = 0
        self.publisher_.publish(msg)
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

