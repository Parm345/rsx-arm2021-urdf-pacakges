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
    
    buttons = {"X": 0, "O": 0, "TRIANGLE": 0, "SQUARE": 0 , "L1": 0, "R1": 0, "L2": 0, "R2": 0, "SELECT": 0, "START": 0, "PLAY_STATION": 0, 
        "L3": 0, "R3": 0,"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0 }
    global buttonNames 
    buttonNames = list(buttons.keys())
    for i in range(0, joystick.get_numbuttons()):
        button = joystick.get_button(i)
        buttons[buttonNames[i]] = button
    # print(buttons)
    return buttons

initializeJoystick()
run = True
while run:
    buttons = getJoystickButtons()
    buttonsEmpty = True
    
    for button in buttons.values():
        if button != 0:
            buttonsEmpty = False
            break
    
    if buttonsEmpty == False:
        # print(buttons)
        for i in range(0, buttonNames.__len__()):
            if buttons[buttonNames[i]]:
                print(buttonNames[i] + " " + str(i))
        run = False
        
