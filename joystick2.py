import pygame

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

initializeJoystick()
run = True
defualtAxis = getJoystickAxes()
print(defualtAxis)
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
        print(axis)
        # run = False

    if buttonsEmpty == False:
        print(buttons)
        run = False