#!/usr/bin/python
## By Ayush Ghosh
#import rospy
#from visualization_msgs.msg import Marker
#
#rospy.init_node('ellipse', anonymous=True)
#publisher = rospy.Publisher("ellipse", Marker)
#count = 0
#while not rospy.is_shutdown():
#    ellipse = Marker()
#    ellipse.header.frame_id = "plane"
#    ellipse.header.stamp = rospy.Time.now()
#    ellipse.type = Marker.CUBE
#    ellipse.pose.position.x = 0
#    ellipse.pose.position.y = 0
#    ellipse.pose.position.z = -3
#    ellipse.pose.orientation.x = 0
#    ellipse.pose.orientation.y = 0
#    ellipse.pose.orientation.z = 0
#    ellipse.pose.orientation.w = 1
#    ellipse.scale.x = 0.5
#    ellipse.scale.y = 0.5
#    ellipse.scale.z = 0.5
#    ellipse.color.a = 1.0
#    ellipse.color.r = 1.0
#    ellipse.color.g = 0.0
#    ellipse.color.b = 0.0
#
#    # Publish the MarkerArray
#    publisher.publish(ellipse)
#
#    rospy.sleep(0.01)
#
##!/usr/bin/env python  
import rospy
from visualization_msgs.msg import Marker
from tf.transformations import euler_from_quaternion, quaternion_from_euler
#import geometry_msgs.msg
from sensor_msgs.msg import Temperature, Imu

roll = 0
pitch = 0
yaw = 0
marker_down_found = False
marker_up_found = False
marker_left_found = False
marker_right_found = False

down_counter = 0
up_counter = 0
right_counter = 0
left_counter = 0

up_complete = False
down_complete = False

def arrow ():

    ellipse = Marker()
    ellipse.header.frame_id = "imu_link"
    ellipse.header.stamp = rospy.Time.now()
    ellipse.type = Marker.ARROW
    ellipse.pose.position.x = 1
    ellipse.pose.position.y = 0
    ellipse.pose.position.z = 0
    ellipse.pose.orientation.x = 0
    ellipse.pose.orientation.y = 0
    ellipse.pose.orientation.z = 0
    ellipse.pose.orientation.w = 1
    ellipse.scale.x = 40
    ellipse.scale.y = 0.06
    ellipse.scale.z = 0.05

    
    ellipse.color.a = 1.0
    ellipse.color.r = 0.5
    ellipse.color.g = 1.0
    ellipse.color.b = 0.5
    
    # Publish the MarkerArray
    publisher4.publish(ellipse)

def text ():

    ellipse = Marker()
    ellipse.header.frame_id = "imu_link"
    ellipse.header.stamp = rospy.Time.now()
    ellipse.type = Marker.TEXT_VIEW_FACING
    ellipse.pose.position.x = 1
    ellipse.pose.position.y = 0
    ellipse.pose.position.z = 2.5
    ellipse.pose.orientation.x = 0
    ellipse.pose.orientation.y = 0
    ellipse.pose.orientation.z = 0
    ellipse.pose.orientation.w = 1

    ellipse.scale.x = 0.15
    ellipse.scale.y = 0.15
    ellipse.scale.z = 0.15

    
    ellipse.color.a = 1.0
    ellipse.color.r = 1.0
    ellipse.color.g = 1.0
    ellipse.color.b = 1.0
    
    
    ellipse.text = "Welcome to your daily wrist excercise! \nPlease move your wirst to the top and find the upper target!"

    if down_complete and up_complete and marker_left_found and marker_right_found:
        ellipse.text = "Congratulations! You have successfully completed the wrist excerise!"
    
    elif marker_left_found == True and down_complete:
        ellipse.text = "You are almost there! Now please point your wrist forward and twist to the right"
    
    elif down_complete == True:
        ellipse.text = "Wonderful! Now please point your wrist forward and twist to the left. \nMake sure you are still aiming for the target :)"
    
    elif up_complete == True:
        ellipse.text = "Awesome! Now please point your wrist to the bottom and find the lower target"
    

    # Publish the MarkerArray
    publisher5.publish(ellipse)

def down_marker ():
    global down_counter, down_complete

    ellipse = Marker()
    ellipse.header.frame_id = "plane"
    ellipse.header.stamp = rospy.Time.now()
    ellipse.type = Marker.CUBE
    ellipse.pose.position.x = 30
    ellipse.pose.position.y = 0
    ellipse.pose.position.z = -30

    
    ellipse.pose.orientation.x = 0
    ellipse.pose.orientation.y = 0
    ellipse.pose.orientation.z = 0
    ellipse.pose.orientation.w = 1
    q = quaternion_from_euler(0, 0, yaw)
    #ellipse.pose.orientation.x = q[0]
    #ellipse.pose.orientation.y = q[1]
    #ellipse.pose.orientation.z = q[2]
    #ellipse.pose.orientation.w = q[3]
    ellipse.scale.x = 0.5
    ellipse.scale.y = 2.0
    ellipse.scale.z = 0.5

    
    ellipse.color.a = 1.0
    ellipse.color.r = 1.0
    ellipse.color.g = 0.0
    ellipse.color.b = 0.0

    if marker_down_found == True:
        ellipse.color.a = 1.0
        ellipse.color.r = 0.5
        ellipse.color.g = 0.0
        ellipse.color.b = 0.5
        down_counter += 1


    if (marker_down_found == True) and (down_counter > 100):
        ellipse.color.a = 1.0
        ellipse.color.r = 0.0
        ellipse.color.g = 1.0
        ellipse.color.b = 0.0
        down_complete = True
    
    # Publish the MarkerArray
    publisher.publish(ellipse)

def up_marker ():
    global up_counter, up_complete
    ellipse = Marker()
    ellipse.header.frame_id = "plane"
    ellipse.header.stamp = rospy.Time.now()
    ellipse.type = Marker.CUBE
    ellipse.pose.position.x = 10
    ellipse.pose.position.y = 0
    ellipse.pose.position.z = 30
    ellipse.pose.orientation.x = 0
    ellipse.pose.orientation.y = 0
    ellipse.pose.orientation.z = 0
    ellipse.pose.orientation.w = 1
    q = quaternion_from_euler(0, 0, yaw)
    #ellipse.pose.orientation.x = q[0]
    #ellipse.pose.orientation.y = q[1]
    #ellipse.pose.orientation.z = q[2]
    #ellipse.pose.orientation.w = q[3]
    ellipse.scale.x = 0.5
    ellipse.scale.y = 2.0
    ellipse.scale.z = 0.5

    
    ellipse.color.a = 1.0
    ellipse.color.r = 1.0
    ellipse.color.g = 0.0
    ellipse.color.b = 0.0

    if marker_up_found == True:
        ellipse.color.a = 1.0
        ellipse.color.r = 0.5
        ellipse.color.g = 0.0
        ellipse.color.b = 0.5
        up_counter += 1


    if (marker_up_found == True) and (up_counter > 100):
        ellipse.color.a = 1.0
        ellipse.color.r = 0.0
        ellipse.color.g = 1.0
        ellipse.color.b = 0.0
        up_complete = True

    # Publish the MarkerArray
    publisher2.publish(ellipse)

def front_marker ():
    ellipse = Marker()
    ellipse.header.frame_id = "plane"
    ellipse.header.stamp = rospy.Time.now()
    ellipse.type = Marker.CUBE
    ellipse.pose.position.x = 20
    ellipse.pose.position.y = 0
    ellipse.pose.position.z = 0
    ellipse.pose.orientation.x = 0
    ellipse.pose.orientation.y = 0
    ellipse.pose.orientation.z = 0
    ellipse.pose.orientation.w = 1
    q = quaternion_from_euler(0, 0, yaw)
    #ellipse.pose.orientation.x = q[0]
    #ellipse.pose.orientation.y = q[1]
    #ellipse.pose.orientation.z = q[2]
    #ellipse.pose.orientation.w = q[3]
    
    ellipse.scale.x = 0.5
    ellipse.scale.y = 2.0
    ellipse.scale.z = 0.5

    
    ellipse.color.a = 1.0
    ellipse.color.r = 1.0
    ellipse.color.g = 0.0
    ellipse.color.b = 0.0
    
    if (marker_left_found == True) and (marker_right_found == True):
        ellipse.color.a = 1.0
        ellipse.color.r = 0.0
        ellipse.color.g = 1.0
        ellipse.color.b = 0.0


    elif marker_left_found == True:
        ellipse.color.a = 1.0
        ellipse.color.r = 1.0
        ellipse.color.g = 1.0
        ellipse.color.b = 0.0
    
    elif marker_right_found == True:
        ellipse.color.a = 1.0
        ellipse.color.r = 0.0
        ellipse.color.g = 0.0
        ellipse.color.b = 1.0

    # Publish the MarkerArray
    publisher3.publish(ellipse)


def handle_imu_pose(msg):
    global roll, pitch, yaw, marker_up_found, marker_down_found, marker_left_found, marker_right_found
    
    
    (roll, pitch, yaw) = euler_from_quaternion ([
        msg.orientation.x,
        msg.orientation.y,
        msg.orientation.z,
        msg.orientation.w])

    if pitch > 0.67:
        marker_down_found = True
    
    if pitch < -1.3:
        marker_up_found = True

    if roll > 1.3:
        marker_right_found = True

    if roll < -1.0:
        marker_left_found = True

    down_marker()
    up_marker()
    front_marker()
    arrow()
    text()
    #print("roll:", roll, " pitch:", pitch, " yaw:", yaw)

    

if __name__ == '__main__':
      rospy.init_node('marker_node')
      publisher = rospy.Publisher("cube_down", Marker)
      publisher2 = rospy.Publisher("cube_up", Marker)
      publisher3 = rospy.Publisher("cube_front", Marker)
      publisher4 = rospy.Publisher("arrow", Marker)
      publisher5 = rospy.Publisher("text", Marker)
      rospy.Subscriber('/imu/data_raw', Imu, handle_imu_pose)
#      talker()
      rospy.spin()
