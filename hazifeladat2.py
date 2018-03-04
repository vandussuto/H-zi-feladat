def feladat_10():
    try:
        fajl=open("be.txt",mode="r")
        max=0
        for sr in fajl:
            temp=0
            sr=sr.strip()
            sr=sr.split(" ")
            h=len(sr)
            temp+=h
            if max<temp:
                max=temp
        print(max)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_11():
    try:
        fajl=open("be.txt",mode="r")
        li=[".","!","?"]
        max=0
        for sr in fajl:
            sr=sr.strip()
            sr=sr.split(" ")
            temp=0
            h=len(sr)
            u=sr[-1]
            i=u[-1]
            if i in li:
                temp+=h
                if max<temp:
                    max=temp
        print(int(max))
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_12():
    try:
        fajl1=open("be.txt",mode="r")
        fajl2=open("ki.txt",mode="w")
    finally:
        fajl1.close()
        fajl2.close()

def feladat_13():
    try:
        fajl=open("be.txt",mode="r")
    finally:
        fajl.close()

def feladat_25():
    try:
        fajl=open("szotar.txt",mode="r")
        angol=-1
        magyar=-1
        a=[]
        m=[]
        for sr in fajl:
            sr=sr.strip()
            angol+=1
            magyar+=1
            sr=sr.split(":")
            sr=[sr]
            a.append(sr[-2])
            m.append(sr[-2])
        print(angol)
    finally:
        fajl.close()

feladat_25()

