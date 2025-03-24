line = "-" * 53
title = ("/,------.        ,--.   ,--.       ,--.  ,--."
         "/|  .--. ' ,---. |  |   |  |,--.--.`--',-'  '-. ,---.  "
         "/|  '--'.'| .-. :|  |.'.|  ||  .--',--.'-.  .-'| .-. : "
         "/|  |\\  \\ \\   --.|   ,'.   ||  |   |  |  |  |  \\   --. "
         "/`--' '--' `----''--'   '--'`--'   `--'  `--'   `----' /")
start_text = ("/and you are going to rewrite History"
              "/////////////////To learn how to play type \"help\" at any time,"
              "/if you want to see the welcome text, type \"h welcome\"")

help = ("/             ,--.  ,--.       ,--.           "
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
        "/if you rewrite a corrupted tile, "
        "/it is erased from existence leaving "
        "/nothing but floor behind."
        "/Be careful what you rewrite. You could end up "
        "/erasing yourself from existence if you are not careful."
        "/after you are finished with the goal in a level,"
        "/move to the time machine ' T ' and you will continue the story.")

lvl_text = [("Level 1"
             "/It's 1929 your mission is to find and kill Hitler. "
             "/\"He's an adult obviously it's wrong to kill a baby.\""
             "/this is a university campus"),
            ("Level 2"
             "//You stumble out of the time machine and are startled "
             "/by the lush trees all around you. The scientist's "
             "/voice crackles over the time machine's telecom."
             "//\"That was a warmup. we're here to see how far we can go."
             "it's 39000000 B.C. we're about to bring the dinosaurs back."),
            ("Level 3"
             "/You walk out of the time machine and are immediately blinded by an immense white light."
             "/The time machine's timer displays 00000000000"
             "//\"Where am I?\" "
             "You say as your eyes slowly adjust to the world around you."
             "/A booming voice echoes above your head"
             "/\"You have mettled with forces beyond your imagining boy.\""
             "/You lock your eyes onto an incredibly muscular old man "
             "/\"I will destroy you before you break everything!\"")]

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
        color = '\033[40m'
    elif bg_color == "RED":
        color = '\033[41m'
    elif bg_color == "GREEN":
        color = '\033[42m'
    elif bg_color == "YELLOW":
        color = '\033[43m'  # orange on some systems
    elif bg_color == "BLUE":
        color = '\033[44m'
    elif bg_color == "MAGENTA":
        color = '\033[45m'
    elif bg_color == "CYAN":
        color = '\033[46m'
    elif bg_color == "DARK_GRAY":
        color = '\033[100m'
    elif bg_color == "BRIGHT_RED":
        color = '\033[101m'
    elif bg_color == "BRIGHT_GREEN":
        color = '\033[102m'
    elif bg_color == "BRIGHT_YELLOW":
        color = '\033[103m'
    elif bg_color == "BRIGHT_BLUE":
        color = '\033[104m'
    elif bg_color == "BRIGHT_MAGENTA":
        color = '\033[105m'
    elif bg_color == "BRIGHT_CYAN":
        color = '\033[106m'
    elif bg_color == "WHITE":
        color = '\033[107m'
    return f"{color}{bg_color}{input_string}\033[0m"


def level_text(character):
    if character["level"] == 1:
        return f"{line} {title} {line} //Your name is {character["name"]} {start_text}"
    else:
        return f"{line} {title} {line} {lvl_text[character["level"] - 2]}"