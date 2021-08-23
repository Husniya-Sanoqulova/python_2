a=int(input('Ixriyoriy son kiriting:   '))
if a==0:
    print('Siz nol sonini kiritdingiz')
else:
    if a>0 and a<10:
        print('Bu bir xonali musbat son')
    else:
        if a>10 and a<100:
            print('Bu ikki xonali musbat son')
        else:
            if a>=100:
                print('Siz katta musbat son kiritdingiz')
            else:
                print('Siz manfiy son kiritdingiz')
                
