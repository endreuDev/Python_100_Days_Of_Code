import time

print("Welcome to The Abandoned Mansion of The Oliver's!\n\n"
      "To play this game, you will need to type keywords to progress.\n"
      "Keywords will be declared as UPPER CASE characters.\n"
      "Example: There is a door in front of you. OPEN the door or GO BACK?\n"
      "In this case, you could either type OPEN or GO BACK. Any other response \n"
      "will cause a GAME OVER and you will have to start over, so pay close attention!.\n")
input("*Press 'enter' to start...*\n")
print("You arrive at the abandoned mansion of the Oliver Family.")
time.sleep(3)
print("There are rumors that deep inside of one of it's abandoned rooms,")
time.sleep(2)
print("there is an extremely valuable treasure. And you are here to find it...\n")
time.sleep(3)


def game_over(intro, death):
    print(intro)
    time.sleep(2)
    print(f"{death}\n\nGAME OVER!\n")
    input("*Press 'enter' to exit...*")


prompt = input("You find yourself at the entrance of the mansion.\n"
               "OPEN the main entrance door or go AROUND to explore?\n>")
if "open" in prompt.lower():
    prompt = input("The door is locked.\n"
                   "Use FORCE to break the door or go AROUND the mansion?\n>")
    if "force" in prompt.lower():
        print("You kick the door with all your strength and it breaks.\n"
              "You can hear the sound of wolfs howling in the distance,\n"
              "it seems you have startled them with the sound of the door breaking.")
        prompt = input("RUN inside or HIDE somewhere nearby?\n>")
        if "run" in prompt.lower():
            print("You run inside the old mansion, it's dark and it smells mold.\n"
                  "The living room has a destroyed fireplace, some furniture,\n"
                  "stairs going to the second floor and a door next to the fireplace.")
            prompt = input("EXAMINE the fireplace, go UP the stairs or OPEN the door?\n>")
            if "up" in prompt.lower():
                print("You approach the stairs and start going up, causing it to creak\n"
                      "each step you take. Arriving at the top, there is a corridor\n"
                      "leading to a few broken doors and others with ornaments in the front:\n"
                      "> one with a WIND ROSE\n"
                      "> one with a SUNFLOWER\n"
                      "> one with a BOOK\n")
                prompt = input("Which door do you want to enter?\n>")
                if "wind" in prompt.lower() or "rose" in prompt.lower():
                    print("You enter what appears to be an old office with a few maps.")
                    game_over("After a few seconds analyzing the room,you notice there\n"
                              "is a boy with a rope tied around his neck...",
                              "...before you can do anything, he simply dashes\n"
                              "in front of you and breaks your neck!")
                elif "sunflower" in prompt.lower():
                    print("You enter what appears to be a girl's room.")
                    game_over("After a few seconds analyzing the room,you notice there\n"
                              "is a girl with a blood stained dress staring at you...",
                              "...before you can do anything, she simply dashes\n"
                              "in front of you and breaks your neck!")
                elif "book" in prompt.lower():
                    prompt = input("You enter what appears to be a library. There are several books thrown\n"
                                   "around and papers ripped apart. EXAMINE bookshelves or go BACK?\n>")
                    if "examine" in prompt.lower():
                        print("As you examine the bookshelves, there is one book in particular that does not\n"
                              "seem as old as the others. You try grabbing it but it turns out that book\n"
                              "was a secret lever attached to the bookshelf.")
                        time.sleep(7)
                        print("The book triggers a mechanism that opens a secret vault that\n"
                              "was under the grand table, located at the center of the room.\n"
                              "You approach, believing the treasure is located inside this vault...")
                        time.sleep(7)
                        print("...but as you approach and see what's inside, you discover that it's empty.")
                        game_over("You turn around furious, thinking how useless this adventure was...",
                                  "...and behind you there is a man pointing a gun at you, he says:\n"
                                  "'What you are looking for belongs only to the man buried outside.'\n"
                                  "And he finally shoots at you.")
                    else:
                        game_over("You decide to go back, but as you turn around...",
                                  "...a mysterious force levitates and chokes you to death!")
                else:
                    game_over("You are uncertain which room you enter first, and while you think at the corridor...",
                              "...the wolfs found you and mauled you alive!")
            elif "open" in prompt.lower():
                print("You go to the door next to the fireplace and open it.\n"
                      "It appears you have entered the kitchen."
                      "You see what seems a little girl in the corner sobbing.")
                prompt = input("APPROACH the little girl or go BACK?\n>")
                if "approach" in prompt.lower():
                    game_over("You approach the little girl to help her, and as you approach\n"
                              "you notice that her dress has some red spots and her skin is pale...",
                              "...she turns around violently, snapping her neck,\n"
                              "jumping at you and stabbing you with a knife!")
                else:
                    game_over("You decide to go back, pretending you never saw her...",
                              "...but as you turn around, she appears in front of you,\n"
                              "holding a knife in hands and starts stabbing you as she screams!")
            else:
                game_over("You decide to stay in the living room and examine the fireplace...",
                          "...but the wolfs found you and mauled you alive!")
        else:
            game_over("You hide in a bush nearby...",
                      "...but the wolfs found you and mauled you alive!")
    else:
        print("You go around the mansion, and finds what appears to be a tombstone with a gun resting on top.")
        time.sleep(2)
        game_over("You approach to read who's name is on the grave...",
                  "...but as you do so, a mysterious force levitates and chokes you to death!")
else:
    print("You go around the mansion, and finds what appears to be a tombstone with a gun resting on top.")
    time.sleep(2)
    game_over("You approach to read who's name is on the grave...",
              "...but as you do so, a mysterious force levitates and chokes you to death!")
