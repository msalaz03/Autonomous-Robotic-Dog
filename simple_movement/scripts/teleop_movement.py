# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import rclpy #ros client library for python
from rclpy.node import Node #import nodes
from geometry_msgs.msg import Twist #from the geometry library import variables: linear and angular
from sensor_msgs.msg import Joy #this is importing the controller dependencies
from geometry_msgs.msg import Pose as Pose #create our msg type of pose


#object-oriented programming approach:
class Teleop(Node):

    def __init__ (self): #init our class
        super().__init__('Clifford_Controller_KB') #create the parent class
        self.get_logger().info('Publisher Online') #logging for status

        #here is our declaration of what we should for the dog
        self.clifford_pub_sit = self.create_publisher(Pose, 'sit_pose', 1) #defining our publisher and the node
        self.clifford_pub_idle = self.create_publisher(Pose, 'idle_pose', 1) #define our pub and msg: pose
        self.clifford_pub_velocity = self.create_publisher(Twist, 'cmd_vel',1)
        
        #before send out the velcoity commands we want to translate what the controller is sending us
        self.joy_sub = self.create_subscription(Joy, 'joy', self.joy_callback, 1) #this call back is necessary to make sure we're constantly updating our values

        #This could be in handy if need to adjust some necessary things before the robot is launched
        #self.declare_parameter("parameters needed", default value) declaring parameters
        #self.my_parameter = self.get_parameter("parameters needed")


        """
        Reading from the keyboard  and Publishing to Twist!
        ---------------------------
        Moving around:
        u    i    o
        j    k    l
        m    ,    .
        For Holonomic mode (strafing), hold down the shift key:
        ---------------------------
        U    I    O
        J    K    L
        M    <    >
        t : up (+z)
        b : down (-z)
        anything else : stop
        q/z : increase/decrease max speeds by 10%
        w/x : increase/decrease only linear speed by 10%
        e/c : increase/decrease only angular speed by 10%
        CTRL-C to quit
        """

        #create a dictionary to define what each key is doing in their 
        self.velocityBindings = {
                'i':(1,0,0,0),  #x,y,z_linear and angular.
                'o':(1,0,0,-1),
                'j':(0,0,0,1),
                'l':(0,0,0,-1),
                'u':(1,0,0,1),
                ',':(-1,0,0,0),
                '.':(-1,0,0,1),
                'm':(-1,0,0,-1),
                'O':(1,-1,0,0),
                'I':(1,0,0,0),
                'J':(0,1,0,0),
                'L':(0,-1,0,0),
                'U':(1,1,0,0),
                '<':(-1,0,0,0),
                '>':(-1,-1,0,0),
                'M':(-1,1,0,0),
                'v':(0,0,1,0),
                'n':(0,0,-1,0),
            }

        self.poseBindings = {
                'f':(-1,0,0,0),
                'h':(1,0,0,0),
                't':(0,1,0,0),
                'b':(0,-1,0,0),
                'r':(0,0,1,0),
                'y':(0,0,-1,0),
            }

        self.speedBindings={
                'q':(1.1,1.1),
                'z':(.9,.9),
                'w':(1.1,1),
                'x':(.9,1),
                'e':(1,1.1),
                'c':(1,.9),
            }
        
        self.poll_keys()

    def joy_callback(self,data):
        twist = Twist() #now we have access to joy which sends information to cmd_vel/ topic
        #our calculations here
    

    def joy_buttons(self,buttons):
        if buttons == 0:
            print("passed")
        else:
            print("hello")
        
    
        
#look more into this
def main(args=None):
    rclpy.init(args=args)

#execute our main
if __name__ == '__main__':
    rclpy.init()
    teleop = Teleop()
