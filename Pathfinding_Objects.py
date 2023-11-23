# import required modules
from Constants import *
from Data_Structure_Objects import *
import time


class State:
    """
    A class to represent the state of a node.
    """

    def __init__(self):
        self.state = None

    @property
    def colour(self):
        return states.get(self.state)

    def get_colour(self):
        return self.colour

    def get_state(self):
        return self.state

    def set_colour(self):
        self.colour = states.get(self.state)

    def set_state(self, newState):
        self.state = newState

    def is_closed(self):
        return self.state == "Closed"

    def is_open(self):
        return self.state == "Open"

    def is_barrier(self):
        return self.state == "Barrier"

    def is_start(self):
        return self.state == "Start"

    def is_end(self):
        return self.state == "End"

    def is_path(self):
        return self.state == "Path"


class Node:
    """
    A class to represent a node in the grid.
    """

    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.state = State()
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def reset(self):
        self.state.set_state(None)

    def make_start(self):
        self.state.set_state("Start")

    def make_closed(self):
        self.state.set_state("Closed")

    def make_open(self):
        self.state.set_state("Open")

    def make_barrier(self):
        self.state.set_state("Barrier")

    def make_end(self):
        self.state.set_state("End")

    def make_path(self):
        self.state.set_state("Path")

    def draw(self, win):
        """
        Draw the node onto the window.
        """
        pygame.draw.rect(
            win, self.state.get_colour(), (self.x, self.y, self.width, self.width)
        )

    def update_neighbours(self, grid):
        """
        Update the neighbours of the node.
        """
        self.neighbours = []
        if (
            self.row < self.total_rows - 1
            and not grid[self.row + 1][self.col].state.is_barrier()
        ):  # Update the bottom side neighbour
            self.neighbours.append(grid[self.row + 1][self.col])

        if (
            self.row > 0 and not grid[self.row - 1][self.col].state.is_barrier()
        ):  # Update the top side neighbour
            self.neighbours.append(grid[self.row - 1][self.col])

        if (
            self.col < self.total_rows - 1
            and not grid[self.row][self.col + 1].state.is_barrier()
        ):  # Update the right side neighbour
            self.neighbours.append(grid[self.row][self.col + 1])

        if (
            self.col > 0 and not grid[self.row][self.col - 1].state.is_barrier()
        ):  # Update the left side neighbour
            self.neighbours.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False


class DijkstraPathfinding:
    """
    This class implements Dijkstra's pathfinding algorithm
    """

    # Initialize the class with a priority queue, dictionaries for g_score and f_score, and other variables
    def __init__(self, rows):
        self.open_set = PriorityQueue()  # priority queue to hold nodes
        self.came_from = {}  # dictionary to hold parent nodes
        self.g_score = {}
        # dictionary to hold the cost of the path from the start node to a node
        self.f_score = {}
        # dictionary to hold the sum of g_score and h_score (heuristic) for a node
        self.open_set_hash = HashTable(
            rows
        )  # hash table to keep track of which nodes are in the open set
        self.path_length = 0  # initialize path length variable
        self.nodes_accessed = 0  # initialize nodes accessed variable
        self.elapsed_time = 0  # initialize elapsed time variable

    # Reconstruct the path from the end node to the start node using parent nodes and draw the path
    def reconstruct_path(self, current, draw):
        self.path_length = 0  # initialize path length variable
        while current in self.came_from:
            current = self.came_from[current]
            current.make_path()
            self.path_length += 1  # update path length
            draw()  # draw the updated path

    # Dijkstra's pathfinding algorithm
    def algorithm(self, draw, grid, start, end):
        initial_time = time.time()  # record start time
        self.open_set.push(start, 0)  # add start node to the open set with priority 0
        self.open_set_hash.insert(start)  # add start node to the hash table

        # Initialize g_score and f_score dictionaries
        self.g_score = {node: float("inf") for row in grid for node in row}
        self.g_score[start] = 0
        self.f_score = {node: float("inf") for row in grid for node in row}
        self.f_score[start] = 0

        # Loop until the open set is empty
        while not self.open_set.is_empty():

            current = (
                self.open_set.pop()
            )  # get node with lowest f_score from the open set
            self.nodes_accessed += 1  # update nodes accessed
            self.open_set_hash.remove(
                current
            )  # remove current node from the hash table

            if (
                current == end
            ):  # if the current node is the end node, reconstruct the path and return True
                self.reconstruct_path(end, draw)
                end.make_end()
                return True

            # Loop through the neighbours of the current node
            for neighbour in current.neighbours:
                try:
                    temp_g_score = (
                        self.g_score[current] + 1
                    )  # calculate the tentative g_score for the neighbour node
                except KeyError:
                    pass

                if (
                    temp_g_score < self.g_score[neighbour]
                ):  # if the tentative g_score is lower than the current g_score of the neighbour node
                    self.came_from[
                        neighbour
                    ] = current  # update the parent node of the neighbour node
                    self.g_score[
                        neighbour
                    ] = temp_g_score  # update the g_score of the neighbour node
                    self.f_score[
                        neighbour
                    ] = temp_g_score  # update the f_score of the neighbour node
                    if neighbour not in [
                        element
                        for sublist in self.open_set_hash.table
                        for element in sublist
                    ]:
                        # add the neighbour node to the open set with priority f_score and add it to the hash table
                        self.open_set.push(neighbour, self.f_score[neighbour])

                        self.open_set_hash.insert(neighbour)
                        neighbour.make_open()

            draw()

            if current != start:
                current.make_closed()
            final_time = time.time()
            self.elapsed_time = final_time - initial_time

        # if no path is found, False is returned
        return False


class AStarPathfinding(DijkstraPathfinding):
    """
    This class implements A* pathfinding algorithm
    """

    # Define the constructor for the class.
    def __init__(self, rows):

        # Call the constructor of the superclass.
        super().__init__(rows=rows)

    # Define a method that calculates the Manhattan distance between two points.

    @staticmethod
    def manhattan_distance(p1, p2):

        # Get the x and y coordinates of each point.
        x1, y1 = p1
        x2, y2 = p2

        # Return the absolute difference between the x coordinates plus the absolute difference between the y coordinates.
        return abs(x1 - x2) + abs(y1 - y2)

    # Define a method that calculates the Euclidean distance between two points.

    @staticmethod
    def euclidean_distance(p1, p2):
        # Get the x and y coordinates of each point.
        x1, y1 = p1
        x2, y2 = p2

        # Return the square root of the sum of the squares of the differences between the x and y coordinates.
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # Define a method that implements the A* algorithm.
    def algorithm(self, draw, grid, start, end, current_heuristic):

        # Record the time at the start of the algorithm.
        initial_time = time.time()

        # Add the start node to the open set and mark it as visited.
        self.open_set.push(start, 0)
        self.open_set_hash.insert(start)

        # Set the g score for each node to infinity.
        self.g_score = {node: float("inf") for row in grid for node in row}

        # Set the g score for the start node to 0.
        self.g_score[start] = 0

        # Set the f score for each node to infinity.
        self.f_score = {node: float("inf") for row in grid for node in row}

        # Set the f score for the start node based on the chosen heuristic.
        if current_heuristic:
            self.f_score[start] = self.manhattan_distance(
                start.get_pos(), end.get_pos()
            )
        else:
            self.f_score[start] = self.euclidean_distance(
                start.get_pos(), end.get_pos()
            )

        # Loop until the open set is empty.
        while not self.open_set.is_empty():
            print(self.open_set)

            # Check for quit event.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # Remove the node with the lowest f score from the open set.
            current = self.open_set.pop()

            # Increment the nodes_accessed counter.
            self.nodes_accessed += 1

            # Remove the current node from the hash table.
            self.open_set_hash.remove(current)

            # Check if the current node is the end node.
            if current == end:
                # Reconstruct the path from the start node to the end node.
                self.reconstruct_path(end, draw)

                # Mark the end node as the end node.
                end.make_end()

                # Return True to indicate that a path was found.
                return True

            # Loop through the neighbours of the current node.
            for neighbour in current.neighbours:
                try:
                    # Calculate the tentative g score for the neighbour.
                    temp_g_score = self.g_score[current] + 1
                except KeyError:
                    pass

                # Check if the tentative g score is lower than the current g score for the neighbour.
                if temp_g_score < self.g_score[neighbour]:
                    self.came_from[neighbour] = current
                    self.g_score[neighbour] = temp_g_score
                    if current_heuristic:
                        self.f_score[
                            neighbour
                        ] = temp_g_score + self.manhattan_distance(
                            neighbour.get_pos(), end.get_pos()
                        )
                    else:
                        self.f_score[
                            neighbour
                        ] = temp_g_score + self.euclidean_distance(
                            neighbour.get_pos(), end.get_pos()
                        )

                    if neighbour not in [
                        element
                        for sublist in self.open_set_hash.table
                        for element in sublist
                    ]:
                        self.open_set.push(neighbour, self.f_score[neighbour])
                        self.open_set_hash.insert(neighbour)
                        neighbour.make_open()

            draw()

            if current != start:
                current.make_closed()

            # Record the time at the end of the algorithm
            final_time = time.time()

            # Set the elapsed time attribute to the amount of time the algorithm took
            self.elapsed_time = final_time - initial_time

        # Return False if path was not found
        return False


