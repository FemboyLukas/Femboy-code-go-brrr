from saver import *
quitting = False
print("Welcome to the database")
print("You have been chosen")
attempt = input("Password ").lower()
if attempt == "jay":
    print("Good")
    print("You have proved your worth. Get what you are looking for")
    while not quitting:
        file = input("Femboy pictures," +  " The bubba achives," + " Homework " + "Quit ")
        if file == "Femboy pictures":
            password = input("Extra security layer activated. Password ").lower()
            if password == "astolfo":
                save_image ("https://media.discordapp.net/attachments/841427112828993536/959483040357314600/Screenshot_20220217_213712.jpg?width=429&height=401","good boy.jpg")
                save_image ("https://media.discordapp.net/attachments/841427112828993536/959483040629932032/Screenshot_20220217_213754.jpg?width=415&height=401","based.jpg")
                save_image ("https://media.discordapp.net/attachments/841427112828993536/959483041196154971/Screenshot_20220217_213612.jpg?width=414&height=401","facts.jpg")
                print("The files have been uploaded. Have a good day cutie pie <3")
        elif file == "The bubba achives":
            password = input("Extra security layer activated. Password ").lower()
            if password == "lord fatass":
                print("Im sorry sir but even with your security clearence these files are still heavily restricted. If you think this is a mistake please check with Bubbasholder")
        elif file == "Homework":
            password = input("Extra security layer activated. Password ").lower()
            if password == "i like boys":
                save_image("https://media.discordapp.net/attachments/841427112828993536/960579231656607834/unknown.png?width=346&height=400","Good times.jpg")
                save_image("https://media.discordapp.net/attachments/841427112828993536/960579340494589962/unknown.png?width=275&height=400","Sissy.jpg")
                save_image("https://media.discordapp.net/attachments/841427112828993536/960579670175256656/unknown.png?width=301&height=401","Use me.jpg")
        if file == "Quit":
            print("System failing. Fuck")
            quitting = True