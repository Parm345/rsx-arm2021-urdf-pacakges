# pip3 install
import pygame
import copy
import numpy as np

def initializeJoystick():
# robot operated with a joystick - uses pygame library
    pygame.init()
    global joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print('Initialized joystick: %s' % joystick.get_name())
    print(joystick.get_numbuttons())
    
def getJoystickButtons(): # setting up the buttons
    pygame.event.pump() # allow pygame to handle internal actions, keep everything current
    
    buttons = []
    for i in range(0, joystick.get_numbuttons()):
        button = joystick.get_button(i)
        buttons.append(button)
    # print(buttons)
    return buttons

def getJoystickAxes(): # setting up the axes for the control stick
    out = [0,0,0,0,0,0]
    it = 0 # iterator
    pygame.event.pump()
    #Read input from the joystick       
    for i in range(0, joystick.get_numaxes()):
        out[i] = joystick.get_axis(i)
    return out

def getJoystickDirection(): # read the position of the stick
    global modeOfMovement
    global savedJointAngles
    global modeOfOperation

    modeOfMovement = 0

    joystickValues = getJoystickAxes()
    #print("Joystick direction values: {}".format(joystickValues))

    if modeOfMovement == 0:
        # print("All DOFs mode")
        # mode for all joints being controlled at once
        beforeDirectionVector = copy.deepcopy(joystickValues)
        #print(beforeDirectionVector)
        directionVector = [0,0,0,0,0,0] #beforeDirectionVector
        index = -1
        for thing in beforeDirectionVector:
            index += 1
            if abs(thing) > 0.05: # sensitivity "gap", to avoid random movements
                directionVector[index] = thing
        #print(directionVector)
    elif modeOfMovement == 1:
        # print("One DOF mode")
        # mode for only one joint at once rotation
        # determine direction
        directionVector = [0,0,0,0,0,0]
        storedVal = 0
        storedInd = 0
        ind = -1
        absJoystickValues = np.absolute(np.matrix(joystickValues))
        storedInd = np.argmax(absJoystickValues)
        storedVal = joystickValues[storedInd]
        # introduce some "sensitivity gap" to avoid random movement
        if abs(storedVal) > 0.05:
            # if storedInd == 3 and modeOfOperation == 3:
            #     if savedJointAngles[5] > 0:
            #         directionVector[storedInd] = storedVal
            #     else:on
            #         directionVector[storedInd] = -storedVal
            # else:
            directionVector[storedInd] = storedVal
        #print(directionVector)
        
    # needed specifically to make thigs coincide with our arm
    for i in range( len(directionVector) ):
        directionVector[i] = -directionVector[i]
    #xyz > yxz > zxy
    # swap x with y
    tempval = copy.deepcopy( directionVector[0] )
    directionVector[0] = copy.deepcopy( directionVector[1] )
    directionVector[1] = tempval
    # in new translation swap z and y
    tempval2 = copy.deepcopy( directionVector[2] )
    directionVector[2] = copy.deepcopy( directionVector[0] )
    directionVector[0] = tempval2
    # swap the z direction
    directionVector[0] = -directionVector[0]
    # rotations swaps. Remember for positionalIK mode it's rotations above yxz order
    directionVector[3] = -directionVector[3]
    directionVector[4] = directionVector[4]
    directionVector[5] = -directionVector[5]
    return directionVector

initializeJoystick()
run = True
defualtAxis = getJoystickAxes()

print(defualtAxis)
print(getJoystickDirection())


while run:
    buttons = getJoystickButtons()
    axis = getJoystickAxes()
    buttonsEmpty = True
    
    for button in buttons:
        if button != 0:
            buttonsEmpty = False
            break
    
    axisMoved = False

    for ax in axis:
        if ax != 0:
            axisMoved = True
    
    if defualtAxis != axis:
        # print(axis)
        # run = False
        print(getJoystickDirection())
        # pass

    if buttonsEmpty == False:
        # print(buttons)
        run = False