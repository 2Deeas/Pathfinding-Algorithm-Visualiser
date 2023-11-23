# import required modules
import pygame, sys
from User_Interface_Objects import UI_Button
from Constants import *

# Defining a class for the help menu
class Help_State:
    # Initializing the class and creating the window and button object
    def __init__(self):
        # Initializing pygame
        pygame.init()
        # Setting the caption of the window
        pygame.display.set_caption("Help Menu")

        # Creating an object for the back button
        self.Button_Back_Object = UI_Button(940, 650, Button_Back, 0.5, WINDOW)

        # Displaying the help menu background image
        WINDOW.blit(background_image_3, (0, 0))

    # Creating the main loop for the help menu
    def help_loop(self):
        try:
            # Running an infinite loop until the user closes the window or clicks the back button
            while True:
                # Checking for events
                for event in pygame.event.get():
                    # If the user clicks the close button, exit the program
                    if event.type == pygame.QUIT:
                        sys.exit()
                    # If the user clicks the back button, delete the object and return to the previous menu
                    if self.Button_Back_Object.draw():
                        del self

                # Updating the display
                pygame.display.update()

        # Catching an error that occurs when the object is deleted before exiting the loop
        except UnboundLocalError:
            pass
