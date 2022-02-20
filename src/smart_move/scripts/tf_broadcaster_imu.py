#!/usr/bin/env python  
## By Ayush Ghosh
import rospy
import tf_conversions
import tf2_ros
import geometry_msgs.msg
from sensor_msgs.msg import Temperature, Imu
from tf.transformations import euler_from_quaternion, quaternion_from_euler

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

    (roll, pitch, yaw) = euler_from_quaternion ([
        msg.orientation.x,
        msg.orientation.y,
        msg.orientation.z,
        msg.orientation.w])
    print ("roll:", roll, " pitch:", pitch)
    q = quaternion_from_euler(roll, pitch, 0)
    t.transform.rotation.x = msg.orientation.x
    t.transform.rotation.y = msg.orientation.y
    t.transform.rotation.z = msg.orientation.z
    t.transform.rotation.w = msg.orientation.w

    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    br.sendTransform(t)

if __name__ == '__main__':
      rospy.init_node('tf_broadcaster_imu')
      rospy.Subscriber('/imu/data', Imu, handle_imu_pose)
      rospy.spin()
