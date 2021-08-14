from tkinter import *

root = Tk()
root.title("Guess Your Own Path Game")

ask_name = Label(root, text="What is your name?")
name_player_field = Entry(root, width=50)
ask_friend = Label(root, text="What is your friends name in this adventure?")
name_friend_field = Entry(root, width=50)



# greeting = Label(root, text="Hello " + name_player + " and welcome to your adventure game! There will be different paths depending on what you choose.")

names = []
go_button = Button(root, text="GO")

def gofunc():
    name_player_gofunc = name_player_field.get()
    names.append(name_player_gofunc)
    name_friend_gofunc = name_friend_field.get()
    names.append(name_friend_gofunc)
    gofunc.greeting = Label(root, text="Hello " + name_player_gofunc + " and welcome to your adventure game! There will be different paths depending on what you choose.")
    gofunc.next_greet = Label(root, text="Good luck and have fun")
    gofunc.ok_button = Button(root, text="OK", command=start_func)

    name_player_field.destroy()
    ask_name.destroy()
    name_friend_field.destroy()
    ask_friend.destroy()
    go_button.destroy()

    gofunc.greeting.pack()
    gofunc.next_greet.pack()
    gofunc.ok_button.pack()
    
    
   
def start_func():
    name_player = names[0]
    name_friend = names[1]

    gofunc.greeting.destroy()
    gofunc.next_greet.destroy()
    gofunc.ok_button.destroy()

    start_func.start_path = Label(root, text="Where would you like to start?" )
    start_func.option1 = Button(root, text="Your friend " + name_friend + "'s house", command=house_start)
    start_func.orlabel = Label(root, text="OR")
    start_func.option2 = Button(root, text="The neighborhood Park")


    start_func.start_path.pack()
    start_func.option1.pack()
    start_func.orlabel.pack()
    start_func.option2.pack()

def house_start():
    name_player = names[0]
    name_friend = names[1]
    start_func.start_path.destroy()
    start_func.option1.destroy()
    start_func.orlabel.destroy()
    start_func.option2.destroy()

    house_start.start = Label(root, text="You are in "+ name_friend + "'s bedroom. When " + name_friend + " says")
    house_start.start1 = Label(root, text='"Hey I\'m pretty bored. What do you want to do? I feel like going to the old')
    house_start.start2 = Label(root, text='abandoned house down the road. You want to go?"')

    house_start.button_go = Button(root, text="Yea sure lets go!")
    house_start.button_stay = Button(root, text="Uhm im not quite sure about that. Maybe we should just get ice cream instead")


    house_start.start.pack()
    house_start.start1.pack()
    house_start.start2.pack()




    



go_button = Button(root, text="GO", command=gofunc)
ask_name.pack()
name_player_field.pack()
ask_friend.pack()
name_friend_field.pack()
go_button.pack()






# print()
# start_decision = int(input("Where would you like to start? \n1) Your Friend " + name_friend + "'s house \nor \n2) the neighborhood park"))



root.mainloop()
