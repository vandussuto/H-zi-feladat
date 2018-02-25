def feladat_7(h,sz,d):
    maradek=d-(2*h+2*sz)
    if maradek>0:
        print(maradek,"m drót maradt.")
    elif maradek==0:
        print("Pontosan ennyi drótra volt szükség")
    elif maradek<0:
        print (maradek*-1,"m drótra van még szükség.")



def feladat_11(ev):
    if ev//4==0:
        szokoev=ev/4
        nap=int(szokoev*366+(ev-szokoev)*365)
        print(nap)
    elif ev//4!=0:
        x=ev//4
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
