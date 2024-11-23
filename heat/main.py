import os
import rclpy
from . import heater
from rclpy.node import Node
from std_msgs.msg import Float32

TARGET_TEMP = int(os.getenv('TARGET_TEMP',20))
PIN = int(os.getenv('PIN',12))

class Heat(Node):

    def __init__(self):
        super().__init__('heat')
        self.heater = heater.Heater(PIN)
        
        self.subscription = self.create_subscription(
            Float32,
            'temp',
            self.listener_callback,
            10)

    def listener_callback(self, msg):

        temp = msg.data
        self.get_logger().info('Current temp: "%.2f"' % temp)
        
        if temp < TARGET_TEMP:
            self.get_logger().info('Turning on heat')
            self.heater.on()
        else:
            self.get_logger().info('Turning off heat')
            self.heater.off()


def main(args=None):
    rclpy.init(args=args)

    heat_subscriber = Heat()

    rclpy.spin(heat_subscriber)

    heat_subscriber.heater.shutdown()
    heat_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()