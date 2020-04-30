while True:
    try:
        in1=int(input("please enter a number:"))
    except:
        print("that is not a number")
        continue
    else:
        print("Num sq= "+str(in1**2))
        break
    finally:
        print("program over")