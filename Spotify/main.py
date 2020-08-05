from playlistModifier import *
import tkinter
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Spotify Playlist Modifier")

# TODO: add spotify logo
spotifyLogoText = Label(root, text="Spotify Playlist Modifier", font="Sans_Serif 20 bold", \
    padx=10, pady=10)
spotifyLogoText.grid(row=0, column=0, columnspan=3)
spotifyLogo = ImageTk.PhotoImage(Image.open("C:/Users/dudoi/OneDrive/Desktop/python/Spotify/images/spotifyLogo.png").resize((200, 200)))
spotifyLogoLabel = Label(image=spotifyLogo)
spotifyLogoLabel.grid(row=1, column=0, columnspan=3)
 

userIDLabel = Label(root, text="Spotify User ID", padx=5, pady=5)
userIDLabel.grid(row=2, column=0)
userIDEntry = Entry(root, borderwidth=2)
userIDEntry.grid(row=2, column=1)

authLabel = Label(root, text="OAuth Access Token", padx=5, pady=5)
authLabel.grid(row=3, column=0)
authEntry = Entry(root, borderwidth=2)
authEntry.grid(row=3, column=1)

p1Label = Label(root, text="Main Playlist ID", padx=5, pady=5)
p1Label.grid(row=4, column=0)
p1Entry = Entry(root, borderwidth=2)
p1Entry.grid(row=4, column=1)

p2Label = Label(root, text="Second Playlist ID", padx=5, pady=5)
p2Label.grid(row=5, column=0)
p2Entry = Entry(root, borderwidth=2)
p2Entry.grid(row=5, column=1)

clicked = StringVar()
clicked.set("what would you like to do with the playlists")
dropDownMenu = OptionMenu(root, clicked, "Combine Playlists", "Subtract Playlists")
dropDownMenu.grid(row=6, column=0, columnspan=2)

def confirm():
    authToken = "accessToken:" +authEntry.get()
    userID = "userID:" +userIDEntry.get()
    p1ID = "playlist1ID:" +p1Entry.get()
    p2ID = "playlist2ID:" +p2Entry.get()
    exampleSong = "photosynthesisID:spotify:track:3DlgDXIYtnWtJKiB8bZQMv"
    command = "command:" +clicked.get()
    secrets = [
        authToken, 
        userID, 
        p1ID, 
        p2ID, 
        exampleSong,
        command
    ]
    with open("C:/Users/dudoi/OneDrive/Desktop/python/Spotify/secrets.txt", "w") as f:
        for secret in secrets:
            f.write(secret+"\n")
    
    a = PlaylistModifier()
    if(a.commmand == "Combine Playlists"):
        if(a.combinePlaylists().status_code == 201):
            messagebox.showinfo("success", "successfully combined the playlists")
        else:
            messagebox.showerror("error", 
            "there was an error. please make sure all the information is entered correctly. " 
            +"your playlists were not successfully combined")
    elif(a.commmand == "Subtract Playlists"):
        if(a.subtractPlaylists().status_code == 200):
            messagebox.showinfo("success", "successfully subtracted the playlists")
        else:
            messagebox.showerror("error", 
            "there was an error. please make sure all the information is entered correctly. "
            +"your playlists were not successfully subtracted")


confirmButton = Button(root, text="confirm", padx=20, command=confirm)
confirmButton.grid(row=7, column=0)

root.mainloop()