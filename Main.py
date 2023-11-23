# import required modules
from Pathfinding_State_File import Pathfinding_State
from Menu_State_File import Menu_State
from User_Interface_Objects import Graph_Dimensions_Input
from Help_State_File import Help_State

# Define the main function
def Main():
    # Create a new Menu_State object
    Menu = Menu_State()

    # Check the value returned by the main loop method of the Menu_State object
    if Menu.main_loop():
        # If the return value is True, create a new Graph_Dimensions_Input object and retrieve its return value
        Pathfinding_Dimensions = Graph_Dimensions_Input()

        # If the return value of the Graph_Dimensions_Input object is None, call the main function again
        if Pathfinding_Dimensions.return_value == None:
            return Main()

        # If the return value of the Graph_Dimensions_Input object is not None, create a new Pathfinding_State object with the return value as its parameter and call its pathfinding_loop method
        Current_State = Pathfinding_State(Pathfinding_Dimensions.return_value)
        Current_State.pathfinding_loop()

    # If the return value of the Menu_State main loop method is False, create a new Help_State object and call its help_loop method
    else:
        Current_State = Help_State()
        Current_State.help_loop()

    # Call the main function again
    return Main()


# Call the main function if this script is run as the main program
if __name__ == "__main__":
    Main()
