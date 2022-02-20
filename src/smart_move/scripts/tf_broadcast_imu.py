#!/usr/bin/env python  
## By Ayush Ghosh
import rospy
import tf_conversions
import tf2_ros
import geometry_msgs.msg
from sensor_msgs.msg import Temperature, Imu

from std_msgs.msg import String
def talker():
    pub = rospy.Publisher('talker', String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        msg = "hello test %s" % rospy.get_time()
        print("Sending talker msg")
        pub.publish(msg)
        rate.sleep()

def handle_imu_pose(msg):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "plane"
    t.child_frame_id = "imu_link"
    t.transform.translation.x = 0
    t.transform.translation.y = 0
    t.transform.translation.z = 0
    t.transform.rotation.x = msg.orientation.x
    t.transform.rotation.y = msg.orientation.y
    t.transform.rotation.z = msg.orientation.z
    t.transform.rotation.w = msg.orientation.w

    br.sendTransform(t)

if __name__ == '__main__':
      rospy.init_node('tf_broadcaster_imu')
      rospy.Subscriber('/imu/data_raw', Imu, handle_imu_pose)
#      talker()
      rospy.spin()
