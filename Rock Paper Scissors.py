import tkinter as tk
import pygame
import random
rps = tk.Tk()
def sf(frame):
    frame.tkraise()
computer_throws = {
    "1": "Rock",
    "2": "Paper",
    "3": "Scissors"
}
# Player throws rock

def p_rock():
    ct = computer_throws[str(random.randint(1, 3))]
    if ct == "Rock":
        matchres = "Draw"
    elif ct == "Paper":
        matchres = "Computer"
    else:
        matchres = "Player"
    board = tk.Label(game_screen, text=matchres, font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=510, y=545, width=300, height=45)
    ptb = tk.Label(game_screen, text="Rock", font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=820, y=280, width = 170, height=45)
    ctb = tk.Label(game_screen, text= ct, font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=220, y=280, width = 170, height=45)

# Player throws paper
def p_paper():
    ct = computer_throws[str(random.randint(1,3))]
    if ct == "Rock":
        matchres = "Player"
    elif ct == "Paper":
        matchres = "Draw"
    else:
        matchres = "Computer"
    board = tk.Label(game_screen, text=matchres, font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=510, y=545, width=300, height=45)
    ptb = tk.Label(game_screen, text="Paper", font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=820, y=280, width = 170, height=45)
    ctb = tk.Label(game_screen, text= ct, font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=220, y=280, width = 170, height=45)

# Player throws scissors
def p_scissors():
    ct = computer_throws[str(random.randint(1,3))]
    if ct == "Rock":
        matchres = "Computer"
    elif ct == "Paper":
        matchres = "Player"
    else:
        matchres = "Draw"
    board = tk.Label(game_screen, text=matchres, font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=510, y=545, width=300, height=45)
    ptb = tk.Label(game_screen, text="Scissors", font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=820, y=280, width = 170, height=45)
    ctb = tk.Label(game_screen, text= ct, font="Helvetica 20", bg="#c01609", fg="white",borderwidth=2.5, relief="solid").place(x=220, y=280, width = 170, height=45)

pygame.mixer.init()
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.play(loops=-1)
rps.geometry("1000x600")
rps.minsize(1000, 600)
rps.maxsize(1000, 600)
rps.title("Rock Paper Scissors")
# Frames
game_screen = tk.Frame(rps)
load_screen = tk.Frame(rps)
for frame in (game_screen, load_screen):
    frame.grid(row=0, column=0, sticky="nsew")

rps.rowconfigure(0, weight=1)
rps.columnconfigure(0, weight=1)
rps.state('zoomed')

# Load Screen code:
bg = tk.PhotoImage(file="bg3.png")
rpl = tk.Label(load_screen, image=bg).place(relx=0, rely=0)
play_button = tk.Button(load_screen, text="Play Game", font="Helvetica 20", padx=45, pady=6, command=lambda: sf(game_screen)).place(relx=0.5, rely=0.62, anchor="center")
exit_button = tk.Button(load_screen, text="Exit", font="Helvetica 20", padx=89, pady=6, command=exit).place(relx=0.5, rely=0.735, anchor="center")

# Game Screen Code:
image = tk.PhotoImage(file="vs.png")
rpg = tk.Label(game_screen, image=image).place(relx=0, rely=0)
gs_back = tk.Button(game_screen, text="Back", font="Helvetica 10", command=lambda: sf(load_screen)).place(relx=0.0, rely=0.955)
pl = tk.Label(game_screen, text="You", font="Helvetica 20", bg="#c01609", fg="white", padx=120, pady=2.5, borderwidth=2.5, relief="solid").place(x=620, y=128)
cl = tk.Label(game_screen, text="Computer", font="Helvetica 20", bg="#00141b", fg="white", padx=95, pady=2.5, borderwidth=2.5, relief="solid").place(x=90, y=128)
rockb = tk.Button(game_screen, text="Rock", font="Commando 15 bold", bg="#d52c0d", fg="white", command=p_rock).place(x=710, y=350)
paperb = tk.Button(game_screen, text="Paper", font="Commando 15 bold", bg="#d52c0d", fg="white", command=p_paper).place(x=710, y=400)
scissorsb = tk.Button(game_screen, text="Scissors", font="Commando 15 bold", bg="#d52c0d", fg="white", command=p_scissors).place(x=710, y=455)

rps.mainloop()