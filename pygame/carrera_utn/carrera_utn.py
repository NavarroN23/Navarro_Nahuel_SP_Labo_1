import pygame
from datos import lista
from colores import *
from funciones import *

ANCHO_VENTANA = 850
ALTO_VENTANA = 600
contador_preguntas = -1
puntaje = 0
errores = 0
segundos = "5"
ingreso = ""
jugador = ""
fin_juego = False
bandera_ingreso = False
fin_tiempo = False
bandera_pregunta = False
bandera_mal = False
bandera_bien = False
bandera_abajo = False
bandera_avanzar = False
bandera_retroceder = False
pos_personaje = [104,245]
lista_jugadores = leer_json("pygame\carrera_utn\puntajes_y_nombres.json")
if not lista_jugadores:
    lista_jugadores = []
# CARGA Y ESCALADO DE IMAGENES------------------------------------------------------ 
imagen = pygame.image.load("pygame\carrera_utn\imagenes\imagen.JPG")
imagen = pygame.transform.scale(imagen,(200,150))
personaje = pygame.image.load("pygame\carrera_utn\imagenes\personaje.JPG")
personaje = pygame.transform.scale(personaje,(40,80))
# guardo todos los elementos de la lista original en listas individuales 
lista_preguntas = []
lista_opciones_a = []
lista_opciones_b = []
lista_opciones_c = []
lista_respuesta = []
for elemento in lista:
    lista_preguntas.append(elemento["pregunta"])
    lista_opciones_a.append(elemento["a"])
    lista_opciones_b.append(elemento["b"])
    lista_opciones_c.append(elemento["c"])
    lista_respuesta.append(elemento["correcta"])

pygame.init()
# TEMPORIZADOR--------------------------------------------------------
tiempo_segundos = pygame.USEREVENT
pygame.time.set_timer(tiempo_segundos, 1000)
# TEXTOS Y FUENTES----------------------------------------------------
fuente_chica = pygame.font.SysFont("Arial", 20)
fuente_chica2 = pygame.font.SysFont("Arial", 15)
fuente_grande = pygame.font.SysFont("Arial", 30)
btn_comenzar = fuente_grande.render("Comenzar", True, BLACK)
btn_terminar = fuente_grande.render("Terminar", True, BLACK)
btn_salir = fuente_grande.render("Salir", True, BLACK)
score = fuente_grande.render("Puntaje:", True, BLACK)
tiempo = fuente_grande.render("Tiempo:", True, BLACK)
titulo_lista = fuente_grande.render("Puntajes:", True, WHITE)
# texto casillas
salida = fuente_chica.render("salida->", True, BLACK)
llegada = fuente_chica.render("llegada", True, BLACK)
avanzar = fuente_chica2.render("Avanzar", True, BLACK)
retroceder = fuente_chica2.render("Retroceder", True, BLACK)
# texto puntaje y tiempo
texto_puntaje = fuente_grande.render(str(puntaje), True, BLACK)
texto_tiempo = fuente_grande.render(str(segundos), True, BLACK)
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
ingreso_rect = pygame.Rect(350,275,150,40)
jugador_rect = pygame.Rect(356,150,150,40)
# BUCLE PRINCIPAL-------------------------------------------------------------------------------------------------------
bandera_correr = True
while bandera_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: 
            bandera_correr = False  
        if evento.type == pygame.USEREVENT:
            if evento.type == tiempo_segundos:
                if bandera_pregunta == True and fin_tiempo == False:
                    segundos = int(segundos) - 1
                    if int(segundos) == 0:
                        fin_tiempo = True
                        bandera_mal = True
        if fin_juego:
            fin_tiempo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    ingreso = ingreso[0:-1]
                elif evento.key == pygame.K_RETURN:
                    bandera_ingreso = True
                elif len(ingreso) < 10 and not bandera_ingreso:
                    ingreso += evento.unicode
            
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            print(posicion_click)
            #apreta el boton Comenzar-----------------------------------------------------------------------
            if ((posicion_click[0] > 220 and posicion_click[0] < 350) and 
                (posicion_click[1] > 510 and posicion_click[1] < 570)):
                    fin_juego = False
                    bandera_ingreso = False
                    bandera_mal = False
                    bandera_bien = False
                    bandera_avanzar = False
                    bandera_retroceder = False
                    errores = 0
                    segundos = "5"
                    fin_tiempo = False
                    contador_preguntas = 0

                    pregunta = fuente_chica.render(lista_preguntas[contador_preguntas], True, BLACK)
                    opcion_a = fuente_grande.render(lista_opciones_a[contador_preguntas], True, BLACK)
                    opcion_b = fuente_grande.render(lista_opciones_b[contador_preguntas], True, BLACK)
                    opcion_c = fuente_grande.render(lista_opciones_c[contador_preguntas], True, BLACK)

                    bandera_pregunta = True

            if bandera_pregunta == True:#comprueba si se esta mostrando alguna pregunta
                #opcion A----------------------------------------------------------------------------------------------
                if ((posicion_click[0] > 225 and posicion_click[0] < 675) and 
                    (posicion_click[1] > 53 and posicion_click[1] < 93)): 
                    if lista_respuesta[contador_preguntas] == "a":
                        bandera_bien = True
                    else:
                        errores += 1
                #opcion B----------------------------------------------------------------------------------------------
                if ((posicion_click[0] > 225 and posicion_click[0] < 675) and 
                    (posicion_click[1] > 103 and posicion_click[1] < 143)): 
                    if lista_respuesta[contador_preguntas] == "b":
                        bandera_bien = True
                    else:
                        errores += 1
                #opcion C----------------------------------------------------------------------------------------------
                if ((posicion_click[0] > 225 and posicion_click[0] < 675) and 
                    (posicion_click[1] > 153 and posicion_click[1] < 193)): 
                    if lista_respuesta[contador_preguntas] == "c":
                        bandera_bien = True
                    else:
                        errores += 1
            #preciona el boton terminar------------------------------------
            if ((posicion_click[0] > 495 and posicion_click[0] < 625) and 
                (posicion_click[1] > 510 and posicion_click[1] < 570)):
                fin_juego = True
            #preciona el boton salir---------------------------------------
            if ((posicion_click[0] > 350 and posicion_click[0] < 480) and 
                (posicion_click[1] > 510 and posicion_click[1] < 570)):
                if fin_juego and bandera_ingreso:
                    puntaje = 0
                    errores = 0
                    ingreso = ""
                    fin_juego = False
                    bandera_ingreso = False
                    fin_tiempo = False
                    bandera_pregunta = False
                    bandera_mal = False
                    bandera_bien = False
                    bandera_avanzar = False
                    bandera_retroceder = False
                    bandera_abajo = False
                    pos_personaje = [104,245]
                
    if errores == 2:
        bandera_mal = True

    if bandera_mal:
        bandera_mal = False
        errores = 0
        segundos = "5"
        fin_tiempo = False

        if contador_preguntas < (len(lista)-1):
            contador_preguntas += 1
        else:
            contador_preguntas = 0

        pregunta = fuente_chica.render(lista_preguntas[contador_preguntas], True, BLACK)
        opcion_a = fuente_grande.render(lista_opciones_a[contador_preguntas], True, BLACK)
        opcion_b = fuente_grande.render(lista_opciones_b[contador_preguntas], True, BLACK)
        opcion_c = fuente_grande.render(lista_opciones_c[contador_preguntas], True, BLACK)
        if not bandera_abajo:
            pos_personaje[0] -= 58
        if bandera_abajo:
            pos_personaje[0] += 58

    elif bandera_bien:
        bandera_bien = False
        puntaje += 10
        texto_puntaje = fuente_grande.render(str(puntaje), True, BLACK)
        errores = 0
        segundos = "5"

        if contador_preguntas < (len(lista)-1):
            contador_preguntas += 1
        else:
            contador_preguntas = 0

        pregunta = fuente_chica.render(lista_preguntas[contador_preguntas], True, BLACK)
        opcion_a = fuente_grande.render(lista_opciones_a[contador_preguntas], True, BLACK)
        opcion_b = fuente_grande.render(lista_opciones_b[contador_preguntas], True, BLACK)
        opcion_c = fuente_grande.render(lista_opciones_c[contador_preguntas], True, BLACK)
        if not bandera_abajo:
            pos_personaje[0] += 116
        if bandera_abajo:
            pos_personaje[0] -= 116

    # COMPROBAR CORDENADAS PJ------------------------------------------------------------------------------------------
    if pos_personaje[0] == 510 and not bandera_avanzar:# cae en casilla avanzar
        if not bandera_abajo:
            pos_personaje[0] +=58
            bandera_avanzar = True
    if pos_personaje[0] == 394 and not bandera_retroceder:# cae en casilla retroceder
        if bandera_abajo:
            pos_personaje[0] += 116
            bandera_retroceder = True
    if bandera_pregunta and pos_personaje[0] < 220 and not bandera_abajo:#evita que retroceda si esta en la primera casilla
        pos_personaje[0] = 220
        pos_personaje[1] = 245
    if pos_personaje[0] < 220 and bandera_abajo:#supera la ultima casilla (termina el juego)
        pos_personaje[0] = 135
        pos_personaje[1] = 345
        fin_tiempo = True
        fin_juego = True
    if pos_personaje[0] > 671 and not bandera_abajo:# avanza desde la ultima casilla de la fila de arriba
        bandera_abajo = True
        pos_personaje[0] = 626
        pos_personaje[1] = 345
    elif pos_personaje[0] > 671 and bandera_abajo:# retrocede desde la primer casilla de la fila de abajo
        bandera_abajo = False
        pos_personaje[0] = 626
        pos_personaje[1] = 245
# MOSTRAR ELEMENTOS PANTALLA--------------------------------------------------------------------------------------------
    pantalla.fill(CYAN4)
    if not fin_juego:
        texto_tiempo = fuente_grande.render(str(segundos), True, BLACK)
        # BOTONES COMENZAR Y TERMINAR------------------------------------------
        pygame.draw.rect(pantalla,CYAN5,(220,510,130,60))
        pantalla.blit(btn_comenzar,(230,520))
        pygame.draw.rect(pantalla,CYAN5,(495,510,130,60))
        pantalla.blit(btn_terminar,(510,520))
        # CUADRO DE PREGUNTAS Y OPCIONES---------------------------------------
        pygame.draw.rect(pantalla,GREEN,(220,10,460,200))
        if bandera_pregunta == True:
            pantalla.blit(pregunta,(225,15))
            pygame.draw.rect(pantalla, GREEN4, [225, 53, 450, 40])
            pantalla.blit(opcion_a,(230,55))

            pygame.draw.rect(pantalla, GREEN4, [225, 103, 450, 40])
            pantalla.blit(opcion_b,(230,105))

            pygame.draw.rect(pantalla, GREEN4, [225, 153, 450, 40])
            pantalla.blit(opcion_c,(230,155))
        # CASILLAS-------------------------------------------------------------
        pygame.draw.rect(pantalla,ORANGE,(215,300,50,50))
        pygame.draw.rect(pantalla,GREEN,(273,300,50,50))
        pygame.draw.rect(pantalla,YELLOW1,(331,300,50,50))
        pygame.draw.rect(pantalla,COLOR_CELESTE,(389,300,50,50))
        pygame.draw.rect(pantalla,RED1,(447,300,50,50))
        pygame.draw.rect(pantalla,VIOLET,(505,300,50,50))
        pygame.draw.rect(pantalla,YELLOW1,(563,300,50,50))
        pygame.draw.rect(pantalla,GREEN,(621,300,50,50))
        # segunda fila
        pygame.draw.rect(pantalla,ORANGE,(215,400,50,50))
        pygame.draw.rect(pantalla,GREEN,(273,400,50,50))
        pygame.draw.rect(pantalla,YELLOW1,(331,400,50,50))
        pygame.draw.rect(pantalla,COLOR_CELESTE,(389,400,50,50))
        pygame.draw.rect(pantalla,RED1,(447,400,50,50))
        pygame.draw.rect(pantalla,VIOLET,(505,400,50,50))
        pygame.draw.rect(pantalla,YELLOW1,(563,400,50,50))
        pygame.draw.rect(pantalla,GREEN,(621,400,50,50))
        # TEXTO CASILLAS-------------------------------------------------------
        pantalla.blit(salida,(105,320))
        pantalla.blit(llegada,(131,420))
        if not bandera_avanzar: 
            pantalla.blit(avanzar,(506,323))
        if not bandera_retroceder:
            pantalla.blit(retroceder,(384,423))
        # TIEMPO Y PUNTAJE-----------------------------------------------------
        pantalla.blit(score,(690,90))
        pantalla.blit(texto_puntaje,(781,91))
        pantalla.blit(tiempo,(690,10))
        pantalla.blit(texto_tiempo,(781,11))
        # IMAGENES-------------------------------------------------------------
        pantalla.blit(imagen,(10,10))
        pantalla.blit(personaje,(pos_personaje))
    # INGRESO DEL USUARIO
    if fin_juego:
        if not bandera_ingreso: 
            guardado = False
            pygame.draw.rect(pantalla,BLACK,ingreso_rect,2)
            texto_superficie = fuente_chica.render(ingreso,True,BLACK)
            pantalla.blit(texto_superficie,(ingreso_rect.x+5,ingreso_rect.y +5))
        else:
            if not guardado:
                lista_jugadores = agregar_a_lista(lista_jugadores, ingreso, puntaje)
                guardar_json(lista_jugadores,"pygame\carrera_utn\puntajes_y_nombres.json")
                guardado = True
            contador = 0
            lista_top_jugadores = ordenar_por_clave(lista_jugadores)
            pantalla.blit(titulo_lista,(356,100))
            jugador_rect.y = 150
            for elemento in lista_top_jugadores:
                contador += 1
                jugador = ""
                jugador = elemento["nombre"] +": "+ str(elemento["puntaje"])
                if contador < 11:
                    texto_jugador = fuente_chica.render(jugador,True,BLACK)
                    pantalla.blit(texto_jugador,(jugador_rect.x,jugador_rect.y))
                    jugador_rect.y += 20
            pygame.draw.rect(pantalla,CYAN5,(350,510,130,60))
            pantalla.blit(btn_salir,(365,520))
    pygame.display.flip()
pygame.quit()