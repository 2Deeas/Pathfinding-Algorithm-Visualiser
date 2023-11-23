# import required modules

import pygame, sys
from User_Interface_Objects import UI_Button
from Constants import *


class Menu_State:
    """
    This class is responsible for the Menu state of the software
    """

    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Set the caption and icon of the game window
        pygame.display.set_caption("Main Menu")
        pygame.display.set_icon(Button_Astar)

        # Set the background image of the game window
        WINDOW.blit(background_image, (0, 0))

        # Calculate the x,y coordinates for the two buttons
        self.x, self.y = self.get_centered_image_position(
            Button_Help_Scaled.get_width(), Button_Help_Scaled.get_height()
        )

        # Create a play button
        self.Button_Pathfinding_Object = UI_Button(
            *self.get_centered_image_position(
                Button_Play_Scaled.get_width(), Button_Play_Scaled.get_height()
            ),
            Button_Play_Scaled,
            1,
            WINDOW
        )

        # Create a help button
        self.Button_Help_Scaled_Object = UI_Button(
            self.x,
            self.y + self.Button_Pathfinding_Object.height + 40,
            Button_Help_Scaled,
            1,
            WINDOW,
        )

    @staticmethod
    def get_centered_image_position(m, n):
        """Return the x,y coordinates of the top-left corner of an image with size m by n centered on a WINDOW with size p by q."""
        # Calculate the x,y coordinates of the top-left corner of the image to be centered
        x = (WINDOW_WIDTH - m) / 2
        y = (WINDOW_HEIGHT - n) / 2
        return (x, y)

    def main_loop(self):
        # The main loop of the game
        while True:
            for event in pygame.event.get():
                # Check if the user closed the window
                if event.type == pygame.QUIT:
                    sys.exit()

            # Check if the help button is clicked
            if self.Button_Help_Scaled_Object.draw() == True:
                return False

            # Check if the play button is clicked
            elif self.Button_Pathfinding_Object.draw() == True:
                return True

            # Update the display
            pygame.display.update()
