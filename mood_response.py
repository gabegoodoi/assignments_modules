def mood_response(mood):
    while True:
        print(f"\nHi, I'm Mister Mood Response! I heard how you're feeling...\n")
        mood = mood.lower()
        if mood in ['1', "sad"]:
            return "You'll be okay. Let's get some dessert.\n"
            break
        elif mood in ['2', "happy"]:
            return "I've been feeling low, but your mood sure is bringing me up.\n"
        elif mood in ['3', "sleepy"]:
            return "WAKEUPWAKEUPWAKEUP\n"
        else:
            mood = input(f"{mood} is not a recognized mood (not recognized YET, just wait for Mr. Mood 2.0).\n\nTry again with a valid mood... Not to say your mood isn't valid, but you know what I mean.\n\nHow are you feeling?\n1. Sad\n2. Happy\n3. Sleepy\n")