# import Pygame module
import pygame

# set Window height and width
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 1200

# create a Pygame display with the given dimensions
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# define colors using RGB values
RED = (247, 87, 47)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (247, 221, 47)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
DARK_BLUE = (59, 70, 225)
LIGHT_BLUE = (96, 179, 243)
GOLD = (218, 182, 100)


# define the states with the corresponding colors
states = {
    None: WHITE,
    "Open": DARK_BLUE,
    "Closed": LIGHT_BLUE,
    "Start": RED,
    "End": ORANGE,
    "Barrier": BLACK,
    "Path": GOLD,
}

# load background images
background_image = pygame.image.load("Pathfinding NEA - Graphics\Background_Menu.png")
background_image_2 = pygame.image.load(
    "Pathfinding NEA - Graphics\Background_Pathfinding.png"
)
background_image_3 = pygame.image.load("Pathfinding NEA - Graphics\Background_Help.png")

# load button images
Button_Play = pygame.image.load("Pathfinding NEA - Graphics\Button_Pathfinding.png")
Button_Back = pygame.image.load("Pathfinding NEA - Graphics\Button_Back.png")
Button_Help = pygame.image.load("Pathfinding NEA - Graphics\Button_Help.png")
Button_Dijkstra = pygame.image.load("Pathfinding NEA - Graphics\Button_Dijkstra.png")
Button_Astar = pygame.image.load("Pathfinding NEA - Graphics\Button_Astar.png")
Button_Manhattan = pygame.image.load("Pathfinding NEA - Graphics\Button_Manhattan.png")
Button_Euclidean = pygame.image.load("Pathfinding NEA - Graphics\Button_Euclidean.png")
Button_Start = pygame.image.load("Pathfinding NEA - Graphics\Button_Start.png")
Button_End = pygame.image.load("Pathfinding NEA - Graphics\Button_End.png")
Button_Barrier = pygame.image.load("Pathfinding NEA - Graphics\Button_Barrier.png")
Button_Barrier_Clear = pygame.image.load(
    "Pathfinding NEA - Graphics\Button_Barrier_Clear.png"
)
Button_Clear_All = pygame.image.load("Pathfinding NEA - Graphics\Button_Clear_All.png")

# scale button images
Button_Dijkstra_Scaled = pygame.transform.scale(
    Button_Dijkstra,
    (Button_Dijkstra.get_width() * 0.7, Button_Dijkstra.get_height() * 0.7),
)
Button_Astar_Scaled = pygame.transform.scale(
    Button_Astar, (Button_Astar.get_width() * 0.7, Button_Astar.get_height() * 0.7)
)
Button_Manhattan_Scaled = pygame.transform.scale(
    Button_Manhattan,
    (Button_Manhattan.get_width() * 0.7, Button_Manhattan.get_height() * 0.7),
)
Button_Euclidean_Scaled = pygame.transform.scale(
    Button_Euclidean,
    (Button_Euclidean.get_width() * 0.7, Button_Euclidean.get_height() * 0.7),
)
Button_Play_Scaled = pygame.transform.scale(
    Button_Play, (Button_Play.get_width() * 0.75, Button_Play.get_height() * 0.75)
)
Button_Help_Scaled = pygame.transform.scale(
    Button_Help, (Button_Help.get_width() * 0.75, Button_Help.get_height() * 0.75)
)
