games = []
while True :
    c = input(" add / view / count / remove / edit / exit :  ")
    if c == "add" :
        games.append(input())
    elif c == "view" :
        for game in games :
            print(game)
    elif c == "count" :
        print(len(games))
    elif c == "edit" or c == "remove" :
        while True :
            g = input(" wich one to remove ")
            if g in games :
                if c == "remove" :
                    games.remove(g)
                    break
                if c == "edit" :
                    gn = input(" add ur new game ")
                    games.remove(g)
                    games.append(gn)
                    break
            else:
                print(" This game doesnt exist try again ")
    elif c == "exit" :
        break
    else :
        print(" cant " )