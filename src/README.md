# Smart Move Project
By Ayush Ghosh for Calgary Hacks 2022

Source code for a cheap, portable wearable device that acts as your virtual physiotherapist!

## Running project for the First Time:
Ensure ROS is installed on both RPi and Ubuntu desktop.

Clone this repo on both RPi and Ubuntu Desktop.

### On Rpi: 
Run the command `roslaunch mpu_6050_driver imu_demo.launch` followed by `python ~/calgary_ws/src/smart_move/scripts/marker_pub.py`. Follow the instructions [here](https://smallbusiness.chron.com/run-command-startup-linux-27796.html) to get the previous 2 commands to run on startup.

### On Desktop:
Move the file `SmartMove.desktop` and place it in `/usr/local/share/applications/` to allow for the app to show up in the app launcher.


