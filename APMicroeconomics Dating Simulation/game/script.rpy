# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Micro", color="#F7C1CB")
define i = Character("Me")
# counts points that are wrong
default point = 0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene auditorium

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show micro

    # These display lines of dialogue.

    m "Welcome, it is finally you're time to shine, and win me over!"

    m "You will be scored from 0 - 5, and there will be prizes or punishments depending on what score you get as you answer my questions!"

    m "Let's get STARTED!"
    hide logo
    jump question_1

label question_options:
    scene auditorium with fade

    menu:
        "1":
            hide logo
            jump question_1
        "2":
            hide logo
            jump question_2
        "3":
            hide logo
            jump question_3
        "4":
            hide logo
            jump question_4
        "5":
            hide logo
            jump question_5


# hayun_jung question
label question_1:
    show micro
    menu:
        "When a firm is experiencing diseconomies of scale:"

        "A It should increase the size of its plant to decrease its average total costs":
            hide logo
            jump warning
        "B It should increase the amount of labor it hires":
            hide logo
            jump warning
        "C It should lower its price to the competitive level":
            hide logo
            jump warning
        "D Its average total costs will decline if it reduces its scale of operations":
            m "Good job, you scored a point"
            m "Let's move onto the next question"
            hide logo
            jump question_2

label question_2:
    show micro
    menu:
        "In the diagram it is assumed that:"
        "A The law of diminishing returns determines the shape of the cost curve.":
            hide logo
            jump warning
        "B All costs are variable":
            m "Hmmm surprisingly, persistent"
            m "Let's see if you can get the next one"
            hide logo
            jump question_3
        "C Some costs are fixed and other costs are variable.":
            hide logo
            jump warning
        "D Marginal product first falls, but ultimately rises as output is increased.":
            hide logo
            jump warning

label question_3:
    show micro
    menu:
        "A profit-maximizing firm is currently producing a quantity at which price is less than average variable cost. To maximize profit, the firm will do whihc of the following in the short run and the long run?"
        "A Shut down in the short run and exit the market in the long run.":
            m "Oh my~"
            hide logo
            jump question_4
        "B Produce less quantity in the short run and increase its scale of production in the long run.":
            hide logo
            jump warning
        "C Produce more quantity in the short run and increase its scale of production in the long run":
            hide logo
            jump warning
        "D Continue producing the same quantity in the short run and in the long run.":
            hide logo
            jump warning
        "E Continue producing the same quantity in the short and exit the market in the long run.":
            hide logo
            jump warning

label question_4:
    show micro
    menu:
        "In a comparison of a perfectly competitive firm's short-run equilibrium to its long-run equilibrium, which of the following is true?"
        "A Price must equal marginal cost in the long run, but not necessarily in the short run.":
            hide logo
            jump warning
        "B Economic profit must be positive in the long run, but not necessarily in the short run":
            hide logo
            jump warning
        "C The firm can set price in the short run, but not necessarily in the long run.":
            hide logo
            jump warning
        "D The firm must produce at minimum average total cost in the short run, but not necessarily in the long run.":
            hide logo
            jump warning
        "E Price equals average total cost in the long run, but not necessarily in the short run.":
            m "Wow you're really good at this"
            hide logo
            show blush_micro
            hide logo
            jump question_5

label question_5:
    show micro
    menu:
        "Sally quits her own job($25,000 a year) and starts her own firm. Rather than renting a building she owns to someone else for $10,000 per year, she uses it as the location for herself. Her cost for advertising during her first year are $125,000, total revenue $155,000. Economic profit?"
        "A -$5,000":
            m "..."
            m "..."
            m "DING DING DING"
            m "Congratulations let's see if I'm yours"
            hide logo
            show blush_micro
            hide logo
            jump game_ending_options
        "B $5,000":
            hide logo
            jump warning
        "C $20,000":
            hide logo
            jump warning
        "D $30,000":
            hide logo
            jump warning
        "E $120,000":
            hide logo
            jump warning

label game_ending_options:
    if point == 4:
        jump ending_1
    elif point == 3:
        jump ending_2
    elif point == 2:
        jump ending_3
    elif point == 1:
        jump ending_4
    elif point == 0:
        jump ending_5
    else:
        jump ending_0

label warning:
    $ point += 1
    scene warning with pixellate

    show warning_micro

    m "this is a warning ..."

    m "I hope you get the other questions right :)!!!!!!!!"

    m "Let's review why it's wrong"

    hide logo
    jump question_options

label ending_0:
    scene ascending_1 with pixellate
    m "You don't deserve me or the AP TEST!!"
    scene ascending_2 with fade
    show angry_micro
    m "THE MICRO GODS LOOK DOWN UPON YOU IN SHAME, ADAM SMITH DOESN'T KNOW YOU!"
    hide logo
    jump last_ending

label ending_1:
    scene auditorium with dissolve
    i "You're not going to catch me, I'm going to run!"
    scene runaway_1 with dissolve
    scene runaway_2 with dissolve
    i "I never liked you anyway!"
    scene runaway_3 with dissolve
    scene runaway_4 with dissolve
    scene runaway_5 with dissolve
    scene light with dissolve
    i "I'm free, god i hate micro, she's so mean!! ;-;"
    scene look_back with dissolve
    m "You think you could leave me :D, you thought!"

    show angry_micro
    m "You can NEVER LEAVE ME :D, you're MINE!"
    i "NOOoooo"
    hide logo
    scene dragged_1 with dissolve
    m "come study with me uwu >_<, stay beside me"
    scene dragged_2 with dissolve
    scene micro_classroom with dissolve
    m "we're here darling :D"
    jump last_ending

label ending_2:
    scene auditorium with dissolve
    show micro
    m "you're really not my type, i'm sorry"
    i "what??"
    m"sorry"
    m "micro runs away"
    hide logo
    jump last_ending

label ending_3:
    scene auditorium with dissolve
    show micro
    m "I think I don't like you that way, we should be FRIENDS instead :D"
    i "okay ;-;"
    scene commons with dissolve
    m "let's study and raise your grades in commons :D"
    i "alright"
    jump last_ending

label ending_4:
    scene upper_caf with dissolve
    show blush_micro
    m "Let's go on a date, rarely do I meet a 4!!!"
    i "OH MY GOD YES I LOVE YOU!"
    jump last_ending

label ending_5:
    scene wedding with dissolve
    show wedding_micro
    m "WE'RE GETTING MARRIED >_<"
    i " OH MY GOD I'M PERFECT AT MICRO!"
    m "You deserve me"
    jump last_ending
    #church bell music maybe?

label last_ending:
    scene ascending_1 with fade
    m "WE HAVE COME TO THE END"
    menu:
        "Choose an ending if you want to go one you missed"
        "0":
            jump ending_0
        "1":
            jump ending_1
        "2":
            jump ending_2
        "3":
            jump ending_3
        "4":
            jump ending_4
        "5":
            jump ending_5
        "none":
            "okay"
    m "Thanks to my groupmates for support and my friends."
    m "Thanks for playing"
    return
