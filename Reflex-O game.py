                 #REFLEX-O GAME CODE

import time
import turtle
import random
import sys              
import string

def draw_header(t_text):
   
    header = turtle.Turtle()       #header turtle yaratiyoruz.
    header.hideturtle()             
    header.penup()
    header.setpos(-10,250)             #header pozisyonu
    header.write("Puan almak icin dairelere tiklayin.",move=False,align='center',font=("Arial",18,("bold","normal")))
    time.sleep(1)                    #1sn bekle
    header.hideturtle()              
    t_text.penup()
    t_text.setpos(0,-150)         #text pozisyonu
    t_text.hideturtle()

def plus_one(score):         #score'a +100 eklenir
    score+=100
    return score

def plus_two(score):       #score'a +200 eklenir   
    score+=200
    return score

def plus_four(score):      #score'a +400 eklenir
    score+=400
    return score

def draw_score(score):     #score yazımı
    
    header = turtle.Turtle()
    header.shape('blank')
    header.penup()
    header.setpos(-10, -170)
    header.write(score,move=False,align='center',font=("Arial",15,("bold","normal")))
    header.clear()
    header.hideturtle()

def draw_one(t_one):      #1.dairenin ozellikleri
    
    x = random.randint(-250, 250)    #random konum
    y = random.randint(-200, 200)
    t_one.hideturtle()
    t_one.color("blue")             #rengi
    t_one.shapesize(3.5)            #cismin boyutu
    t_one.penup()
    t_one.setpos(x, y)
    t_one.shape("circle")           #cismin sekli (Daire)
    t_one.showturtle()

def draw_two(t_two):       #2.dairenin ozellikleri
    
    x = random.randint(-250, 250)          #random konum
    y = random.randint(-200, 200)
    t_two.hideturtle()
    t_two.color("red")             #rengi
    t_two.shapesize(1.5)            #cismin boyutu
    t_two.penup()
    t_two.setpos(x, y)
    t_two.shape("circle")       #cismin sekli (Daire)
    t_two.showturtle()

def draw_four(t_four):          #3.dairenin ozellikleri
    
    t_four.shape('blank')

    x = random.randint(-250,250)     #random konum
    y = random.randint(-200,200)
    t_four.hideturtle()
    t_four.color("purple")         #rengi
    t_four.shapesize(.27)         #cismin boyutu
    t_four.penup()
    t_four.setpos(x, y)
    t_four.shape("circle")   #cismin sekli (Daire)
    t_four.showturtle()

def color(numb):           #daire renkleri icin

    turtle.colormode(255)

def draw_quit(t_quit):                      #cikis butonu ayarlari
   
    t_quit.penup()
    t_quit.hideturtle()
    t_quit.setpos(205,-247)
    t_quit.write("stop'a bas ->",move=False,align='center',font=("Courier New",14,("bold","normal")))
    t_quit.showturtle()
    t_quit.setpos(310,-240)
    t_quit.shapesize(1,1,10)
    t_quit.shape("square")
    t_quit.color("#AFA4AF")

def handler_quit(x, y):    #cikis butonu basilirsa
    
    text.clear()
    text.write("Cikiliyor",move=False,align='center',font=("Arial",30,("bold","normal")))
    time.sleep(1)
    wn.bye()          #ekran kapatiliyor
    # sys.exit(0)

def main():

    print ("\n\n\n ReflexO'ya hos geldin!!!\n")                                 #Oyun kurallarını kullanıcıya iletmek icin
    instructions=input("Oyun acıklamasını okumak ister misin? (evet/hayir)")
    if instructions.lower()=='evet':
        print ("Ekranda cikan toplara basarak puan kazanabilirsin."
            "60 Saniyen var.\n" 
            "Mavi top 100 puan.\nKırmızı top 200 puan.\nMor top 400 puan.\n"
            "Bolsans! Oyun yakında baslayacak!.\n\n")
        time.sleep(18)
    elif instructions.lower()=='hayır':
        print ('Oyun kısa zaman icinde baslayacak. Iyi eglenceler!')
        time.sleep(8)

    else:
        print("Sanirim bu hayir demek, Oyun kısa zaman icinde baslayacak. Iyi eglenceler!")
        time.sleep(8)

    global score       #baslangıc degerleri
    score=0

    global start
    start=0


    def handler_one(x, y):           #1.daire tıklanırsa cagirilir.

        global score
        one.hideturtle()                  #daire ekrandan alınır.
        text.setpos(-105,-200)            #puan gosterim yeri                                            
        text.write("+100",move=False,align='center',font=("Arial",25,("bold","normal")))  #ekranda 100 puan yazimi
        
        score=plus_one(score)             #score'u artırmak       
        print ('Points:\t'+str(score))
        print ('\n'*3)
        #time.sleep(.2)
        draw_one(one)                 #1.daire baska yerde cizilir.
        text.clear()

    def handler_two(x, y):            #2.daire tıklanırsa cagirilir.
  
        global score
        two.hideturtle()                               #daire ekrandan alınır.
        text.setpos(-80,-200)                          #puan gosterim yeri
        text.write("+200",move=False,align='center',font=("Arial",25,("bold","normal"))) #ekranda 200 puan yazimi
       
        score=plus_two(score)            #score'u artırmak  
        print ('Points:\t'+str(score))
        print ('\n'*3)
        draw_two(two)              #2.daire baska yerde cizilir.
        text.clear()

    def handler_four(x, y):          #3.daire tıklanırsa cagirilir. 
 
        global score

        four.hideturtle()                 #daire ekrandan alınır.
        text.setpos(120,+210)              #puan gosterim yeri 
        text.write("+400",move=False,align='center',font=("Arial",25,("bold","normal")))   #ekranda 400 puan yazimi

        score=plus_four(score)               #score'u artırmak  
        print ('Points:\t'+str(score))
        print ('\n'*3)
        draw_four(four)                  #3.daire baska yerde cizilir.
        text.clear()

    def handler_quit(x, y):    #cıkıs butonu basılırsa cagirilir
        

        text.clear()
        text.setposition(-20,-260)                      #cikis mesajinin gosterim konumu
        text.write("Cikiliyor",move=False,align='center',font=("Arial",30,("bold","normal"))) #cikis mesaji
        time.sleep(1)                             #1sn bekle
        wn.bye()
        print ('Final Skorunuz:\t'+str(score)+' puan!\n bir dahakine daha iyi yapabilecegini biliyorum!')  #skoru goster
        time.sleep(2)             #2sn bekle
        sys.exit(0)                #sistemi birak


    turtle.colormode(255)                

    global wn
    wn = turtle.Screen()

    global text
    text = turtle.Turtle()
    draw_header(text)
    wn=turtle.Screen()

    one = turtle.Turtle()        #100 puan daire olusturuldu
    draw_one(one)


    two = turtle.Turtle()       #200 puan daire olusturuldu
    draw_two(two)


    four = turtle.Turtle()      #400 puan daire olusturuldu  
    draw_four(four) 

    quit_box = turtle.Turtle()     #quit butonu olusturuldu
    draw_quit(quit_box)

    wn.listen()     

    while True:
        
            clock=turtle.Turtle()      #oyundaki zamanlayici ayarlari
            clock.shape('blank')
            clock.penup()
            clock.setpos(-280,-250)
            clock.pendown()
            global seconds
            seconds=61

            for i in range(seconds):                       #zamanı azaltmak  
                seconds-=1
                clock.write('Time:  '+str(seconds),font=("Arial",15,("bold","normal")))
                time.sleep(1)
                clock.clear()

                
                one.onclick(handler_one)          #turtle tıklamak icin isleyici komutlar
                two.onclick(handler_two)
                four.onclick(handler_four)
                quit_box.onclick(handler_quit)

           
                if seconds ==0:        #zaman 0 olunca oyun sonu
                    wn.clearscreen()
                    text.setpos(0,0)
                    text.write("Oyun Bitti!",move=False,align='center',font=("Arial",40,("bold","normal")))
                    time.sleep(3)
                    wn.bye()
                    print ('Oyun sonu skorun:\t'+str(score)+' puan!\n Daha iyi bile yapabilirsin bence!\n')
                    time.sleep(2)
                    restart=raw_input("Tekrar denemek ister misin?(evet/hayir)")
                    global evet
                    global hayir
                    if restart.lower()=="evet":             #evet cevabi geldiyse
                        print ('\n Harika! (Shift+F10) bas ve baslayalim')
                        sys.exit(0)
                    if restart.lower()=='hayir':                  #hayir cevabi geldiyse
                        print ('\n Kahveni ic ve tekrardan gel bekliyoruz :)')
                        sys.exit(0)


main()