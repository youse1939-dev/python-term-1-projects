w=input("enter your weight :")
h=input("enter your height:")
h=float(h)
w=float(w)
bmi=w/(h*h)
bmi=round(bmi,2)



print(bmi)
if(bmi<20):
    print("you are underweighted")
    u_bmi=20-bmi
    u_w=bmi*h*h
    print("mizan kambood vazn shoma")
    print(u_w)





if(bmi>25):
    print("you are overweighted")
    o_bmi=bmi-25
    o_w=o_bmi*h*h
    print(" mizan ezafe vazn shoma:")
    print(o_w)



if (bmi>=20 and bmi<=25):
    print("you are normal ")



print('finish')                                      