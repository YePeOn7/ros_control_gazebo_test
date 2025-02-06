#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

def shutdown():
    rospy.loginfo("Stopping the robot...")
    pub1.publish(0.0)
    pub2.publish(0.0)
    pub3.publish(0.0)
    rospy.sleep(1)

if __name__ == '__main__':
    try:
      rospy.init_node('test_ros_control', anonymous=True)
      rospy.on_shutdown(shutdown)
      
      # Publishers for wheel velocity
      pub1 = rospy.Publisher('/test_robot/first_wheel_controller/command', Float64, queue_size=10)
      pub2 = rospy.Publisher('/test_robot/second_wheel_controller/command', Float64, queue_size=10)
      pub3 = rospy.Publisher('/test_robot/third_wheel_controller/command', Float64, queue_size=10)
      rate = rospy.Rate(1)  # 10 Hz

      while((pub1.get_num_connections() == 0 or pub2.get_num_connections() == 0 or pub3.get_num_connections() == 0) and not rospy.is_shutdown()):
        rospy.loginfo(f"Waiting for subscriber to connect: {pub1.get_num_connections()}")
        rospy.sleep(0.1)
      print("gooo")

      pub1.publish(3.14/2)
      pub2.publish(3.14/2)
      pub3.publish(3.14/2)
      rospy.sleep(4)

      rospy.signal_shutdown("Shutdown")
    except rospy.ROSInterruptException:
        pass
