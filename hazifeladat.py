def feladat_7(h,sz,d):
    maradek=d-(2*h+2*sz)
    if maradek>0:
        print(maradek,"m drót maradt.")
    elif maradek==0:
        print("Pontosan ennyi drótra volt szükség")
    elif maradek<0:
        print (maradek*-1,"m drótra van még szükség.")



def feladat_11(ev):
    if ev%4==0:
        szokoev=ev/4
        nap=int(szokoev*366+(ev-szokoev)*365)
        print(nap)
    elif ev%4!=0:
        x=ev%4
        y=ev-x
        szokoev=y/4
        nap=int(szokoev*366+(ev-szokoev+x)*365)
        print(nap)



def feladat_14(h):
    if h==1:
        print("Január")
    elif h==2:
        print("Február")
    elif h==3:
        print("Március")
    elif h==4:
        print("Április")
    elif h==5:
        print("Május")
    elif h==6:
        print("Június")
    elif h==7:
        print("Július")
    elif h==8:
        print("Augusztus")
    elif h==9:
        print("Szeptember")
    elif h==10:
        print("Október")
    elif h==11:
        print("November")
    elif h==12:
        print("December")



def feldat_5(a,b,c,d):
    a=int()
    b=int()
    c=int()
    d=int()
    print(a,b,c,d)
    if d>=0:
        print(a,c,b,d)
    else:
        print(a,b,d,c)


def feladat_6(a,b,c):
    if a+b>c or a+c>b or b+c>a:
        br=



def feladat_3(x):
    if x>-2 and x<0:
        return 2*x
        print(2*x)
    if x>=0 and x<2:
        return x*x
        print(x*x)
    if x>2:
        return 10
        print(10)
    else:
        print("Erre az értékre nem definiált a függvény.")



def feladat_12(pontszam,maximum):
    if pontszam>=maximum*0.6:
        print("Sikeres!")
    else:
        print("Sikertelen!")



def feladat_13(erdemjegy):
    if erdemjegy==5:
        print("Kiváló")
    if erdemjegy==4:
        print("Jó")
    if erdemjegy==3:
        print("Közepes")
    if erdemjegy==2:
        print("Elégséges")
    if erdemjegy==1:
        print("Elégtelen")
    else:
        print("Az érdemjegynek 1 és 5 között kell lennie!")



def feladat_28(n):
    m=0
    m>=n
    if n>1:
        z=m//



def feladat_26(x):
    x=0
    minusz=0
    plusz=0
    z=int(input("Adja meg az első számot: "))
    if z > 0:
        plusz += 1
    elif z < 0:
        minusz += 1
    x=x+z
    print(x)
    while x!=0:
        z=int(input("Adja meg a következő számot: "))
        if z>0:
            plusz+=1
        elif z<0:
            minusz+=1
        x=x+z
        print(x)
    print("Minusz: ",minusz,", Plusz: ",plusz)