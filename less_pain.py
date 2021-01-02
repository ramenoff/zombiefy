
def checkExistingList(title):

    playlistNames = "PlaylistNames.txt"
    
    title = title.upper()
    repeat = False
    readFile = open(playlistNames, "r")
    plList = readFile.readlines()
    readFile.close()

    for eachTitle in plList:

        if(eachTitle == title):
            repeat = True

    if repeat == True:
        
        print("Playlist with name exists. Try new name.")
        #Redirect to user input

    else:
        
        with open(playlistNames, "a") as myfile:
            myfile.write(title)
            myfile.write("\n")

            

checkExistingList("Ramya")
