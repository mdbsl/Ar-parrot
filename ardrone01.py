
#!/usr/bin/env python
import rospy
import sys
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist

def move(speed=0.0, distance=0.0, type='u'):
    vel_msg = Twist()

    #Since we are moving just in x-axis
    
    #Since we are moving just in x-axis
    vel_msg.linear.x = 0.0
    vel_msg.linear.y = 0.0
    vel_msg.linear.z = 0.0

    vel_msg.angular.x = 0.0
    vel_msg.angular.y = 0.0
    vel_msg.angular.z = 0.0


    if (type == 'f'):
        vel_msg.linear.x = speed       
    elif (type == 'b'):
        vel_msg.linear.x = -abs(speed) 
    if (type == 'u'):
        vel_msg.linear.z = speed       
    elif (type == 'd'):
        vel_msg.linear.z = -abs(speed)        
    elif (type == 'r'):
        vel_msg.linear.y = -abs(speed)         
    elif (type == 'l'):
        vel_msg.linear.y = speed
    elif (type == 'rr'):
        vel_msg.angular.z = -abs(speed)        
    elif (type == 'rl'):
        vel_msg.angular.z = speed

    #while not rospy.is_shutdown():

        #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0

    #Loop to move the turtle in an specified distance
    while(current_distance < distance):
        #Publish the velocity
        velocity_pub.publish(vel_msg)
        #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
        #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
        #rospy.sleep(2)
        #Force the robot to stop
    stop()


def takeoff():    
    takeoff_pub.publish(Empty())
    stop()

def land():    
    land_pub.publish(Empty())
    
def stop(): 
    twist = Twist()  
    twist.linear.x=0.0
    twist.linear.y=0.0
    twist.angular.z=0.0 
    velocity_pub.publish(twist)

def recorrido(vel):
    #takeoff()
    #print('SUBIR')
    #move(vel, 0.1, 'u')
    #print('DERECHA')
    #move(vel, 0.1, 'r')
    #print('BAJAR')
    #move(vel, 0.1, 'd')
    #print('IZQUIERDA')
    #move(vel, 0.1, 'l')
    #print('SUBIR')
    #move(vel, 0.1, 'u')
    #print('ATERRIZAR')
    #land()
    #stop()

    takeoff()
    print('SUBIR')
    move(vel, 4, 'u')
    print('GIRO DERECHA')
    move(vel, 1.7, 'rr')
    print('RECTO')
    move(vel, 2, 'f')
    print('GIRO DERECHA')
    move(vel, 1.7, 'rr')
    print('RECTO')
    move(vel, 2, 'f')
    print('GIRO DERECHA')
    move(vel, 1.7, 'rr')  
    print('RECTO')
    move(vel, 2, 'f')      
    print('GIRO DERECHA')
    move(vel, 1.7, 'rr')  
    print('RECTO')
    move(vel, 2, 'f')        
    print('ATERRIZAR')
    land()

def menu():

    print ("1: TAKEOFF")
    print ("0: STOP")
    print ("2: arriba")
    print ("3: abajo")
    print ("4: derecha")
    print ("5: izquierda")
    print ("6: Rotar derecha")
    print ("7: Rotar izquierda")
    print ("9: LAND")  
    print ("a: ADELANTE")
    print ("b: ATRAS")    
    print ("R: RECORRIDO")     



if __name__ == '__main__':
    rospy.init_node('ardrone_control_node', anonymous=True)
    takeoff_pub = rospy.Publisher("/ardrone/takeoff", Empty, queue_size=10 )
    land_pub = rospy.Publisher("ardrone/land", Empty, queue_size=10 )
    velocity_pub = rospy.Publisher("cmd_vel", Twist, queue_size=10 )
    #rate = rospy.Rate(10) # 10hz
    vel = 0.1
    try:
        while not rospy.is_shutdown():
            menu()
            #key= input("press a key for action")
            key=sys.stdin.read(1)
            if (key == str('1')):
                takeoff()
            elif (key == str('9')):
                land()
            elif (key == str('0')):
                stop()
            elif (key == str('2')):
                move(vel, 0.1, 'u')
            elif (key == str('3')):
                move(vel, 0.1, 'd')
            elif (key == str('4')):
                move(vel, 0.1, 'r')                
            elif (key == str('5')):
                move(vel, 0.1, 'l')
            elif (key == str('6')):
                move(vel, 0.1, 'rr')                
            elif (key == str('7')):
                move(vel, 0.1, 'rl')
            elif (key == str('a')):
                move(vel, 0.1, 'f')
            elif (key == str('b')):
                move(vel, 0.1, 'b')           
            elif (key == str('R')):
                recorrido(vel)   

    except rospy.ROSInterruptException:
        pass