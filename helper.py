import textwrap
import time

# HELPER FUNCTIONS | Call them by helper.('fn-name')
# pause(n)              - freezes the program for n seconds
# refresh(n, title)     - refreshes the screen. params not required: 
#                                  n        - how many lines. 
#                                  title    - what to print in the box
# press_any_key()       - allows to pause for user to read

WIDTH = 64
PADDING = 8
REFRESH = 50
DELAY = 0.03
# DELAY = 0.03 original
PAUSE = 1.3
# PAUSE = 1 original



def print_menu(text, title="FOOD HEALTH ESTIMATOR v.0.21",response = True):
    # prints the menu
    print_with_line(text, ref=True, n=0, title=title)
    # get and returns the response
    if response:
        answer = press_any_key(s ="Enter your choice\n> ", inp = True)
        return(answer)




def pause(t = PAUSE):
    time.sleep(t)

def refresh(n=REFRESH, title = "FOOD HEALTH ESTIMATOR v.0.21"):
    title = "  "+str(title)+"  "

    title_width = len(title)
    left_n = int((WIDTH - (title_width + 4) )/2) # first_side_width
    right_n  = WIDTH - title_width - left_n - 4 # last_side_width

    print("\n" * n)
    print(" {}┌{}┐{}".format(left_n*" ",title_width*"─",right_n*" "))
    pause(DELAY)
    print("┌{}│{}│{}┐".format(left_n*"─",title,right_n*"─"))
    pause(DELAY)
    print("│{}└{}┘{}│".format(left_n*" ",title_width*"─",right_n*" "))
        



def print_with_line(string, width = WIDTH, ref = True, n = REFRESH, title = "FOOD HEALTH ESTIMATOR v.0.21"):
    final_string = []
    adjusted_w = WIDTH - PADDING*2
    # split by newline chars into a list
    string = string.split('\n')

    # go threouh each item and see if it needs another split
    for item in string:
        item = textwrap.dedent(item)
        item_wrap = textwrap.wrap(text=item, width = adjusted_w)
        # add the smallest chunks to the final string
        final_string += item_wrap

    print_frame(final_string, width = WIDTH, ref = ref, title  = title, n = n)
    return


def wrap(string, width = WIDTH):
    adjusted_w = WIDTH - PADDING
    shortened = textwrap.shorten(text=string, width=adjusted_w)
    shortened_wrapped = textwrap.fill(text=shortened)
    return shortened_wrapped


def print_frame(string_split_final, 
                width = WIDTH, 
                ref = True, 
                title = "FOOD HEALTH ESTIMATOR v.0.21", 
                n = REFRESH):
    refresh(title = title, n = n) if ref else draw_top()
    # │        Hi there! Welcome to the food health estimator!        │

    for line in [" "]+string_split_final+[" "]:
        emoji_count = str(line.encode("utf-8")).count("xf0")

        cur_text_width  = len(line)
        whitespace      = WIDTH - 2 - cur_text_width - emoji_count # -2: there are two border chars 
        left_pad        = round((whitespace)/2)
        right_pad       = whitespace - left_pad
        total_len       = len(line)+left_pad+right_pad+2
        print("│{}{}{}│".format(left_pad*" ",line,right_pad*" ") )
        pause(DELAY)

    draw_bottom()


def draw_top(n = WIDTH):
    print("{}{}{}".format("┌","─"*(WIDTH-2),"┐" ))

def draw_bottom(n = WIDTH):
    print("{}{}{}".format("└","─"*(WIDTH-2),"┘" ))


def simple_print(string):
    for line in string.split('\n'):
        print(line)
        pause(DELAY)

def press_any_key(s="...Press ENTER to continue!\n", inp = True, n=DELAY):
    for i in s:
        print(i, end = "", flush = True)
        pause(n)
    if inp:
        user_in = input("")
        return user_in