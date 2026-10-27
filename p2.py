avg1=0
while(avg1!=20            ):



    e1=float(input( "course1:"               )   )
    e2=float(input( "course2:"               )   )
    e3=float(input( "course3:"               )   )
    e4=float(input( "course4:"               )   )

    avg1=(e1+e2+e3+e4)/4

    if(avg1>15  ):
        print("you get exelent                 "  )

    if(avg1<18         ):
        print(" you get truely exelent" )

    if(avg1>=15)and(avg1<18):print("you got good")

    if(avg1>10     )and(avg1<15):print("you got bad")

    if(avg1<1)and(avg1>10):print(fail)
        