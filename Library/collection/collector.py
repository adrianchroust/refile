def collect():

    import os
    import time
    import shutil
    from photo_sorting import sort
    from settings.config import yes, no, stop

    show = False

    diverse = "Diverse"
    roast = "Roast"
    inbox = "Inbox"
    various = [diverse,roast]

    zwettl = "Zwettl"
    album = [zwettl]

    print("Dieses Programm ist nur für den Ersteller (Adrian) gedacht, Benutzung auf eigene Gefahr!\n")

    while True:
        src = input("Quelle (Data-Kopie vom Handy): ")
        while True:
            try:
                os.listdir(src)
            except:
                src = input("Dieser Ordner existiert nicht. Versuche es noch einmal: ")
                continue
            else:
                break

        dst = input("Ziel (Adrian's Library): ")
        while True:
            try:
                os.listdir(dst)
            except:
                dst = input("Dieser Ordner existiert nicht. Versuche es noch einmal: ")
                continue
            else:
                if dst == src:
                    dst = input("Quelle und Ziel können nicht derselbe Ordner sein. Versuche es noch einmal: ")
                    continue
                else:
                    break

        print("\n",src,"\n",dst,"\n")
        
        janein = input('Gib "Ja" ein, um fortzufahren, "Nein", um deine Auswahl zu ändern, oder "Stopp", um das Programm zu stoppen: ')
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
            print("\nBenenne Dateien um...\n")
            break
        elif janein in stop:
            print("\nIch hoffe ich konnte dir behilflich sein!")
            time.sleep(2)
            quit()

    srcfolders = os.listdir(src)
    mistake = False
	
    for s in srcfolders:
        path = os.path.join(src,s)
        folder = s.lower()

        choice = False
        for v in various:
            if v.lower() in folder:
                choice = True
        if choice:
            
            if diverse.lower() in folder:
                #err = False
                #if len(os.listdir(path))>1:
                sort(path,diverse,show)
                place = os.path.join(dst,"Ongoing","Various")
                dstfolder = False
                for p in os.listdir(place):
                    if diverse.lower() in p.lower():
                        dstfolder = p
                if dstfolder:
                    for f in os.listdir(path):
                        if f not in os.listdir(os.path.join(place,dstfolder)):
                            shutil.move(os.path.join(path,f),os.path.join(place,dstfolder,f))
                        else:
                            print("Eine Datei im Ordner",s,"konnte nicht verschoben werden.")
                            mistake = True
                            #err = True
                             
            elif roast.lower() in folder:
                #err = False
                #if len(os.listdir(path))>1:
                name = roast + "s"
                sort(path,name,show)
                place = os.path.join(dst,"Ongoing","Various")
                dstfolder = False
                for p in os.listdir(place):
                    if roast.lower() in p.lower():
                        dstfolder = p
                if dstfolder:
                    for f in os.listdir(path):
                        if f not in os.listdir(os.path.join(place,dstfolder)):        
                            shutil.move(os.path.join(path,f),os.path.join(place,dstfolder,f))
                        else:
                            print("Eine Datei im Ordner",s,"konnte nicht verschoben werden.")
                            mistake = True
                            #err = True
                    
        elif inbox.lower() in folder:
            if len(os.listdir(path))>1:
                print(path)
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
                        if name not in "": name = name.replace(" ","_")
                        print("\r")
                        break
            else:
                name = ""
            sort(path,name,show)
            if len(os.listdir(path))>0:
                from random import randint
                subinbox = inbox + str(randint(0,1000000)) + name
                place = os.path.join(dst,"Inbox",subinbox)
                shutil.move(path,place)
                

        if "Albums" in s:
            for k in os.listdir(path):
                for custom in album:
                    if custom.lower() in k.lower():
                        #albumfolder = [x.lower() for x in album]
                        #albumpath = os.path.join(src,s)
                        err = False
                        custompath = os.path.join(src,s,k)
                        sort(custompath,custom,show)
                        dstfolder = ""

                        if custom == zwettl:
                            place = os.path.join(dst,"Ongoing","Albums")
                            for q in os.listdir(place):
                                if custom.lower() in q.lower():
                                    dstfolder = q
                            if dstfolder:
                                for f in os.listdir(custompath):
                                    if f not in os.listdir(os.path.join(place,dstfolder)):
                                        shutil.move(os.path.join(custompath,f),os.path.join(place,dstfolder,f))
                                    else:
                                        print("Die Datei",f,"im Ordner",s,"konnte nicht verschoben werden.")
                                        mistake = True
                                        err = True
                            else:
                                mistake = True
                                err = True
                                print("Für",custom,"existiert kein Ziel-Ordner.")
                            if not err:
                                    os.rmdir(custompath)

        #if os.listdir(os.path.join(src,"Albums")) == []:
            #os.rmdir(os.path.join(src,"Albums"))
            
        for b in os.listdir(src):
            if os.listdir(os.path.join(src,b)) == []:
                os.rmdir(os.path.join(src,b))
                    
    if mistake:
        input("\nEs sind Fehler aufgetreten.\nDrücke ENTER um das Programm zu beenden.\n")
        quit()
    else:
        print("Der Vorgang wurde erfolgreich abgeschlossen.")
        time.sleep(10)
        quit()
