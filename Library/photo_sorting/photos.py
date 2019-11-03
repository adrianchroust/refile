def sort(path,name,show):

    import os
    import time
    from PIL import Image
    from settings.config import images, excluded, con1, con2, sep
    
    album = []
    n = 1

    folder = []
    rawfolder = os.listdir(path)
    for f in rawfolder:
        if os.path.isfile(os.path.join(path,f)) and os.path.splitext(f)[1] not in excluded: folder.append(f)
        
    for r in range(0, len(folder)):
        x = os.path.join(path,folder[r])
        y = folder[r]
        if os.path.splitext(y)[0] not in "placeholder":
            refile = os.path.join(path,"refile") + str(r) + os.path.splitext(x)[1]
            os.rename(x,refile)

    folder = []
    rawfolder = os.listdir(path)
    for f in rawfolder:
        if os.path.isfile(os.path.join(path,f)) and os.path.splitext(f)[1] not in excluded: folder.append(f)

    for i in range(0, len(folder)):
        x = os.path.join(path,folder[i])
        y = folder[i]

        try:
            if os.path.splitext(x)[1].lower() not in images:
               1 / 0 #Error on Purpose
            else:
                Image.open(x)._getexif()[36867]
        except:
            info = time.ctime(os.path.getmtime(x))
            year = info[20:24]
            months = {"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
            month = months.get(info[4:7])
            day = info[8:10].replace(" ","0")
            hour = info[11:13]
            minute = info[14:16]
            second = info[17:19]
        else:
            info = Image.open(x)._getexif()[36867]
            year = info[0:4]
            month = info[5:7]
            day = info[8:10]
            hour = info[11:13]
            minute = info[14:16]
            second = info[17:19]

        #date = year + "-" + month + "-" + day + "-" + hour + "-" + minute + "-" + second
        date = year + con1 + month + con1 + day + con2 + hour + con1  + minute + con1 + second
        ext = os.path.splitext(x)[-1].lower()
        file = date + sep + name + ext

        while True:
            if file in album:
                file = date + con2 + "0" + str(n) + sep + name + ext
                n = n + 1
                continue
            else:
                n = 1
                break

        if os.path.splitext(y)[0] in "placeholder":
            os.remove(x)
            if show is True:
                print("Entferne",folder[i], end=".")
        else:
            if file in rawfolder:
                print("\n",x,"konnte leider nicht umbenannt werden.\n")
            else:
                new = os.path.join(path,file)
                os.rename(x,new)
                album.append(file)
                if show is True:
                    print("Benenne Datei in",file,"um.")

def photos():
    
    import time
    import os
    from settings.config import yes, no, stop, excluded
    
    workplace = "Workplace"
    current = os.getcwd()
    print("Willkommen bei Refile, einem kleinen Programm zur Sortierung von Photos.")
    #time.sleep(2)
    input("\nDrücke ENTER um fortzufahren.\n")

    while True:
        while True:
            os.chdir(current)
            name = ""

            print("Dateipfad des Albums (wenn dieser leer bleibt, wird automatisch der ",workplace,"-Ordner ausgewählt): ",sep="",end="")
            path = input()
            while True:
                try:
                    if path not in "": os.listdir(path)
                except:
                    path = input("Dieser Ordner existiert nicht. Versuche es noch einmal: ")
                    continue
                else:
                    break
            os.chdir("..")
            while True:
                subfolders = [f.path for f in os.scandir(os.path.join(os.getcwd(),workplace)) if f.is_dir()]
                if path in "" and len(subfolders)==1:
                    path = subfolders[0]
                    print(path)
                    break
                elif path in "" and len(subfolders)==0:
                        print("Der ",workplace,"-Ordner enthält keine Dateien. Wähle einen anderen Ordner oder platziere ein Album im ",workplace,"-Ordner: ",sep="",end="")
                        path = input()
                        continue
                elif path in "" and len(subfolders)>1:
                    print("\r")
                    for m in range(0, len(subfolders)):
                        print(m+1,". ",subfolders[m], sep="")
                    print("\r")
                    while True:
                        zahl = input("Gib die Nummer deines Ordners ein: ")
                        try:
                            zahl = int(zahl)
                            subfolders[zahl-1]
                        except:
                            continue
                        else:
                            int(zahl)
                            path = subfolders[zahl-1]
                            break
                    break
                else:
                    try:
                        if path not in "": os.listdir(path)
                    except:
                        path = input("Dieser Ordner existiert nicht. Versuche es noch einmal: ")
                        continue
                    else:
                        break

            folder = []
            rawfolder = os.listdir(path)
            for f in rawfolder:
                if os.path.isfile(os.path.join(path,f)) and os.path.splitext(f)[1] not in excluded:
                    folder.append(f)
            
            if folder:
                print("\r")
                while True:
                    name = input('Name des Albums ohne Datum (optional): ')
                    try:
                        if name not in "":
                            testname = name + ".txt"
                            testfile = open(testname, "x")
                            testfile.close()
                    except:
                        continue
                    else:
                        testname = name + ".txt"
                        testdir = os.listdir(os.getcwd())
                        if testname in testdir: os.remove(testname)
                        break

            if name not in "": name = name.replace(" ","_")

            if not folder:
                #print("\nOrdner:",path)
                print("\nDer Ordner ist leer. Wähle einen anderen Ordner für dein Album.")
                continue
            else:
                print("\n",folder,"\n")
                print("Ordner:",path,"\n")
                janein = input('Alle hier gelisteten Dateien werden nach Datum, Uhrzeit und dem Namen des Albums umbenannt. \nGib "Ja" ein, um fortzufahren, "Nein", um deine Auswahl zu ändern, oder "Stopp", um das Programm zu stoppen: ')
                janein = janein.lower()
            
            while True:
                if janein in yes or janein in no or janein in stop:
                    break
                else:
                    janein = input('Gib "Ja" ein, um fortzufahren, "Nein", um deine Auswahl zu ändern, oder "Stopp", um das Programm zu stoppen: ')
                    continue

            if janein in no:
                print("\r")
                continue
            elif janein in yes:
                print("\nBereite Umbenennung der Dateien vor...\n")
                break
            elif janein in stop:
                print("\nIch hoffe ich konnte dir behilflich sein!")
                time.sleep(2)
                quit()

        show = True
        sort(path,name,show)
                
        janein = input('\nAlle deine Photos wurden erfolgreich umbenannt!\nGib "Ja" ein, um weitere Photos umzubenennen, oder "Nein", um das Programm zu stoppen: ')
        janein = janein.lower()
                  
        while True:
            if janein in yes or janein in no:
                break
            else:
                janein = input('Gib "Ja" ein, um weitere Photos umzubenennen, oder "Nein" bzw. "Stopp", um das Programm zu stoppen: ')
                continue

        if janein in no or janein in stop:
            print("\nIch hoffe ich konnte dir behilflich sein!")
            time.sleep(2)
            quit()
        elif janein in yes:
            print("\r")
            continue
