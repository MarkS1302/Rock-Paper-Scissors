# PythonGeeks - import library
import random
from tkinter import *
from tkinter import ttk
from tkinter import Tk, Label
from tkinter import Button, PhotoImage


# CONTINUE BUTTON
def continue_clicked():
    name = name_entry.get()
    popup.destroy()  # Close the popup window
    main_window(name)  # Open the main window


# MAIN GAME
def main_window(name):
    root = Tk()
    root.title("ROCK, PAPER, SCISSOR GAME USING PYTHONGEEKS")
    width = 650
    height = 700
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    x = (window_width / 2) - (width / 2)
    y = (window_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    root.config(bg="white")

    # BACKGROUND IMAGE

    # PythonGeeks- Function for making rock paper scissor
    def Rock():
        global player_option
        player_option = 1
        Image_Player.configure(image=Player_Rock)
        Matching()

    def Paper():
        global player_option
        player_option = 2
        Image_Player.configure(image=Player_Paper)
        Matching()

    def Scissor():
        global player_option
        player_option = 3
        Image_Player.configure(image=Player_Scissor)
        Matching()

    # PythonGeeks- Function for making rock paper scissor for computer

    def Comp_Rock():
        if player_option == 1:
            Label_Status.config(text="  Game  \n"" Tie ", bg="#FFBE6A")
        elif player_option == 2:
            Label_Status.config(text=" Player \n"" Win ", bg="#00FF00")
        elif player_option == 3:
            Label_Status.config(text="Computer\n"" Win ", bg="#FF0000")

    def Comp_Paper():
        if player_option == 1:
            Label_Status.config(text="Computer\n"" Win ", bg="#FF0000")
        elif player_option == 2:
            Label_Status.config(text="  Game  \n"" Tie ", bg="#FFBE6A")
        elif player_option == 3:
            Label_Status.config(text=" Player \n"" Win ", bg="#00FF00")

    def Comp_Scissor():
        if player_option == 1:
            Label_Status.config(text=" Player \n"" Win ", bg="#00FF00")
        elif player_option == 2:
            Label_Status.config(text="Computer\n"" Win ", bg="#FF0000")
        elif player_option == 3:
            Label_Status.config(text="  Game  \n"" Tie ", bg="#FFBE6A")

    # Function for matching

    def Matching():
        computer_option = random.randint(1, 3)
        if computer_option == 1:
            Image_Computer.configure(image=Computer_Rock)
            Comp_Rock()

        elif computer_option == 2:
            Image_Computer.configure(image=Computer_Paper)
            Comp_Paper()

        elif computer_option == 3:
            Image_Computer.configure(image=Computer_Scissor)
            Comp_Scissor()

    def Exit():
        root.destroy()
        exit()

    Blank_img = PhotoImage(file="resources/blank.png")
    Player_Rock = PhotoImage(file="resources/rock_player.png")
    Player_Paper = PhotoImage(file="resources/paper_player.png")
    Player_Scissor = PhotoImage(file="resources/scissor_player.png")
    Computer_Rock = PhotoImage(file="resources/rock_computer.png")
    Computer_Paper = PhotoImage(file="resources/paper_computer.png")
    Computer_Scissor = PhotoImage(file="resources/scissor_computer.png")
    Image_Player = Label(root, image=Blank_img)
    Image_Computer = Label(root, image=Blank_img)
    Label_Player = Label(root, text=format(name))
    Label_Player.grid(row=1, column=1)
    Label_Player.config(bg="white", fg="black", font=('Arial', 18, 'bold'))
    Label_Computer = Label(root, text="COMPUTER")
    Label_Computer.grid(row=1, column=3)
    Label_Computer.config(bg="white", fg="black", font=('Arial', 18, 'bold'))
    Label_Status = Label(root,bg="white", text="", font=('Arial', 12))
    Label_Status.config(fg="black", font=('Arial', 20, 'bold', 'italic'))
    Image_Player.grid(row=2, column=1, padx=30, pady=20)
    Image_Computer.grid(row=2, column=3, pady=20)
    Label_Status.grid(row=3, column=2)

    rock_img = PhotoImage(file="resources/rock_player.png").subsample(3, 3)
    paper_img = PhotoImage(file="resources/paper_player.png").subsample(3, 3)
    scissor_img = PhotoImage(file="resources/scissor_player.png").subsample(3, 3)

    rock = Button(root, image=rock_img, command=Rock, borderwidth=7)
    rock.image = rock_img
    paper = Button(root, image=paper_img, command=Paper, borderwidth=7)
    paper.image = paper_img
    scissor = Button(root, image=scissor_img, command=Scissor, borderwidth=7)
    scissor.image = scissor_img
    button_quit = Button(root, text="Quit", bg="red", fg="white", font=('Arial', 15, 'bold'),
                         activebackground="dark red", activeforeground="white", relief="groove", command=Exit)

    rock.grid(row=4, column=1, pady=30)
    paper.grid(row=4, column=2, pady=30)
    scissor.grid(row=4, column=3, pady=30)
    button_quit.grid(row=5, column=2)


# NEW POPUP WINDOW TO INSERT THE NAME OF THE PLAYER
popup = Tk()
popup.title("Welcome!")
width = 800
height = 700
window_width = popup.winfo_screenwidth()
window_height = popup.winfo_screenheight()
x = (window_width / 2) - (width / 2)
y = (window_height / 2) - (height / 2)
popup.geometry("%dx%d+%d+%d" % (width, height, x, y))
popup.resizable(0, 0)

# BACKGROUND IMAGE
background_img = PhotoImage(file="resources/rockpaperscissorsBACK.png")
background_label = Label(popup, image=background_img)
background_label.image = background_img
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# WELCOME MESSAGE LABEL
Label(popup, text="Welcome to Rock-Paper-Scissors!", font=('Arial', 15, 'bold')).pack(pady=10)

# INSERT NAME
name_label = Label(popup, text="Enter your name:", font=('Arial', 12))
name_label.pack(pady=5)
name_entry = Entry(popup, font=('Arial', 12))
name_entry.pack(pady=5)

# CONTINUE
continue_button = ttk.Button(popup, text="Continue", command=continue_clicked)
continue_button.pack(pady=10)

style = ttk.Style()
style.configure('TButton', font=('Arial', 12, 'bold'), padding=10, width=12)

if __name__ == "__main__":
    popup.mainloop()
