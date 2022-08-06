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

initializeJoystick()
run = True
while run:
    buttons = getJoystickButtons()
    buttonsEmpty = True
    
    for button in buttons:
        if button != 0:
            buttonsEmpty = False
            break
    
    if buttonsEmpty == False:
        print(buttons)
        run = False
        
