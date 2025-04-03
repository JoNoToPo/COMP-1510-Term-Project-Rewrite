import random


def input_color(input_string: str, color: str, bg_color=""):
    """
    Inserts text color and optionally a background color into a string.

    :precondition: three strings
    :postcondition: a string
    :param input_string: a string
    :param color: an all caps string defining and limited to the terminal text color options
    :param bg_color: an all caps string limited to the terminal background color options
    :return: a string with the correct text color and background color
    """
    if color == "BLACK":
        color = "\033[30"
    elif color == "RED":
        color = '\033[31m'
    elif color == "GREEN":
        color = '\033[32m'
    elif color == "YELLOW":
        color = '\033[33m'
    elif color == "BLUE":
        color = '\033[34m'
    elif color == "MAGENTA":
        color = '\033[35m'
    elif color == "CYAN":
        color = '\033[36m'
    elif color == "LIGHT_GRAY":
        color = '\033[37m'
    elif color == "DARK_GRAY":
        color = '\033[90m'
    elif color == "BRIGHT_RED":
        color = '\033[91m'
    elif color == "BRIGHT_GREEN":
        color = '\033[92m'
    elif color == "BRIGHT_YELLOW":
        color = '\033[93m'
    elif color == "BRIGHT_BLUE":
        color = '\033[94m'
    elif color == "BRIGHT_MAGENTA":
        color = '\033[95m'
    elif color == "BRIGHT_CYAN":
        color = '\033[96m'
    elif color == "WHITE":
        color = '\033[97m'
    if bg_color == "BLACK":
        bg_color = '\033[40m'
    elif bg_color == "RED":
        bg_color = '\033[41m'
    elif bg_color == "GREEN":
        bg_color = '\033[42m'
    elif bg_color == "YELLOW":
        bg_color = '\033[43m'  # orange on some systems
    elif bg_color == "BLUE":
        bg_color = '\033[44m'
    elif bg_color == "MAGENTA":
        bg_color = '\033[45m'
    elif bg_color == "CYAN":
        bg_color = '\033[46m'
    elif bg_color == "DARK_GRAY":
        bg_color = '\033[100m'
    elif bg_color == "BRIGHT_RED":
        bg_color = '\033[101m'
    elif bg_color == "BRIGHT_GREEN":
        bg_color = '\033[102m'
    elif bg_color == "BRIGHT_YELLOW":
        bg_color = '\033[103m'
    elif bg_color == "BRIGHT_BLUE":
        bg_color = '\033[104m'
    elif bg_color == "BRIGHT_MAGENTA":
        bg_color = '\033[105m'
    elif bg_color == "BRIGHT_CYAN":
        bg_color = '\033[106m'
    elif bg_color == "WHITE":
        bg_color = '\033[107m'
    return f"{color}{bg_color}{input_string}\033[0m"


def level_text(character: dict):
    """
    Returns the level text given the character's level

    :precondition: a dictionary
    :postcondition: a string
    :param character: a dictionary with at minimum the keys 'level' and 'name'
    :return: a string containing the level text
    """
    line = "-" * 53
    level_ascii = ("/,------.        ,--.   ,--.       ,--.  ,--."
                   "/|  .--. ' ,---. |  |   |  |,--.--.`--',-'  '-. ,---.  "
                   "/|  '--'.'| .-. :|  |.'.|  ||  .--',--.'-.  .-'| .-. : "
                   "/|  |\\  \\ \\   --.|   ,'.   ||  |   |  |  |  |  \\   --. "
                   "/`--' '--' `----''--'   '--'`--'   `--'  `--'   `----' /",
                   "/,--.                         ,--.     ,--."
                   "/|  |    ,---.,--.  ,--.,---. |  |    ,   |"
                   "/|  |   | .-. :\\  `'  ,| .-. :|  |    `|  | "
                   "/|  '--.\\   --. \\    , \\   --.|  |     |  | "
                   "/`-----' `----'  `--'   `----'`--'     `--'/",
                   "/,--.                         ,--.     ,---.  "
                   "/|  |    ,---.,--.  ,--.,---. |  |    '.-.  \\ "
                   "/|  |   | .-. :\\  `'  ,| .-. :|  |     .-' .' "
                   "/|  '--.\\   --. \\    , \\   --.|  |    |   '-. "
                   "/`-----' `----'  `--'   `----'`--'    '-----' /",
                   "/,--.                         ,--.    ,----.  "
                   "/|  |    ,---.,--.  ,--.,---. |  |    '.-.  | "
                   "/|  |   | .-. :\\  `'  ,| .-. :|  |      .' <  "
                   "/|  '--.\\   --. \\    , \\   --.|  |    ,'-'  | "
                   "/`-----' `----'  `--'   `----'`--'    `----' /")
    preamble = (f"//You \"{input_color(" @ ", "GREEN")}\" wake up in a laboratory. "
                f"/You don't remember anything except this."
                f"//Your name is {character["name"]} /and you are going to rewrite History",
                "",
                "",
                "",
                "",)
    lvl_text = [(f"/"
                 f"/looking around you see a very simple room."
                 f"/with no decorations just a man with wild hair, \"{input_color(" P ", "YELLOW")}\""
                 f"/a training dummy \"{input_color(" D ", "RED")}\" and some kind of large glowing device."
                 f" \"{input_color(" T ", "DARK_GRAY", "BRIGHT_BLUE")}\""
                 f"/\"Ah I see you've woken up. I'm Professor Hart. \"{input_color(" P ", "YELLOW")}\" "
                 f"/I'll be guiding you today... wrong choice of words.\" "
                 f"/he awkwardly laughs scratches his head."
                 f"//\"Take this device, you'll need it for your mission.\""
                 f"/he hands you a gun. "
                 f"/\"It's not a gun! It's a rewriting device. "
                 f"/Walk to the training dummy \"{input_color(" D ", "RED")}\" using wasd."
                 "/once you reach the dummy, type r then 'w', 'a', 's', or 'd' to rewrite the dummy"
                 "/(in whichever direction the dummy is in)\""
                 "/(eg. type \"rw\" then press enter to rewrite up)."
                 "(If I am blocking your way, please don't kill me. "
                 "/ you can rewrite walls and rewrite rewritten tiles into floor tiles to get around me.)"
                 "//To learn how to play type \"help\" at any time,"
                 "/if you want to see the welcome text, type \"level text\"/"),
                ("/"
                 "/You step through the door of the time machine into a nearly empty but decidedly German university."
                 "//The professor's voice crackles over the time machine's telecom."
                 f"/\"It's 1929. {character["name"]} Your mission is to find and kill Hitler. "
                 "/He's an adult. obviously it's wrong to kill a baby.\""
                 "/He's still trying to become an art student so this should be easy."
                 "/oh and try not to kill anyone else. "
                 f"/{input_color("\"and your rewrite device is more powerful now so be careful", "BRIGHT_GREEN", "BLACK")}"
                 "/there's almost a 100% chance you'd be related to them."
                 f"//{input_color("\"Again rewrite a space once to make a wall.", "BRIGHT_GREEN", "BLACK")}"
                 f"/{input_color("rewrite twice to make a floor.", "BRIGHT_GREEN", "BLACK")}"
                 f"//As you walk the halls you see"
                 f"/a very angry man \"{input_color(" H ", "RED")}\" yelling in german with a hitler moustache "
                 f"/brandishing a very real gun while shooting"
                 f" it in random directions \"{input_color(" • ", "BRIGHT_RED")}\""
                 "//////To learn how to play type \"help\" at any time,"
                 "/if you want to see the welcome text, type \"level text\"/"),
                ("/"
                 "/You stumble out of the time machine and are startled "
                 f"/by the cavemen \"{input_color(" G ", "YELLOW")}\" and the lush trees all around you. "
                 f"it's night but somehow everything is illuminated by a red, firey light."
                 f"//The professor's voice crackles over the time machine's telecom."
                 f"//\"That was a warmup. We're here to see how far we can go."
                 f"/it's 39000000 B.C. we're about to bring the dinosaurs back."
                 f"//You look directly above head and see a massive meteor \"{input_color(" M ", "RED")}\" hurtling down towards the ground"
                 f"/with many mini bits breaking off and striking the ground before the main body. \"{input_color(" • ", "BRIGHT_RED")}\""
                 f"/based on the trajectory of the meteor you are estimating that it will "
                 f"/land where the \"{input_color(" M ", "RED")}\" is in less than one minute!"
                 f"//You get a feeling that if you rewrite all of the \"{input_color(" M ", "RED")}\" "
                 f"/the meteor will be shot into another dimension."
                 "//////To learn how to play type \"help\" at any time,"
                 "/if you want to see the welcome text, type \"level text\"/"
                 ),
                ("/"
                 "/You walk out of the time machine and are immediately blinded by an immense white light."
                 "/The time machine's timer displays 00000000000"
                 "//\"Where am I?\" "
                 "You say as your eyes slowly adjust to the world around you."
                 "/A booming voice echoes above your head"
                 "/\"You have meddled with forces beyond your imagining boy.\""
                 f"/You lock your eyes onto an incredibly muscular old man \"{input_color(" G ", "WHITE", "BRIGHT_RED")}\""
                 "/\"I will destroy you and your time machine before you break everything!\""
                 "//////To learn how to play type \"help\" at any time,"
                 "/if you want to see the level text, type \"level text\"/"
                 )]
    return (f"{line} {level_ascii[character["level"] - 1]} {line} {preamble[character["level"] - 1]}"
            f" {lvl_text[character["level"] - 1]}")


def end_txt(character: dict):
    line = "-" * 53
    level_ascii = ("/,------.        ,--.   ,--.       ,--.  ,--."
                   "/|  .--. ' ,---. |  |   |  |,--.--.`--',-'  '-. ,---.  "
                   "/|  '--'.'| .-. :|  |.'.|  ||  .--',--.'-.  .-'| .-. : "
                   "/|  |\\  \\ \\   --.|   ,'.   ||  |   |  |  |  |  \\   --. "
                   "/`--' '--' `----''--'   '--'`--'   `--'  `--'   `----' /",
                   "/,--.                         ,--.     ,--."
                   "/|  |    ,---.,--.  ,--.,---. |  |    ,   |"
                   "/|  |   | .-. :\\  `'  ,| .-. :|  |    `|  | "
                   "/|  '--.\\   --. \\    , \\   --.|  |     |  | "
                   "/`-----' `----'  `--'   `----'`--'     `--'/",
                   "/,--.                         ,--.     ,---.  "
                   "/|  |    ,---.,--.  ,--.,---. |  |    '.-.  \\ "
                   "/|  |   | .-. :\\  `'  ,| .-. :|  |     .-' .' "
                   "/|  '--.\\   --. \\    , \\   --.|  |    |   '-. "
                   "/`-----' `----'  `--'   `----'`--'    '-----' /",
                   "/,--.                         ,--.    ,----.  "
                   "/|  |    ,---.,--.  ,--.,---. |  |    '.-.  | "
                   "/|  |   | .-. :\\  `'  ,| .-. :|  |      .' <  "
                   "/|  '--.\\   --. \\    , \\   --.|  |    ,'-'  | "
                   "/`-----' `----'  `--'   `----'`--'    `----' /")
    with_a_random_thing_from_history = (f"{random.choices(["with an assortment of greco-roman jewelery",
                                                           "with a complete garbled mess of shapes and colors",
                                                           "with a pile of cow turds and"
                                                           " an Armenian shovel from the 17th century",
                                                           "with a slightly tattered painting of Andrew Jackson",
                                                           "with an assortment of baked goods "
                                                           "from the Phoenician era"])[0]}"
                                        f" which quickly shifts into something else.")
    output = ["",
              f"{line} {level_ascii[0]} {line} //{input_color("With a blast from your not-gun ", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("the dummy is replaced with a strange quickly ", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("shifting assortment of materials and shapes", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("as you stare into it your eyes start to hurt and you get a headache.", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("The room seems to bend and shift and warp and reverse ", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("over the crazy scar in reality.", "BRIGHT_BLUE", "BLACK")}"
              f"//{input_color("\"Congratulations you rewrote whatever was there...", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("it would make sense if it was a dummy.", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("Oh, and don't stare for too long. You could lose your mind.", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("As you go further back in time, you will accumulate more time manipulation spacial signifiers"
                              " creating a hex field study stratosphere. These hex field study stratospheres will"
                              " allow the area of your cardo babble hypodron to expand exponentially and cause a"
                              " sonic reflux dip in the corival terisalinux. it works by using wormhole theory to"
                              " link a space to every point of the fourth dimension of time. effectively creating a wall."
                              " Using it again will shift that time link to an entirely different spacial dimension, and"
                              " link a separate empty spacial dimension to that space. \"", "BRIGHT_BLUE", "BLACK")}"
              f"/"
              f"/{input_color("As the professor babbles on and on you feel impatient.", "BRIGHT_BLUE", "BLACK")}"
              f"//{input_color("Sensing this he says: ", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("\"Sorry, in layman's terms, the rewrite device will get more powerful"
                              " and rewrite more area as you progress.", "BRIGHT_GREEN", "BLACK")}"
              f"/{input_color("if you use it once it will rewrite a space to make a wall.", "BRIGHT_GREEN", "BLACK")}"
              f"/{input_color("and if you use it again on the same space it will turn the wall into a floor.", "BRIGHT_GREEN", "BLACK")}"
              f"/{input_color("as you go further back in time it will get more powerful.\"", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("that big device", "BRIGHT_BLUE", "BLACK")}"
              f"{input_color(" T ", "DARK_GRAY", "BRIGHT_BLUE")}"
              f"{input_color(" in the room is a time machine. Enter it and you will start your first mission", "BRIGHT_BLUE", "BLACK")}"
              f"///////////",
              f"/{line} {level_ascii[1]} {line} //"
              f"/{input_color("With a blast from your Rewriter ", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color(f"Hitler is replaced {with_a_random_thing_from_history},", "BRIGHT_BLUE", "BLACK")}"
              f"/"
              f"/{input_color("\"Good job, it looks like you did your mission.", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("the device says here that you killed a man called", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("Adolf? Heighter? no Hitter. Eh I don't know my german names.", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("Well I don't know why we had you do that, we should've had you kill Meinard Goudier.", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("anyways go back to the time machine for your next mission.\"", "BRIGHT_BLUE", "BLACK")}"
              f"////////////",
              f"/{line} {level_ascii[2]} {line} //"
              f"/{input_color("After your preparation, the meteors fall into spaces replaced", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color(f"{with_a_random_thing_from_history}", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("you expect to hear something over the time machine's telecom like last time", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("but you don't hear anything.", "BRIGHT_BLUE", "BLACK")}"
              f"//{input_color("You have a bad feeling, but there's nothing to do but enter the time machine", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("and see what fate has in store for you.", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("proceed to the time machine to continue.", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("", "BRIGHT_BLUE", "BLACK")}"
              f"////////////",
              f"/{line} {level_ascii[3]} {line}"
              f"/{input_color("", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("As the world around you warps and strains at the tears in reality", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("created by the battle, The man Yells", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("\"I am the GREATEST-GRANDFATHER, I CANNOT BE DEFEATED!\"", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("Slowly the man fades away into nothingness and", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("closes his eyes in defeat. \"You will regret this day...", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("I certainly did...\"", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("With that ominous message hanging in the air you can't ", "BRIGHT_BLUE", "BLACK")}"
              f"/{input_color("think of anything to do except go back to your time machine", "BRIGHT_BLUE", "BLACK")}"
              f"////////////"
              ]
    return output[character["level"] - 1]
