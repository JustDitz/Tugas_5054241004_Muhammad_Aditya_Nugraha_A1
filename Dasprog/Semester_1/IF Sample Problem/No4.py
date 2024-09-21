Fl_CyColor = str(input("First letter of Clylider Color: ")).lower()
Fl_CyColor = Fl_CyColor[0]

match Fl_CyColor:
    case "o":
        print("ammonia")
    case "b":
        print("carbon monoxide")
    case "y":
        print("hydrogen")
    case "g":
        print("oxygen")
    case _ :
        print("Contents unknown")