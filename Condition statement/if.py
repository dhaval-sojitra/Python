a=int(input('Enter price :'))
d1=(a*10)/100;
d2=(a*12)/100;
d3=(a*15)/100;
d4=(a*20)/100;

if a>5000 and a<=8000:
    print('You got 10% discount on  your ',a,'Shopping that is ',d1,' Rs.')
    print('Total Pice after discount : ',(a-d1),"Rs.")
elif a>8000 and a<=10000:
    print('You got 12% discount on  your ',a,'Shopping that is ',d2,' Rs.')
    print('Total Pice after discount : ',(a-d2),"Rs.")
elif a>10000 and a<=20000:
    print('You got 15% discount on  your ',a,'Shopping that is ',d3,' Rs.')
    print('Total Pice after discount : ',(a-d3),"Rs.")
elif a>20000:
    print('You got 20% discount on  your ',a,'Shopping that is ',d4,' Rs.')
    print('Total Pice after discount : ',(a-d4),"Rs.")
else:
    print('You are not eligible for any discount')

