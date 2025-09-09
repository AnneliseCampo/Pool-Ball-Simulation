#PHYS 261 - FINAL PROJECT - SIMULATION OF TWO POOL BALLS
#FINAL VERSION FOR SUBMISSION
#BY ANNELISE CAMPO AND LUIS VASQUEZ
from numpy import *
from random import *
from matplotlib.pyplot import *

x_initial = randrange(20,180,1)/100 #finds random initial position of 1st ball
y_initial = randrange(20,80,1)/100

x_initial2 = randrange(20,180,1)/100 #finds random initial position of 2nd ball
y_initial2 = randrange(20,80,1)/100  

#constants:

mu_static = 0.006   #coefficient of friction of the pool ball on a pool table
mass = 0.17         #The mass of the pool ball
t_of_contact = 0.001#Time of contact of the ball (impulse momentum theory)
g = 9.8             # m/s**2
radius = 0.06       #m
d_of_hole = 0.05    #(m) diameter of table's pockets


ptl1 = 0            #Limiters for the pocket,prevents infinite loop
ptm1 = 0            #if one ball falls in pocket and other does not, these 
ptr1 = 0            #prevent program from printing 'congrats' repetitively
pbl1 = 0
pbm1 = 0
pbr1 = 0

ptl2 = 0
ptm2 = 0
ptr2 = 0
pbl2 = 0
pbm2 = 0
pbr2 = 0 

markersize = 1100   #constants for shapes/sizes of graph elements
ballgraphsize = 250

#-------------------------------------------------------------------------------

#plotting a representation of a pool table, with both balls' initial positions

ax = axes()         #creates the 'ax' object, of the 'axes' class from matplotlib prackage

Holes_x_position = [0,0,1,1,2,2]        #establishes the positions of the pockets
Holes_y_position = [0,1,0,1,0,1]

scatter(Holes_x_position, Holes_y_position, markersize, 'k') 

ax.set_facecolor("green")#sets background graph color to green, using 'set_facecolor', a method of the 'ax' object

scatter(x_initial, y_initial, ballgraphsize, 'w')#plots initial position 1st ball
scatter(x_initial2, y_initial2, ballgraphsize, 'r')#initial pos. 2nd ball

title("The Pool Table", fontsize=25)    #titles the graph

ax.set_xlabel('x (m)')                         #labels axes using methods of ax object
ax.set_ylabel('y (m)')
xlim(-0.02,2.02)                        #establishes domain and range of graph
ylim(-0.02,1.02)

print("Here's the initial position of the first ball:")
print(array([x_initial, y_initial]))    #shows user inital position of the 1st ball
print("Here's the initial position of the second ball:")
print(array([x_initial2,y_initial2]))   #shows user inital position of the 2nd ball

show()     

#-------------------------------------------------------------------------------

lim = 0
while lim == 0 :        #this variable 'lim' is only here to continue the loop
    
    print ('Input a force between 0 and 150 (N) and direction/angle in Degrees:')

    Force = float(input())
    
    direction = pi * float(input()) / 180
                        #converts the inputted angle that is degrees to radians
    if Force >= 0 and Force <= 150:
            #tests force, determines if resonable/(if positive and not too big)
        break 

    else:

        print('Your force is not in the range of accepted values.')

#------------------------------------------------------------------------------

Force_friction =  mass*mu_static*g 
Fnet = Force_friction       #N Force of friction is only constant force affecting balls during motion

Fnetx = Fnet*cos(direction) #N   x comp of Force
Fnety = Fnet*sin(direction) #N   y comp of Force

accel = mu_static * g

accelx = -Fnetx/mass        #m/s**2   x comp of acceleration
accely = -Fnety/mass        #m/s**2   x comp of acceleration (negative bc friction is decreasing ball speed)

a1 = array([accelx,accely]) #acceleration of 1st ball is constant
a2 = array([0.0,0.0])       #initial acceleration of the 2nd ball

vi = Force * t_of_contact / mass #Impulse momentum theorem
    #magnitude of initial velocity, based on inital applied(inputted)
    #force, treated as an impulse bc it's applied once over short duration of time

v1x_initial = vi * cos(direction) #x-component initial velocity of 1st ball
v1y_initial = vi * sin(direction) #y-component

v1 = array([v1x_initial , v1y_initial])#arrays are created with the initial   
v2 = array([0.0 , 0.0])                    #velocities of either ball, but will
                                         #change as the balls' velocities change

t = 0.01        #this is the constant time interval at which the loop will repetitovely test the ball's position(and other properties)

r1 = array([x_initial + v1[0] *t , y_initial + v1[1] *t])
                            #creates array of initial position of the 1st ball
r2 = array([x_initial2 , y_initial2])
                            #creates array of initial position of the 2nd ball

#-------------------------------------------------------------------------------

r1x_plot=[] #these lists will be populated with positional data consisting of
r1y_plot=[] #the x and y components of the positons of each ball to be used 
r2x_plot=[] #later to plot the balls' paths
r2y_plot=[]

epsilon = 0.01  #Represents small value so that we can confirm that the magnitude of velocity is approaching/practically ZERO

limit = 0

while linalg.norm(v1) > epsilon or linalg.norm(v2) > epsilon:
        #This will be the ultimate while loop that keeps track of the poition of the pool balls 
        #requires magnitude of v1 to be > small number 'epsilon' (to confirm the ball is still moving) in order for the loop to continue
    
    if linalg.norm(v1) != 0: #as long as 1st ball is still moving, acceleration
                             #will always have direction opposite of its veloocity
        a1x = -abs(accel) * v1[0] / linalg.norm(v1) #separates it component wise
        a1y = -abs(accel) * v1[1] / linalg.norm(v1) 

        a1 = array([ a1x , a1y]) #puts components in vector/array

    if linalg.norm(v2) != 0:  #same process but for 2nd ball

        a2x = -abs(accel) * v2[0] / linalg.norm(v2)
        a2y = -abs(accel) * v2[1] / linalg.norm(v2)

        a2 = array([a2x , a2y])

        
    v1[0] = v1[0] + a1[0] * t #these allow the program to handle the change
    v1[1] = v1[1] + a1[1] * t #in velocity in relation to acceleration and
                #takes note of it every cycle of small interval of time: 't'
    
    v2[0] = v2[0] + a2[0] * t  #repeated for the second ball's velocity
    v2[1] = v2[1] + a2[1] * t

    r1 = array([r1[0] + v1[0] * t, r1[1] + v1[1] * t])
    r2 = array([r2[0] + v2[0] * t, r2[1] + v2[1] * t])
            #similar to velocity, these allow program to take note of position
            #of either ball at every cycle of the very small time: 't'

    r1x_plot.append(r1[0])      #populates the lists to be used in graphing 
    r1y_plot.append(r1[1])      #the balls' paths
    r2x_plot.append(r2[0])
    r2y_plot.append(r2[1])

    #------------------------------------------------------------------------
    #depending on position vectors r1 and r2 for the balls, the following
    #repetitive lines analyze whether either ball falls in a pocket
    #there is a set of code for each pocket for each ball 

    if r1[0] >= 0 and r1[0] <= 0 + d_of_hole and r1[1] >= 1 - d_of_hole and r1[1] <= 1 and ptl1 == 0: #Top left pocket 
                #goes through all the parameters needed specifying that 1st ball is within the range of
                #this sepecific pocket's diameter based on both its x and y coordinates
        print('GREAT JOB! You made the cue ball into the top left pocket')
        
        v1 = array([0.0,0.0]) #specifies if the ball falls in pocket, its velocity becomes zero
        ptl1 = 1 #if above code is satified, this breaks the loop

                 #the rest have almost the same code, the only variations being:
                 #parameters of each of the different pockets, and first 6 sections are for 1st ball, the rest are for 2nd ball
        
    if r1[0] >= 2 - d_of_hole and r1[0] <= 2 and r1[1] >= 1 - d_of_hole and r1[1] <= 1 and ptr1 == 0: #Top right 
        print('GREAT JOB! You made the cue ball into the top right pocket')
        
        v1 = array([0.0,0.0])
        ptr1 = 1

    if r1[0] >= 0 and r1[0] <= 0 + d_of_hole and r1[1] >= 0 and r1[1] <= 0 + d_of_hole and pbl1 == 0: #Bottom Left  
        print('GREAT JOB! You made the cue ball into the bottom left')
        
        v1 = array([0.0,0.0])
        pbl1 = 1

    if r1[0] >= 2 - d_of_hole and r1[0] <= 2 and r1[1] >= 0 and r1[1] <= 0 + d_of_hole and pbr1 == 0: #Bottom right 
        print('GREAT JOB! You made the cue ball into the bottom right pocket')

        v1 = array([0.0,0.0])
        pbr1 = 1

    if r1[0] >= 1 - d_of_hole  and r1[0] <= 1 + d_of_hole and r1[1] >= 1 - d_of_hole and r1[1] <= 1 and ptm1 == 0: #Upper Middle 
        print('GREAT JOB! You made the cue ball into the upper middle pocket')

        v1 = array([0.0,0.0])
        ptm1 = 1

    if r1[0] >= 1 - d_of_hole  and r1[0] <= 1 + d_of_hole and r1[1] >= 0 and r1[1] <= 0 + d_of_hole and pbm1 == 0: #Lower Middle  
        print('GREAT JOB! You made the cue ball into the lower middle pocket')

        v1 = array([0.0,0.0])
        pbm1 = 1

    #below is the same code as above but for the 2nd ball
    
    if r2[0] >= 0 and r2[0] <= 0 + d_of_hole and r2[1] >= 1 - d_of_hole and r2[1] <= 1 and ptl2 == 0: #Top left pocket 
        print('GREAT JOB! You made the Red ball into the top left pocket')

        v2 = array([0.0,0.0])
        ptl2 = 1
        
    if r2[0] >= 2 - d_of_hole and r2[0] <= 2 and r2[1] >= 1 - d_of_hole and r2[1] <= 1 and ptr2 == 0: #Top right 
        print('GREAT JOB! You made the Red ball into the top right pocket')

        v2 = array([0.0,0.0])
        ptr2 = 1
        
    if r2[0] >= 0 and r2[0] <= 0 + d_of_hole and r2[1] >= 0 and r2[1] <= 0 + d_of_hole and pbl2 == 0: #Bottom Left  
        print('GREAT JOB! You made the Red ball into the bottom left pocket')

        v2 = array([0.0,0.0])
        pbl2 = 1

    if r2[0] >= 2 - d_of_hole and r2[0] <= 2 and r2[1] >= 0 and r2[1] <= 0 + d_of_hole and pbr2 == 0: #Bottom right 
        print('GREAT JOB! You made the Red ball into the bottom right pocket')

        v2 = array([0.0,0.0])
        pbr2 = 1

    if r2[0] >= 1 - d_of_hole  and r2[0] <= 1 + d_of_hole and r2[1] >= 1 - d_of_hole and r2[1] <= 1 and ptm2 == 0: #Upper Middle 
        print('GREAT JOB! You made the Red ball into the upper middle pocket')

        v2 = array([0.0,0.0])
        ptm2 = 1

    if r2[0] >= 1 - d_of_hole  and r2[0] <= 1 + d_of_hole and r2[1] >= 0 and r2[1] <= 0 + d_of_hole and pbm2 == 0: #Lower Middle  
        print('GREAT JOB! You made the Red ball into the lower middle pocket')

        v2 = array([0.0,0.0])
        pbm2 = 1 

    #------------------------------------------------------------------------------
    #below handles collisions between the ball and any walls

    #when colliding with the left and right walls the x component
    #of the velocity and acceleration changes but not the y components

    if r1[0] >= 2 or r1[0] <= 0: #Left and right wall 

        v1[0] = -v1[0]  #magnitude remains the same, direction is negated
        a1[0] = -a1[0]

    if r2[0] >= 2 or r2[0] <= 0: #same but for 2nd ball

        v2[0] = -v2[0]  
        a2[0] = -a2[0]

    #when top and bottom walls the y component of v and a change and not the y-components
        
    if r1[1] >= 1 or r1[1] <= 0: #Top and bottom wall

        v1[1] = -v1[1]  
        a1[1] = -a1[1]

    if r2[1] >= 1 or r2[1] <= 0:  #same but for 2nd ball
         
        v2[1] = -v2[1]  
        a2[1] = -a2[1]
        
    # BIG IF STATEMENT, THIS WILL DETERMINE THE COLLISION OF THE BALLs

    if linalg.norm(r1 - r2) < 2 * radius and limit == 0: #If the balls are in contact

        v1fx = ( ( r1[1] - r2[1] ) * (r1[1] * v1[0] - r2[1] * v1[0] + (-r1[0] + r2[0]) * v1[1] ) / ((r1[0] - r2[0])**2 + (r1[1] - r2[1])**2 ))

        v1fy = ( ( r1[0] - r2[0]) * (-r1[1] * v1[0] + r2[1] * v1[0] + (r1[0] - r2[0]) * v1[1])) / ((r1[0] - r2[0])**2 + (r1[1] - r2[1])**2 )
                                              
        v2fx = ( ( r1[0] - r2[0]) * ( r1[0] * v1[0] - r2[0] * v1[0] + (r1[1] - r2[1] ) *v1[1])) / ((r1[0] - r2[0])**2 + (r1[1] - r2[1])**2 )

        v2fy = ( ( r1[1] - r2[1] ) * (r1[0] * v1[0]  - r2[0] * v1[0] + (r1[1] - r2[1]) * v1[1] ) ) / ((r1[0] - r2[0])**2 + (r1[1] - r2[1])**2 )

        v1 = array([v1fx,v1fy])  

        v2 = array([v2fx,v2fy]) 

        limit = 1    #this refers back to before the large while statment at which point 'limit == 0'
                     #this prevents the balls from colliding twice, once it happens limit becomes 1 and
                     #this if statement will never be able to run again

#-------------------------------------------------------------------------------
        
#plotting the same pool table, with both balls' final positions and their paths
        
ax = axes()  #creates 'ax' object from 'axes' class

title("The Pool Table", fontsize=25)  #titles the graph

scatter(Holes_x_position , Holes_y_position, markersize, 'k')#plots representation of pockets
plot(r1x_plot,r1y_plot , 'c-.' )  #graphs the paths of either ball
plot(r2x_plot,r2y_plot , 'y-.' )

ax.set_facecolor("green")  #uses method of ax to make backgroud green

ax.set_xlabel('x (m)')                         #labels axes using methods of ax object
ax.set_ylabel('y (m)')
xlim(-0.02,2.02)                        #establishes domain and range of graph
ylim(-0.02,1.02)

scatter( r1[0] , r1[1], ballgraphsize, 'w' )  #graphs the final ball positions
scatter( r2[0] , r2[1], ballgraphsize, 'r' )  

show()

