games = []
genres = set()
while True :
    c = input(" add / view / count / remove / edit / exit :  ")
    if c == "add" :
        games.append(input("Game name : "))
        genres.add(input("Game genre :"))
    elif c == "view" :
        for game in games :
            print("Game name :"+ game[0], "Game genre :" + game[1])
    elif c == "count" :
        print(len(games))
    elif c == "edit" or c == "remove" :
        while True :
            g = input(" wich one to remove ")
            for tuplegame in games:
                if c == "remove" and g == tuplegame[0] :
                    games.remove(tuplegame)
                    break
                elif c == "edit" and g == tuplegame[0] :
                    games.remove(tuplegame)
                    games.append((input("New Game name :"), input("New genre: ")))
                    break
            else:
                print(" This game doesnt exist try again ")
            if g == tuplegame[0]:
                break
            
    elif c == "exit" :
        break
    else :
        print(" cant " )
