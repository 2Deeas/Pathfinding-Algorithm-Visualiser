# importing required modules
import tkinter as tk
from tkinter import Tk, messagebox
import pygame
from Constants import *


class UI_Button:
    def __init__(self, x, y, image, scale, screen):
        """
        Initializes a UI button object with given properties.

        :param x: The x-coordinate of the button.
        :param y: The y-coordinate of the button.
        :param image: The image of the button.
        :param scale: The scale factor of the button.
        :param screen: The screen to draw the button on.
        """

        # Get the dimensions of the image.
        self.width = image.get_width()
        self.height = image.get_height()

        # Scale the image.
        self.image = pygame.transform.scale(
            image, (int(self.width * scale), int(self.height * scale))
        )

        # Set the position of the button.
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Set the screen to draw the button on.
        self.screen = screen

    def draw(self):
        """
        Draws the button on the screen and returns whether the button was clicked.

        :return: A boolean indicating whether the button was clicked.
        """
        action = False

        # Get the position of the mouse.
        pos = pygame.mouse.get_pos()

        # Check if the mouse is over the button and if it is clicked.
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        # Draw the button on the screen.
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


class BooleanButton(UI_Button):
    def __init__(self, x, y, image, scale, screen, alternate_image):
        """
        Initializes a BooleanButton object with a given x and y position, image, scale, screen, and alternate image.

        Args:
            x (int): x position of the button
            y (int): y position of the button
            image (pygame.Surface): default image of the button
            scale (float): scaling factor of the image
            screen (pygame.Surface): screen to draw the button on
            alternate_image (pygame.Surface): image of the button when boolean_condition is False
        """
        self.boolean_condition = True
        self.count = 0
        self.alternate_image = alternate_image
        self.temporary_image = image
        super().__init__(x, y, image, scale, screen)

    def update(self):
        """
        Updates the image of the button and the boolean condition based on the count of updates.

        Returns:
            bool: True if boolean_condition is True, False otherwise
        """
        self.count += 1

        if self.count % 2 == 0:
            self.image = self.temporary_image
            self.boolean_condition = True
        else:
            self.image = self.alternate_image
            self.boolean_condition = False

        self.draw()

        return self.boolean_condition

    def get_boolean_condition(self):
        """
        Returns the boolean condition of the button.

        Returns:
            bool: True if boolean_condition is True, False otherwise
        """
        return self.boolean_condition


class ErrorMessage:
    def __init__(self, error_type):
        """
        Initializes an instance of the ErrorMessage class.

        Args:
            error_type (str): The type of error to display.
        """
        self.error_type = error_type

    def show_error_message(self):
        """
        Displays an error message based on the type of error.
        """
        if "clear" in self.error_type:
            # If error is related to clearing the graph
            if self.error_type == "clear_graph_error":
                error_message = "non-default nodes"
            elif self.error_type == "clear_barriers_error":
                error_message = "barriers"
            # Show an error message with the specific error type and message
            tk.Tk().wm_withdraw()
            messagebox.showerror(
                self.error_type,
                f"There are no {error_message} on the graph",
            )

        # If there are insufficient nodes to run the algorithm
        elif self.error_type == "insufficient_nodes_error":
            tk.Tk().wm_withdraw()
            # Show an error message with the specific error type and message
            messagebox.showerror(
                self.error_type,
                f"Start or End node missing, place both to run the algorithm.",
            )

        # If there is an attempt to place more nodes without clearing the graph
        elif self.error_type == "reset_graph_error":
            tk.Tk().wm_withdraw()
            # Show an error message with the specific error type and message
            messagebox.showerror(
                self.error_type,
                f"Please 'Clear Graph' before continuing to place more nodes.",
            )

        else:
            # If there is no possible path between the start and end nodes
            tk.Tk().wm_withdraw()
            # Show an error message with the specific error type and message
            messagebox.showinfo(
                self.error_type,
                f"There is no possible path between the start and end nodes to be found.",
            )


class Graph_Dimensions_Input:
    def __init__(self):
        """
        Initializes a Graph_Dimensions_Input Tkinter object

        """

        # Instantiating properties
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.title("Menu Window")
        self.root.config(bg="#325971")

        # Set label for graph dimensions
        self.label = tk.Label(
            self.root,
            text="Choose Graph Dimensions:",
            fg="#C8B782",
            bg="#325971",
            font=("Helvetica", 16),
        )
        self.label.pack(pady=10)

        # Create buttons for different dimensions
        self.row1 = tk.Frame(self.root, bg="#325971")
        self.row1.pack()
        self.row2 = tk.Frame(self.root, bg="#325971")
        self.row2.pack()

        self.button1 = tk.Button(
            self.row1,
            text="10x10",
            command=lambda: self.close_window_and_return(10),
            height=2,
            width=10,
            bg="#C8B782",
            fg="#325971",
            font=("Helvetica", 14),
        )
        self.button2 = tk.Button(
            self.row1,
            text="25x25",
            command=lambda: self.close_window_and_return(25),
            height=2,
            width=10,
            bg="#C8B782",
            fg="#325971",
            font=("Helvetica", 14),
        )

        self.button3 = tk.Button(
            self.row2,
            text="50x50",
            command=lambda: self.close_window_and_return(50),
            height=2,
            width=10,
            bg="#C8B782",
            fg="#325971",
            font=("Helvetica", 14),
        )
        self.button4 = tk.Button(
            self.row2,
            text="100x100",
            command=lambda: self.close_window_and_return(100),
            height=2,
            width=10,
            bg="#C8B782",
            fg="#325971",
            font=("Helvetica", 14),
        )

        # Pack buttons in the window
        self.button1.pack(side=tk.LEFT, padx=10, pady=10)
        self.button2.pack(side=tk.LEFT, padx=10, pady=10)
        self.button3.pack(side=tk.LEFT, padx=10, pady=10)
        self.button4.pack(side=tk.LEFT, padx=10, pady=10)

        self.return_value = None

        # Run Tkinter window
        self.root.mainloop()

    def close_window_and_return(self, return_value):
        # Close the window and return selected value
        self.return_value = return_value
        self.root.destroy()

    def get_return_value(self):
        # Returns the value selected by the user
        return self.return_value


class InfoWindow:
    # Initialize the InfoWindow class with three values
    def __init__(self, elapsed_time, total_nodes, path_distance):
        """
        Initializes an InfoWindow object which takes in the output info from the last path.

        Args:
            elapsed_time (float): Last path's elapsed time
            total_nodes (int): Last path's total affected nodes
            path_distance (int): Last path's length
        """
        # Create a new window
        self.root = tk.Tk()
        # Set the title of the window
        self.root.title("Pathfinding Statistics")
        # Set the size of the window
        self.root.geometry("300x215")
        # Set the background color of the window
        self.root.config(bg="#325971")

        # Create the first label with some text, color, font, and alignment
        self.label1 = tk.Label(
            self.root,
            text="Pathfinding Elapsed Time:",
            fg="#C8B782",
            bg="#325971",
            font=("Helvetica", 12),
            width=20,
            anchor="w",
        )
        self.label1.pack(pady=5, padx=5)

        # Create the first value label with the first value passed to the class, some text, color, font, and alignment
        self.elapsed_time_label = tk.Label(
            self.root,
            text=f"{elapsed_time:.4f}",
            fg="#C8B782",
            bg="#325971",
            font=("Helvetica", 12),
            width=20,
            anchor="w",
        )
        self.elapsed_time_label.pack(pady=5, padx=5)

        # Create the second label with some text, color, font, and alignment
        self.label2 = tk.Label(
            self.root,
            text="Total Nodes Affected:",
            fg="#C8B782",
            bg="#325971",
            font=("Helvetica", 12),
            width=20,
            anchor="w",
        )
        self.label2.pack(pady=5, padx=5)

        # Create the second value label with the second value passed to the class, some text, color, font, and alignment
        self.total_nodes_label = tk.Label(
            self.root,
            text=f"{total_nodes}",
            fg="#C8B782",
            bg="#325971",
            font=("Helvetica", 12),
            width=20,
            anchor="w",
        )
        self.total_nodes_label.pack(pady=5, padx=5)

        # Create the third label with some text, color, font, and alignment
        self.label3 = tk.Label(
            self.root,
            text="Shortest Path Length:",
            fg="#C8B782",
            bg="#325971",
            font=("Helvetica", 12),
            width=20,
            anchor="w",
        )
        self.label3.pack(pady=5, padx=5)

        # Create the third value label with the third value passed to the class, some text, color, font, and alignment
        self.path_distance_label = tk.Label(
            self.root,
            text=f"{path_distance}",
            fg="#C8B782",
            bg="#325971",
            font=("Helvetica", 12),
            width=20,
            anchor="w",
        )
        self.path_distance_label.pack(pady=5, padx=5)

        # Start the main loop of the window
        self.root.mainloop()
