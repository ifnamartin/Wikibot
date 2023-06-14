from robotics import Robot
from robotgui import RobotGUI

scientists = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.introduce()

def get_scientists(scientists):
    robot.get_scientists(scientists)

def retrieve_info():
    robot.retrieve_scientist_information()

def close_br():
    print("Closing all browsers...\n")
    robot.browser.close_all_browsers()

def display_information(sdict):
    gui = RobotGUI(sdict)
    gui.run()

def say_goodbye():
    robot.say_goodbye()
    
def main():
    introduce_yourself()
    get_scientists(scientists)
    retrieve_info()
    close_br()
    info = robot.scientistlist
    print("Information is ready and will be displayed in a new tab\n")
    say_goodbye()
    display_information(info)
    

if __name__ == "__main__":
    main()
