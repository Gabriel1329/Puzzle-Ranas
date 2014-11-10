from niveles import niveles
import pygame
import time

#se crea la pantalla y se cargan las imagenes
pantalla=pygame.display.set_mode([750,425])
tablero=pygame.image.load("tablero.png")
boton=pygame.image.load("boton.png")
rana=pygame.image.load("rana.png")

# se crean los rectangulos que van detras del tablero
A=pygame.Rect(38,40,75,75)
B=pygame.Rect(175,40,75,75)
C=pygame.Rect(312,40,75,75)
D=pygame.Rect(106,107,75,75)
E=pygame.Rect(242,107,75,75)
F=pygame.Rect(38,177,75,75)
G=pygame.Rect(175,177,75,75)
H=pygame.Rect(312,177,75,75)
I=pygame.Rect(106,244,75,75)
J=pygame.Rect(242,244,75,75)
K=pygame.Rect(38,314,75,75)
L=pygame.Rect(175,314,75,75)
M=pygame.Rect(312,314,75,75)
X=pygame.Rect(0,0,425,425)
r1=pygame.Rect(0,0,0,1)
pantalla.fill((0,215,240))
pantalla.blit(tablero,(0,0))

#creacion de sprite
kolbi=pygame.sprite.Sprite()
kolbi.image=rana
kolbi.rect=rana.get_rect()
kolbi.rect.top=0
kolbi.rect.left=0

#######################################################################################################################
# borrar es la funcion que elimina las ranas si cumplen las condiciones puestas en el juego original para poder eliminar una rana
def borrar(nivel,x,PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM,corX,corY):
    salir=False
    reloj1=pygame.time.Clock()
    while salir!=True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True

            if x=="A": # la variable x es la posicion en que estaba la rana que se quitó, dependiendo de esta variable y de las condiciones del tablero, se podra mover o no
                if r1.colliderect(C) and PC==0 and PB==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("B")
                        nivel=nivel+["C"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(G) and PG==0 and PD==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("D")
                        nivel=nivel+["G"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(K) and PK==0 and PF==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("F")
                        nivel=nivel+["K"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(X):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel=nivel+["A"]
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

            elif x=="B":
                if r1.colliderect(F) and PF==0 and PD==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("D")
                        nivel=nivel+["F"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(L) and PL==0 and PG==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("G")
                        nivel=nivel+["L"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(H) and PH==0 and PE==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("E")
                        nivel=nivel+["H"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(X):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel=nivel+["B"]
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

            elif x=="C":
                if r1.colliderect(A) and PA==0 and PB==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("B")
                        nivel=nivel+["A"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(G) and PG==0 and PE==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("E")
                        nivel=nivel+["G"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(M) and PM==0 and PH==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("H")
                        nivel=nivel+["M"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(X):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel=nivel+["C"]
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

            elif x=="D":
                if r1.colliderect(J) and PJ==0 and PG==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("G")
                        nivel=nivel+["J"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(X):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel=nivel+["D"]
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

            elif x=="E":
                if r1.colliderect(I) and PI==0 and PG==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("G")
                        nivel=nivel+["I"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(X):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel=nivel+["E"]
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

            elif x=="F":
                if r1.colliderect(B) and PB==0 and PD==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("D")
                        nivel=nivel+["B"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(H) and PH==0 and PG==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("G")
                        nivel=nivel+["H"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(L) and PL==0 and PI==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("I")
                        nivel=nivel+["L"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(X):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel=nivel+["F"]
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

            elif x=="G":
                if r1.colliderect(A) and PA==0 and PD==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("D")
                        nivel=nivel+["A"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(C) and PC==0 and PE==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("E")
                        nivel=nivel+["C"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(K) and PK==0 and PI==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("I")
                        nivel=nivel+["K"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(M) and PM==0 and PJ==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("J")
                        nivel=nivel+["M"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(X):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel=nivel+["G"]
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

            elif x=="H":
                if r1.colliderect(B) and PB==0 and PE==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("E")
                        nivel=nivel+["B"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(F) and PF==0 and PG==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("G")
                        nivel=nivel+["F"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(L) and PL==0 and PJ==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("J")
                        nivel=nivel+["L"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(X):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel=nivel+["H"]
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

            elif x=="I":
                if r1.colliderect(E) and PE==0 and PG==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("G")
                        nivel=nivel+["E"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(X):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel=nivel+["I"]
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

            elif x=="J":
                if r1.colliderect(D) and PD==0 and PG==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("G")
                        nivel=nivel+["D"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(X):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel=nivel+["J"]
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

            elif x=="K":
                if r1.colliderect(A) and PA==0 and PF==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("F")
                        nivel=nivel+["A"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(G) and PG==0 and PI==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("I")
                        nivel=nivel+["G"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(M) and PM==0 and PL==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("L")
                        nivel=nivel+["M"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(X):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel=nivel+["K"]
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

            elif x=="L":
                if r1.colliderect(F) and PF==0 and PI==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("I")
                        nivel=nivel+["F"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(B) and PB==0 and PG==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("G")
                        nivel=nivel+["B"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(H) and PH==0 and PJ==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("J")
                        nivel=nivel+["H"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(X):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel=nivel+["L"]
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

            elif x=="M":
                if r1.colliderect(K) and PK==0 and PL==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("L")
                        nivel=nivel+["K"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(G) and PG==0 and PJ==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("J")
                        nivel=nivel+["G"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(C) and PC==0 and PH==1:
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel.remove("H")
                        nivel=nivel+["C"]
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

                elif r1.colliderect(X):
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        nivel=nivel+["M"]
                        Kolbi(nivel,nivel[:],PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

        (r1.left,r1.top)=pygame.mouse.get_pos()
        (kolbi.rect.left,kolbi.rect.top)=pygame.mouse.get_pos()


        reloj1.tick(20)

        pygame.display.update()

    pygame.quit()    

#######################################################################################################################
# esta funcion solo pone las de nuevo todas las ranas que no se seleccionaron, sin las que si se seleccionó
def Kolbi2(nivel,nivel2,PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM,x):
    if nivel==[]: #cuando la lista de las posiciones este vacia, llama a la funcion borrar
        return borrar(nivel2,x,PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM,kolbi.rect.left,kolbi.rect.top)
    elif nivel[0]=="A":
        kolbi.rect.top=(A.top)+5
        kolbi.rect.left=(A.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi2(nivel[1:],nivel2,PA+1,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM,x)

    elif nivel[0]=="B":
        kolbi.rect.top=(B.top)+5
        kolbi.rect.left=(B.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi2(nivel[1:],nivel2,PA,PB+1,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM,x)

    elif nivel[0]=="C":
        kolbi.rect.top=(C.top)+5
        kolbi.rect.left=(C.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi2(nivel[1:],nivel2,PA,PB,PC+1,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM,x)

    elif nivel[0]=="D":
        kolbi.rect.top=(D.top)+5
        kolbi.rect.left=(D.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi2(nivel[1:],nivel2,PA,PB,PC,PD+1,PE,PF,PG,PH,PI,PJ,PK,PL,PM,x)

    elif nivel[0]=="E":
        kolbi.rect.top=(E.top)+5
        kolbi.rect.left=(E.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi2(nivel[1:],nivel2,PA,PB,PC,PD,PE+1,PF,PG,PH,PI,PJ,PK,PL,PM,x)

    elif nivel[0]=="F":
        kolbi.rect.top=(F.top)+5
        kolbi.rect.left=(F.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi2(nivel[1:],nivel2,PA,PB,PC,PD,PE,PF+1,PG,PH,PI,PJ,PK,PL,PM,x)

    elif nivel[0]=="G":
        kolbi.rect.top=(G.top)+5
        kolbi.rect.left=(G.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi2(nivel[1:],nivel2,PA,PB,PC,PD,PE,PF,PG+1,PH,PI,PJ,PK,PL,PM,x)

    elif nivel[0]=="H":
        kolbi.rect.top=(H.top)+5
        kolbi.rect.left=(H.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi2(nivel[1:],nivel2,PA,PB,PC,PD,PE,PF,PG,PH+1,PI,PJ,PK,PL,PM,x)

    elif nivel[0]=="I":
        kolbi.rect.top=(I.top)+5
        kolbi.rect.left=(I.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi2(nivel[1:],nivel2,PA,PB,PC,PD,PE,PF,PG,PH,PI+1,PJ,PK,PL,PM,x)

    elif nivel[0]=="J":
        kolbi.rect.top=(J.top)+5
        kolbi.rect.left=(J.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi2(nivel[1:],nivel2,PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ+1,PK,PL,PM,x)

    elif nivel[0]=="K":
        kolbi.rect.top=(K.top)+5
        kolbi.rect.left=(K.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi2(nivel[1:],nivel2,PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK+1,PL,PM,x)

    elif nivel[0]=="L":
        kolbi.rect.top=(L.top)+5
        kolbi.rect.left=(L.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi2(nivel[1:],nivel2,PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL+1,PM,x)

    elif nivel[0]=="M":
        kolbi.rect.top=(M.top)+5
        kolbi.rect.left=(M.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi2(nivel[1:],nivel2,PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM+1,x)

#######################################################################################################################
def mover(nivel,PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM):
    
    if len(nivel)==1: # esta es la restriccion para que cuando quede una rana, indique que ya ganó
        FuenteGanastes=pygame.font.Font(None, 100)
        TextoGanastes=FuenteGanastes.render("Ganaste",0,(255,255,255))     
        pantalla.blit(TextoGanastes,(45,150))
        
    salir=False
    reloj1=pygame.time.Clock()
    
    # crea los rectangulos para los botones
    basico=pygame.Rect(470,45,205,70)
    intermedio=pygame.Rect(470,150,205,70)
    avanzado=pygame.Rect(470,255,205,70)
    experto=pygame.Rect(470,360,205,70)
    
    # crea el rectangulo que toma la coordenadas del mouse para las colisiones
    r1=pygame.Rect(0,0,0,1)
    
    while salir!=True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT: 
                salir=True

            # si se preciona algun boton de nivel, el nivel cambia 
            elif r1.colliderect(basico):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pantalla.blit(tablero,(0,0))
                    nivel=niveles("basico")
                    Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            elif r1.colliderect(intermedio):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pantalla.blit(tablero,(0,0))
                    nivel=niveles("intermedio")
                    Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            elif r1.colliderect(avanzado):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pantalla.blit(tablero,(0,0))
                    nivel=niveles("avanzado")
                    Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            elif r1.colliderect(experto):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pantalla.blit(tablero,(0,0))
                    nivel=niveles("experto")
                    Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            # aqui se reconoce si se selecciona alguna rana e imprime el tablero como esta pero sin las rana que se selecionó
            elif r1.colliderect(A):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if "A" in nivel:
                        nivel.remove("A")
                        pantalla.blit(tablero,(0,0))
                        Kolbi2(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0,"A") 
                    else:
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            elif r1.colliderect(B):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if "B" in nivel:
                        nivel.remove("B")
                        pantalla.blit(tablero,(0,0))
                        Kolbi2(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0,"B") 
                    else:
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            elif r1.colliderect(C):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if "C" in nivel:
                        nivel.remove("C")
                        pantalla.blit(tablero,(0,0))
                        Kolbi2(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0,"C") 
                    else:
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            elif r1.colliderect(D):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if "D" in nivel:
                        nivel.remove("D")
                        pantalla.blit(tablero,(0,0))
                        Kolbi2(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0,"D") 
                    else:
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            elif r1.colliderect(E):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if "E" in nivel:
                        nivel.remove("E")
                        pantalla.blit(tablero,(0,0))
                        Kolbi2(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0,"E") 
                    else:
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            elif r1.colliderect(F):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if "F" in nivel:
                        nivel.remove("F")
                        pantalla.blit(tablero,(0,0))
                        Kolbi2(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0,"F") 
                    else:
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            elif r1.colliderect(G):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if "G" in nivel:
                        nivel.remove("G")
                        pantalla.blit(tablero,(0,0))
                        Kolbi2(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0,"G") 
                    else:
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            elif r1.colliderect(H):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if "H" in nivel:
                        nivel.remove("H")
                        pantalla.blit(tablero,(0,0))
                        Kolbi2(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0,"H") 
                    else:
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            elif r1.colliderect(I):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if "I" in nivel:
                        nivel.remove("I")
                        pantalla.blit(tablero,(0,0))
                        Kolbi2(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0,"I") 
                    else:
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            elif r1.colliderect(J):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if "J" in nivel:
                        nivel.remove("J")
                        pantalla.blit(tablero,(0,0))
                        Kolbi2(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0,"J") 
                    else:
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            elif r1.colliderect(K):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if "K" in nivel:
                        nivel.remove("K")
                        pantalla.blit(tablero,(0,0))
                        Kolbi2(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0,"K") 
                    else:
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            elif r1.colliderect(L):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if "L" in nivel:
                        nivel.remove("L")
                        pantalla.blit(tablero,(0,0))
                        Kolbi2(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0,"L") 
                    else:
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            elif r1.colliderect(M):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if "M" in nivel:
                        nivel.remove("M")
                        pantalla.blit(tablero,(0,0))
                        Kolbi2(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0,"M") 
                    else:
                        pantalla.blit(tablero,(0,0))
                        Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            else:
                mover(nivel,PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

        (r1.left,r1.top)=pygame.mouse.get_pos() #el rectrangulo r1 toma las coordenadas del mouse
        pygame.display.update()
        reloj1.tick(20)

    pygame.quit()                
                
        
#######################################################################################################################
#esta funcion posiciona las ranitas segun el nivel que se haya escojido, pone cada una en su lugar
# recibe el una lista con las posiciones de las ranas, una lista clonada de la primera y 
def Kolbi(nivel,nivel2,PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM): #las variables PA, PB, PC.. ect, se utilizan hasta la ultima funcion para las restricciones del juego
    if nivel==[]:
        mover(nivel2,PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

    #dependiendo de la letra que tenga la lista de nivel, ahi se pondra la ranita    
    elif nivel[0]=="A":
        kolbi.rect.top=(A.top)+5 #le sumo 5 y 10 solo para que quede mas centrado en la posicion 
        kolbi.rect.left=(A.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi(nivel[1:],nivel2,PA+1,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

    elif nivel[0]=="B":
        kolbi.rect.top=(B.top)+5
        kolbi.rect.left=(B.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi(nivel[1:],nivel2,PA,PB+1,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

    elif nivel[0]=="C":
        kolbi.rect.top=(C.top)+5
        kolbi.rect.left=(C.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi(nivel[1:],nivel2,PA,PB,PC+1,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

    elif nivel[0]=="D":
        kolbi.rect.top=(D.top)+5
        kolbi.rect.left=(D.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi(nivel[1:],nivel2,PA,PB,PC,PD+1,PE,PF,PG,PH,PI,PJ,PK,PL,PM)

    elif nivel[0]=="E":
        kolbi.rect.top=(E.top)+5
        kolbi.rect.left=(E.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi(nivel[1:],nivel2,PA,PB,PC,PD,PE+1,PF,PG,PH,PI,PJ,PK,PL,PM)

    elif nivel[0]=="F":
        kolbi.rect.top=(F.top)+5
        kolbi.rect.left=(F.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi(nivel[1:],nivel2,PA,PB,PC,PD,PE,PF+1,PG,PH,PI,PJ,PK,PL,PM)

    elif nivel[0]=="G":
        kolbi.rect.top=(G.top)+5
        kolbi.rect.left=(G.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi(nivel[1:],nivel2,PA,PB,PC,PD,PE,PF,PG+1,PH,PI,PJ,PK,PL,PM)

    elif nivel[0]=="H":
        kolbi.rect.top=(H.top)+5
        kolbi.rect.left=(H.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi(nivel[1:],nivel2,PA,PB,PC,PD,PE,PF,PG,PH+1,PI,PJ,PK,PL,PM)

    elif nivel[0]=="I":
        kolbi.rect.top=(I.top)+5
        kolbi.rect.left=(I.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi(nivel[1:],nivel2,PA,PB,PC,PD,PE,PF,PG,PH,PI+1,PJ,PK,PL,PM)

    elif nivel[0]=="J":
        kolbi.rect.top=(J.top)+5
        kolbi.rect.left=(J.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi(nivel[1:],nivel2,PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ+1,PK,PL,PM)

    elif nivel[0]=="K":
        kolbi.rect.top=(K.top)+5
        kolbi.rect.left=(K.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi(nivel[1:],nivel2,PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK+1,PL,PM)

    elif nivel[0]=="L":
        kolbi.rect.top=(L.top)+5
        kolbi.rect.left=(L.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi(nivel[1:],nivel2,PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL+1,PM)

    elif nivel[0]=="M":
        kolbi.rect.top=(M.top)+5
        kolbi.rect.left=(M.left)+10
        pantalla.blit(kolbi.image,kolbi.rect)
        return Kolbi(nivel[1:],nivel2,PA,PB,PC,PD,PE,PF,PG,PH,PI,PJ,PK,PL,PM+1)
    
    
#######################################################################################################################
#funcion inicial
def juego():
    nivel=[]#lista en donde iran las posiciones donde deben ponerse las ranitas
    pygame.init()
    salir=False
    reloj1=pygame.time.Clock()


    r1=pygame.Rect(0,0,0,1)

    #se crean los rectangulos que van detras de cada "boton"
    basico=pygame.Rect(470,45,205,70)
    intermedio=pygame.Rect(470,150,205,70)
    avanzado=pygame.Rect(470,255,205,70)
    experto=pygame.Rect(470,360,205,70)

    # las fuentes de cada uno de los niveles
    FuenteBasico=pygame.font.Font(None, 48)
    TextoBasico=FuenteBasico.render("Basico",0,(0,100,0))
    FuenteIntermedio=pygame.font.Font(None, 48)
    TextoIntermedio=FuenteIntermedio.render("Intermedio",0,(0,100,0))
    FuenteAvanzado=pygame.font.Font(None, 48)
    TextoAvanzado=FuenteAvanzado.render("Avanzado",0,(0,100,0))
    FuenteExperto=pygame.font.Font(None, 48)
    TextoExperto=FuenteExperto.render("Experto",0,(0,100,0))

    while salir!=True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True

            #se elige el nivel que se desea jugar
            if r1.colliderect(basico):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pantalla.blit(tablero,(0,0))
                    nivel=niveles("basico")
                    Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            if r1.colliderect(intermedio):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pantalla.blit(tablero,(0,0))
                    nivel=niveles("intermedio")
                    Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            if r1.colliderect(avanzado):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pantalla.blit(tablero,(0,0))
                    nivel=niveles("avanzado")
                    Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)

            if r1.colliderect(experto):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pantalla.blit(tablero,(0,0))
                    nivel=niveles("experto")
                    Kolbi(nivel,nivel[:],0,0,0,0,0,0,0,0,0,0,0,0,0)
                
                
        #muestra los rectangulos y las etiquetas en la pantalla principal
        reloj1.tick(20)
        (r1.left,r1.top)=pygame.mouse.get_pos()#toma la posicion del mouse
        pantalla.blit(boton,(470,25))
        pantalla.blit(boton,(470,130))
        pantalla.blit(boton,(470,235))
        pantalla.blit(boton,(470,340))
        pantalla.blit(TextoBasico,(515,45))
        pantalla.blit(TextoIntermedio,(487,152))
        pantalla.blit(TextoAvanzado,(487,257))
        pantalla.blit(TextoExperto,(505,360))
        
        pygame.display.update()

    pygame.quit()

juego()


