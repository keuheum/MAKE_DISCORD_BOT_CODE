import time

print(" ")
print("Maker KeuHeum | version-1.0.0")
time.sleep(0.5)
print("This feature is used when you are bothered with creating a Discord Bot dialog.")
time.sleep(0.5)
print("Unauthorized reproduction, unauthorized distribution absolutely impossible")
time.sleep(0.5)
print(" ")

f = open("easybotchat.txt", 'w')
f.close()

user = 1
startmess = 0
imbed = 0
end = 0
message = 1

print("This word appears only in the first. Please read carefully.")
print(" ")
time.sleep(0.5)
print("If you want to go to embed, type 'Embed'")
print(" ")
time.sleep(0.5)
print("The default color for embeds is green. If you want to change it, you can do it yourself.")
print(" ")
time.sleep(0.5)
print("If you want to end it, please type 'End'")
print(" ")
time.sleep(0.5)
print("Basically, it works if the entire message sent by the user is the same as the command.")
print(" ")
time.sleep(0.5)
print("If you want the above function, please type 'Basicmessage'")
print(" ")
time.sleep(0.5)
print("If you want the starting word to be the user's command, please enter 'Startmessage'.")
print(" ")
time.sleep(0.5)


while 1:
    
    if imbed == (1): 
        while imbed == (1):
            print(" ")
            vinput = input(f"Enter the command of the {user}th user (currently embed).")
            if vinput == ("Basicmessage"):
                imbed = 0
                message = 1
                break

            elif vinput == ("Startmessage"):
                imbed = 0
                startmess = 1
                break

            elif vinput == ("End"):
                imbed = 0
                end = 1
                break

            else:
                f = open("easybotchat.txt", 'a')
                f.write("\n   ")
                f.write("\n    elif message.content == (""'" + vinput + "'""):")
                f.close()
                print(" ")
                vinput2 = input("Please write the title of the embed")
                print(" ")
                vinput = input(f"Please enter your answer to {vinput}")
                f = open("easybotchat.txt", 'a')
                f.write("\n      embed = discord.Embed(title=""'" + vinput2 + "'"", description=""'" + vinput + "'"", color=0x00ff00)")
                f.close()
                user = user + 1
                
        

    elif startmess == (1):
        while startmess == (1):
            print(" ")
            vinput = input(f"Please enter the command of the {user}th user. (Current Startmessage)")
            if vinput == ("Basicmessage"):
                startmess = 0
                message = 1
                break

            elif vinput == ("Embed"):
                startmess = 0
                imbed = 1
                break

            elif vinput == ("End"):
                startmess = 0
                end = 1
                break

            else:
                f = open("easybotchat.txt", 'a')
                f.write("\n   ")
                f.write("\n    elif message.content.startswith(""'" + vinput + "'""):")
                f.close()
                print(" ")
                vinput = input(f"Please enter your answer to {vinput}")
                f = open("easybotchat.txt", 'a')
                f.write("\n       await message.channel.send(""'" + vinput + "'"")")
                f.close()
                user = user + 1

    elif message == (1):
        while message == (1):
            print(" ")
            vinput = input(f"Please enter the command of the {user}th user. (Current Basicmessage)")
            if vinput == ("Startmessage"):
                message = 0
                startmess = 1
                break

            elif vinput == ("Embed"):
                message = 0
                imbed = 1
                break

            elif vinput == ("End"):
                message = 0
                end = 1
                break

            else:
                f = open("easybotchat.txt", 'a')
                f.write("\n   ")
                f.write("\n    elif message.content == (""'" + vinput + "'""):")
                f.close()
                print(" ")
                vinput = input(f"Please enter your answer to {vinput}")
                f = open("easybotchat.txt", 'a')
                f.write("\n       await message.channel.send(""'" + vinput + "'"")")
                f.close()
                user = user + 1
    elif end == (1):
        break


print("All commands have been entered.")
time.sleep(1)
print("Enter the following commands in your code")
time.sleep(1)
f = open("easybotchat.txt", 'r')
data = f.read()
print(" ")
print(data)
print(" ")
close = input("Press Enter to close the window")