def input_color(input_string, color, bg_color=""):
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


def level_text(character):
    if character["level"] == 1:
        return (f"{line} {title} {line} //You wake up in a laboratory. "
                f"/You don't remember anything except this."
                f"//Your name is {character["name"]} {start_text}")
    else:
        return f"{line} {level_ascii[character["level"] - 2]} {line} {lvl_text[character["level"] - 2]}"


line = "-" * 53
title = ("/,------.        ,--.   ,--.       ,--.  ,--."
         "/|  .--. ' ,---. |  |   |  |,--.--.`--',-'  '-. ,---.  "
         "/|  '--'.'| .-. :|  |.'.|  ||  .--',--.'-.  .-'| .-. : "
         "/|  |\\  \\ \\   --.|   ,'.   ||  |   |  |  |  |  \\   --. "
         "/`--' '--' `----''--'   '--'`--'   `--'  `--'   `----' /")
level_ascii = ("/,--.                         ,--.     ,--."
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

start_text = ("/and you are going to rewrite History"
              "//looking around you see a very simple room."
              "/with no decorations just a man with wild hair, "
              "/a training dummy and some kind of large glowing device."
              "/\"Ah I see you've woken up. I'm Professor Hart. I'll be guiding you today..."
              "/wrong choice of words.\" he awkwardly laughs scratches his head."
              "/\"Take this device you'll need it for your mission.\""
              "/he hands you a gun. \"It's not a gun! Here. Walk to the training dummy using wasd."
              "/and type r then 'w', 'a', 's', or 'd' (in whichever direction the dummy is in)"
              "/(eg. \"rw\" to rewrite up)."
              "/////To learn how to play type \"help\" at any time,"
              "/if you want to see the welcome text, type \"h welcome\"/")

help_text = ("/             ,--.  ,--.       ,--.           "
             "/             |  '--'  | ,---. |  | ,---.     "
             "/             |  .--.  || .-. :|  || .-. |    "
             "/             |  |  |  |\\   --.|  || '-' '    "
             "/             `--'  `--' `----'`--'|  |-'     "
             "/----------------------------------`--'---------------/"
             "/Welcome to Rewrite!"
             "/To move use 'w' to move up, 'a' to move left "
             "/'s' to move down and 'd' to move right. "
             "//To rewrite an area type 'r' and the direction "
             "/you are rewriting. ('w', 'a', 's', or 'd')"
             "/Once anything is rewritten it will display as a corrupted tile."
             "/corrupted tiles change your perception of reality, and act as barriers."
             "/however the space surrounding remains the same even if it looks different."
             "/if you rewrite a corrupted tile, "
             "/it is erased from existence leaving "
             "/nothing but floor behind."
             "/Be careful what you rewrite. You could end up "
             "/erasing yourself from existence if you are not careful."
             "/after you are finished with the goal in a level,"
             "/move to the time machine ' T ' and you will continue the story.")

lvl_text = [("/"
             "/You step through the door of the time machine into a nearly empty decidedly German university."
             "//The professor's voice crackles over the time machine's telecom."
             "/\"It's 1929. Your mission is to find and kill Hitler. "
             "/He's an adult. obviously it's wrong to kill a baby.\""
             "/He's still an art student so this should be easy."
             "/oh and try not to kill anyone else. "
             "/there's almost a 100% chance you'd be related to them."
             f"//{input_color("\"Again rewrite a space once to make a wall.", "BRIGHT_GREEN", "BLACK")}"
             f"/{input_color("rewrite twice to make a floor.", "BRIGHT_GREEN", "BLACK")}"
             "//////To learn how to play type \"help\" at any time,"
             "/if you want to see the welcome text, type \"h welcome\"/"),
            ("/"
             "/You stumble out of the time machine and are startled "
             f"/by the lush trees all around you. "
             f"//The professor's voice crackles over the time machine's telecom."
             f"//\"That was a warmup. we're here to see how far we can go."
             f"/it's 39000000 B.C. we're about to bring the dinosaurs back."
             f"//You look above your head and see a meteor hurtling down towards the ground"
             f"/based on the trajectory you are estimating that it will "
             f"/land where the \"{input_color(" M ", "RED")}\" is in one minute."
             f"/you get a feeling that if you rewrite all of the \"{input_color(" M ", "RED")}\" "
             f"/the meteor will be shot into another dimension."
             "//////To learn how to play type \"help\" at any time,"
             "/if you want to see the welcome text, type \"h welcome\"/"
             ),
            ("/"
             "/You walk out of the time machine and are immediately blinded by an immense white light."
             "/The time machine's timer displays 00000000000"
             "//\"Where am I?\" "
             "You say as your eyes slowly adjust to the world around you."
             "/A booming voice echoes above your head"
             "/\"You have meddled with forces beyond your imagining boy.\""
             "/You lock your eyes onto an incredibly muscular old man "
             "/\"I will destroy you before you break everything!\""
             "//////To learn how to play type \"help\" at any time,"
             "/if you want to see the welcome text, type \"h welcome\"/"
             )]

colors = ["RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "BRIGHT_RED",
          "BRIGHT_GREEN", "BRIGHT_YELLOW", "BRIGHT_BLUE", "BRIGHT_MAGENTA", "BRIGHT_CYAN"]

end_txt = [f"{line} {title} {line} //{input_color("With a blast from your not-gun ", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("the dummy is replaced with a strange quickly ", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("shifting assortment of materials and shapes", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("as you stare into it your eyes start to hurt and you get a headache.", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("The room seems to bend and shift and warp and reverse ", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("over the crazy scar in reality.", "BRIGHT_BLUE", "BLACK")}"
           f"//{input_color("\"I see you got the hang of it. Don't stare for too long.", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("As you go further back in time, you will accumulate more time manipulation spacial signifiers creating a hex field study stratosphere. These hex field study stratosphere will allow the area of your cardo babble hypodron to expand exponentially and cause a sonic reflux dip in the corival terisalinux. it works by using wormhole theory to link a space to every point of the fourth dimension of time. effectively creating a wall. using it again will shift that time link to an entirely different spacial dimension, and link a separate empty spacial dimension to that space. \"", "BRIGHT_BLUE", "BLACK")}"
           f"/"
           f"/{input_color("As the professor babbles on and on you feel impatient.", "BRIGHT_BLUE", "BLACK")}"
           f"/"
           f"/{input_color("Sensing this he says: ", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("\"Sorry, in layman's terms, use that gun to rewrite a space to make a wall.", "BRIGHT_GREEN", "BLACK")}"
           f"/{input_color("if you use it again on the same space it will turn the wall into a floor.", "BRIGHT_GREEN", "BLACK")}"
           f"/{input_color("as you go further back in time it will get more powerful.\"", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("that big device", "BRIGHT_BLUE", "BLACK")}"
           f"{input_color(" T ", "BRIGHT_BLUE", "DARK_GRAY")}"
           f"{input_color(" in the room is a time machine. Enter it and you will start your first mission", "BRIGHT_BLUE", "BLACK")}"
           f"///////////",
           f"/{line} {level_ascii[0]} {line} //"
           f"/{input_color("With a blast from your Rewriter ", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("Hitler is replaced with an assortment of baked goods from the Phoenician era,", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("which quickly shifts into something else.", "BRIGHT_BLUE", "BLACK")}"
           f"/"
           f"/{input_color("\"Good job, it looks like you did your mission.", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("the device says here that you killed a man called", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("Adolf? Heighter? no Hitter. Eh I don't know my german names.", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("Well I don't know why we had you do that, we should've had you kill Meinard Goudier.", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("anyways go back to the time machine for your next mission.\"", "BRIGHT_BLUE", "BLACK")}"
           f"////////////",
           f"/{line} {level_ascii[1]} {line} //"
           f"/{input_color("The Meteors are stopped in their tracks.", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("you expect to hear something over the time machine's telecom like last time", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("but you don't hear anything.", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("you have a bad feeling but there's nothing to do but enter the time machine", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("and see what fate has in store for you.", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("proceed to the time machine to continue.", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("", "BRIGHT_BLUE", "BLACK")}"
           f"////////////",
           f"/{line} {level_ascii[2]} {line}"
           f"/{input_color("", "BRIGHT_BLUE", "BLACK")}"
           
           f"/{input_color("As the world around you warps and strains at the tears in reality", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("made by the battle, The man Yells", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("\"I am the GREATEST-GRANDFATHER, I CANNOT BE DEFEATED!\"", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("Slowly the man fades away into nothingness and", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("closes his eyes in defeat \"you will regret this day...", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("I certainly did...\"", "BRIGHT_BLUE", "BLACK")}"
           f"/{input_color("", "BRIGHT_BLUE", "BLACK")}"
           f"////////////"
           ]

win = (f"\n\n\n\n\n\n,--.   ,--.                 ,--.   ,--.,--.         "
       f"\n \\  `.'  /,---. ,--.,--.    |  |   |  |`--',--,--,  "
       f"\n  '.    /| .-. ||  ||  |    |  |.'.|  |,--.|      \\ "
       f"\n    |  | ' '-' ''  ''  '    |   ,'.   ||  ||  ||  | "
       f"\n    `--'  `---'  `----'     '--'   '--'`--'`--''--' "
       f"\n\n\n\n\n\nYou enter the time machine and come to a new understanding of... something or other"
       f"\nI'm sure there is something profound I can write here but you'll have to"
       f"\njust imagine some kind of profound ending instead."
       f"\n\n\n\n\n\nThank you Chris for playing the game and making a fun assignment, please give me a good grade lol")