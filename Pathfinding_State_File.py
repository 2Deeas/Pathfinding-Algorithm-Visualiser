# import required modules
import pygame, sys
from Graph_Structure import Graph
from Constants import *
from User_Interface_Objects import *

# define a class for pathfinding state
class Pathfinding_State:
    def __init__(self, graph_dimensions_input):
        # initialize pygame
        pygame.init()

        # set the title of the window
        pygame.display.set_caption("Shortest Path Visualiser")

        # initialize instance variables
        self.graph_dimensions_input = graph_dimensions_input
        self.Button_Start_Object = UI_Button(830, 75, Button_Start, 0.5, WINDOW)
        self.Button_End_Object = UI_Button(830, 195, Button_End, 0.5, WINDOW)
        self.Button_Barrier_Object = UI_Button(830, 315, Button_Barrier, 0.5, WINDOW)
        self.Button_Barrier_Clear_Object = UI_Button(
            830, 435, Button_Barrier_Clear, 0.5, WINDOW
        )
        self.Button_Clear_All_Object = UI_Button(
            830, 555, Button_Clear_All, 0.5, WINDOW
        )
        self.Button_Back_Object = UI_Button(830, 675, Button_Back, 0.5, WINDOW)
        self.Button_Pathfinding = BooleanButton(
            1058, 250, Button_Dijkstra_Scaled, 1, WINDOW, Button_Astar_Scaled
        )
        self.Button_Heuristic = BooleanButton(
            1058, 400, Button_Manhattan_Scaled, 1, WINDOW, Button_Euclidean_Scaled
        )
        self.graph = Graph(self.graph_dimensions_input, WINDOW_HEIGHT)

        # set the background image
        WINDOW.blit(background_image_2, (0, 0))

        # draw the graph
        self.graph.draw()

    def position_check(self, pos):
        # check which button was pressed
        if self.Button_Start_Object.rect.collidepoint(pos):
            self.draw_start()
        elif self.Button_End_Object.rect.collidepoint(pos):
            self.draw_end()
        elif self.Button_Barrier_Object.rect.collidepoint(pos):
            self.draw_barrier()

    def draw_start(self):
        # if start button is clicked
        if self.Button_Start_Object.draw():

            # get the position of the button clicked
            pos = self.graph.pathfinding(
                "Start",
                self.Button_Pathfinding.get_boolean_condition(),
                self.Button_Heuristic.get_boolean_condition(),
            )

            # try to check the position
            try:
                self.position_check(pos)
            except TypeError:
                pass

    def draw_end(self):
        # if end button is clicked
        if self.Button_End_Object.draw():

            # get the position of the button clicked
            pos = self.graph.pathfinding(
                "End",
                self.Button_Pathfinding.get_boolean_condition(),
                self.Button_Heuristic.get_boolean_condition(),
            )

            # try to check the position
            try:
                self.position_check(pos)
            except TypeError:
                pass

    def draw_barrier(self):
        # if barrier button is clicked
        if self.Button_Barrier_Object.draw():

            # get the position of the button clicked
            pos = self.graph.pathfinding(
                "Barrier",
                self.Button_Pathfinding.get_boolean_condition(),
                self.Button_Heuristic.get_boolean_condition(),
            )

            # try to check the position
            try:
                self.position_check(pos)
            except TypeError:
                pass

    def pathfinding_loop(self):
        try:
            while True:

                # Improvement
                Error = False

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                    self.draw_start()

                    self.draw_end()

                    self.draw_barrier()

                    if self.Button_Back_Object.draw():
                        del self

                    elif self.Button_Barrier_Clear_Object.draw():
                        self.graph.clear_barriers()

                    elif self.Button_Clear_All_Object.draw():
                        self.graph.clear_graph()

                    elif self.Button_Pathfinding.draw():
                        self.Button_Pathfinding.update()

                    elif self.Button_Heuristic.draw():
                        self.Button_Heuristic.update()

                    # Improvement
                    for row in self.graph.grid:
                        for node in row:
                            if node.state.is_path():
                                Error = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            print("Enter Key Pressed")

                    # Improvement
                    if event.type == pygame.KEYDOWN and not Error:
                        if (
                            event.key == pygame.K_RETURN
                            and self.graph.start
                            and self.graph.end
                        ):
                            self.graph.running_algorithm(
                                self.Button_Pathfinding.get_boolean_condition(),
                                self.Button_Heuristic.get_boolean_condition(),
                            )
                        elif (
                            event.key == pygame.K_RETURN
                            and self.graph.start
                            and not self.graph.end
                        ):
                            Insufficient_Nodes_Error = ErrorMessage(
                                "insufficient_nodes_error"
                            )
                            Insufficient_Nodes_Error.show_error_message()
                        elif (
                            event.key == pygame.K_RETURN
                            and self.graph.end
                            and not self.graph.start
                        ):
                            Insufficient_Nodes_Error = ErrorMessage(
                                "insufficient_nodes_error"
                            )
                            Insufficient_Nodes_Error.show_error_message()

                        elif (
                            event.key == pygame.K_RETURN
                            and not self.graph.start
                            and not self.graph.end
                        ):
                            Insufficient_Nodes_Error = ErrorMessage(
                                "insufficient_nodes_error"
                            )
                            Insufficient_Nodes_Error.show_error_message()

                pygame.display.update()

        except UnboundLocalError:
            pass

    def __del__(self):
        pass
