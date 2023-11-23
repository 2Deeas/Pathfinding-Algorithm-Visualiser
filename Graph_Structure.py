# Import the required modules
import pygame, sys

# Import the required classes from other files
from Constants import *
from Data_Structure_Objects import *
from Pathfinding_Objects import *
from User_Interface_Objects import ErrorMessage, InfoWindow


class Graph:
    """
    This is the Graph object
    """

    def __init__(self, rows, size):
        # Initialize the rows and size properties
        self.rows = rows
        self.size = size
        # Initialize the graph background as a surface of size (size, size)
        self.graph_background = pygame.Surface((size, size))
        # Initialize the start and end points as None
        self.start = None
        self.end = None
        self.gap = self.size // self.rows
        # Initialize a DijkstraPathfinding object and an AStarPathfinding object
        self.Dijkstra = DijkstraPathfinding(self.rows)
        self.Astar = AStarPathfinding(self.rows)
        # Initialize the grid property by calling the make_grid method
        self.grid = self.make_grid()

    # Define a property to return the total path length
    @property
    def path_length(self):
        return self.Dijkstra.path_length + self.Astar.path_length

    # Define a property to return the total number of nodes accessed
    @property
    def nodes_accessed(self):
        return self.Dijkstra.nodes_accessed + self.Astar.nodes_accessed

    # Define a property to return the total elapsed time
    @property
    def elapsed_time(self):
        return self.Dijkstra.elapsed_time + self.Astar.elapsed_time

    # Define methods to return the path length, number of nodes accessed, and elapsed time
    def get_path_length(self):
        return self.path_length

    def get_nodes_accessed(self):
        return self.nodes_accessed

    def get_elapsed_time(self):
        return self.elapsed_time

    # Define a method to create the grid of nodes
    def make_grid(self):
        # Calculate the gap between the nodes
        gap = self.size // self.rows
        # Create a 2D list of nodes with each node having a size of gap x gap
        return [
            [Node(i, j, gap, self.rows) for j in range(self.rows)]
            for i in range(self.rows)
        ]

    # Define a method to draw the grid
    def draw_grid(self):
        # Calculate the gap between the nodes
        gap = self.size // self.rows
        # Draw horizontal lines on the screen
        for i in range(self.rows):
            pygame.draw.line(WINDOW, GREY, (0, i * gap), (self.size, i * gap))
            # Draw vertical lines on the screen
            for j in range(self.rows):
                pygame.draw.line(WINDOW, GREY, (j * gap, 0), (j * gap, self.size))

    # Define a method to draw the graph
    def draw(self):
        # Fill the background with white color
        self.graph_background.fill(WHITE)
        # Draw each node in the grid
        for row in self.grid:
            for node in row:
                node.draw(WINDOW)
        # Draw the grid lines
        self.draw_grid()
        # Update the display
        pygame.display.update()

    # Define a method to get the row and column of the node that was clicked
    def get_clicked_pos(self, pos):
        # Calculate the gap between the nodes
        gap = self.size // self.rows
        # Get the x and y coordinates of the mouse click
        y, x = pos
        # Calculate the row and column of the node that was clicked
        row = y // gap
        col = x // gap

        return row, col

    def running_algorithm(self, current_algorithm, current_heuristic):
        """
        Runs the selected pathfinding algorithm (Dijkstra or A*) and shows the pathfinding statistics window.
        """
        for row in self.grid:
            for node in row:
                node.update_neighbours(self.grid)

        if current_algorithm == True:
            # If Dijkstra Algorithm is selected, reset path length, nodes accessed and elapsed time to 0
            self.Astar.path_length = 0
            self.Astar.nodes_accessed = 0
            self.Astar.elapsed_time = 0
            # Run Dijkstra's algorithm, if it returns False show a Path_Error error message
            if (
                self.Dijkstra.algorithm(
                    lambda: self.draw(), self.grid, self.start, self.end
                )
                == False
            ):
                Path_Error = ErrorMessage("Path_Error")
                Path_Error.show_error_message()
                return None
            else:
                # Show the pathfinding statistics window
                Pathfinding_Statistics = InfoWindow(
                    self.get_elapsed_time(),
                    self.get_nodes_accessed(),
                    self.get_path_length(),
                )
                return None

        else:
            # If A*'s algorithm is selected, reset path length, nodes accessed and elapsed time to 0
            self.Dijkstra.path_length = 0
            self.Dijkstra.nodes_accessed = 0
            self.Dijkstra.elapsed_time = 0
            # Run A* algorithm, if it returns False show a Path_Error error message
            if (
                self.Astar.algorithm(
                    lambda: self.draw(),
                    self.grid,
                    self.start,
                    self.end,
                    current_heuristic,
                )
                == False
            ):
                Path_Error = ErrorMessage("Path_Error")
                Path_Error.show_error_message()
                return None
            else:
                # Show the pathfinding statistics window
                Pathfinding_Statistics = InfoWindow(
                    self.get_elapsed_time(),
                    self.get_nodes_accessed(),
                    self.get_path_length(),
                )
                return None

    def clear_graph(self):
        """
        Clears the entire graph and resets the start and end points.
        """
        ErrorCount = 0
        for row in self.grid:
            for node in row:
                if node.state.get_state() == None:
                    ErrorCount += 1

        if ErrorCount == self.rows**2:
            # If there are no nodes on the grid, show a Clear_Graph_Error error message
            Clear_Graph_Error = ErrorMessage("clear_graph_error")
            Clear_Graph_Error.show_error_message()
            ErrorCount = 0
        else:
            # Reset all nodes to their initial state, set start and end points to None, and draw the grid
            for row in self.grid:
                for node in row:
                    node.reset()

            self.start = None
            self.end = None

            self.draw()
        return None

    def clear_barriers(self):
        """
        Clears all barrier nodes from the grid.
        """
        Error = True
        # Checks if any node is a barrier node.
        for row in self.grid:
            for node in row:
                if node.state.is_barrier():
                    Error = False

        # If no node is a barrier node, shows an error message. Otherwise, clears all barrier nodes.
        if Error:
            Clear_Barrier_Error = ErrorMessage("clear_barriers_error")
            Clear_Barrier_Error.show_error_message()
        else:
            for row in self.grid:
                for node in row:
                    if node.state.is_barrier():
                        node.reset()
            self.draw()
        return None

    def pathfinding(self, mode, current_pathfinding, current_heuristic):
        """
        Conducts pathfinding according to the given mode and pathfinding algorithm.

        :param mode: the current mode (Start, End, or Barrier)
        :param current_pathfinding: the current pathfinding algorithm (Dijkstra or A*)
        :param current_heuristic: the current heuristic function (Manhattan or Euclidean)
        """
        while True:
            self.draw()
            Error = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                for row in self.grid:
                    for node in row:
                        if node.state.is_path():
                            Error = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print("Enter Key Pressed")

                # If any node is a path node, shows an error message and returns None
                if Error:
                    Reset_Graph_Error = ErrorMessage("reset_graph_error")
                    Reset_Graph_Error.show_error_message()
                    return None
                else:
                    if pygame.mouse.get_pressed()[0]:  # LEFT
                        pos = pygame.mouse.get_pos()
                        if pos[0] <= self.size:
                            row, col = self.get_clicked_pos(pos)

                            node = self.grid[row][col]

                            if mode == "Start":

                                if self.start == None:
                                    if node.state.is_end() == True:
                                        self.end = None
                                    self.start = node
                                    self.start.make_start()
                                else:
                                    if node.state.is_end() == True:
                                        self.end = None
                                    self.start.reset()
                                    self.start = node
                                    self.start.make_start()
                            elif mode == "End":
                                if self.end == None:
                                    if node.state.is_start() == True:
                                        self.start = None
                                    self.end = node
                                    self.end.make_end()
                                else:
                                    if node.state.is_start() == True:
                                        self.start = None
                                    self.end.reset()
                                    self.end = node
                                    self.end.make_end()

                            elif mode == "Barrier":
                                if node.state.is_start() == True:
                                    self.start = None
                                elif node.state.is_end() == True:
                                    self.end = None
                                node.make_barrier()

                        else:

                            return pos

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:

                            if self.start and self.end:
                                self.running_algorithm(
                                    current_pathfinding, current_heuristic
                                )
                            else:
                                Insufficient_Nodes_Error = ErrorMessage(
                                    "insufficient_nodes_error"
                                )
                                Insufficient_Nodes_Error.show_error_message()

                        # A NoneType is returned as we must go back to the main loop
                        return None
