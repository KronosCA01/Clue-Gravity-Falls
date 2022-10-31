#Dipper y Mabel
define Dipper = Character("Dipper", color = "#FF0000") #rojo
define Mabel = Character("Mabel", color = "#ff0080") #rosa

#Villanos
define Gideon = Character("Gideon", color = "#92c5fc") #azul claro
define Bill = Character("Bill", color = "#ffff00") #amarillo
define Fantasma = Character("Fantasma", color = "#000080") #azul marino
define Cambiaformas = Character("Cambiaformas", color = "#FFFFFF") #blanco
define Bebé = Character("Bebé", color = "#008000") #verde


init python:
 import random
 i = 0


label contador:
 
 if (i==4):
     jump finales
 else:
     $i=i+1
     jump casos


label start:

    scene noche_gf

    Dipper "Era una noche como cualquiera, llena de misterios y anomalías, todo normal en Gravity Falls, decidimos hacer una reunión con nuestros enemigos para resolver nuestras diferencias, estaba repasando las notas de mi tío Ford cuando escucho a Mabel gritar"
    Mabel "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHH!!!!!!!!!!"
    Mabel "Dipper ven rápido, ha pasado algo horrible, por favor baja de ahí!!! "

    scene tienda

    show dipper2 at left:
        xzoom 1.75 yzoom 1.75
    Dipper "¿Mabel que pasa?"

    show mabel2 at right:
        xzoom 1.5 yzoom 1.5
    Mabel "Mataron al tío Stan!!!"
    Dipper "No puede ser...."   
    Dipper "Tío Stan....."
    Dipper "Prometo encontrar a quien lo hizo"
    Dipper "¿Quien lo habrá matado?"

    hide mabel2

    show gideon at right:
        xzoom .25 yzoom .25
    Dipper "Gideon..."
    Dipper "Es otro de los charlatanes del pueblo, un supuesto psíquico, no me agrada, no le agrado, y esta enamorado de Mabel"
    hide gideon

    show bill at right
    Dipper "Bill..."
    Dipper "Un ser muy poderoso en su dimensión, pero si no tiene un cuerpo que pueda poseer, su poder baja considerablemente pero sigue siendo peligroso"
    hide bill

    show fantasma2 at right:
        xzoom 2 yzoom 2
    Dipper "El fantasma del leñador..."
    Dipper "A pesar de que su odio es contra los Noroeste, es un rival temible e impredecible, hay que tener precauciones"
    hide fantasma2

    show cambiaformas at right:
        xzoom 1.5 yzoom 1.5
    Dipper "El cambiaformas..."
    Dipper "Una criatura extremadamente peligrosa, puede replicar cualquier ser vivo, por eso Ford lo encerró"
    hide cambiaformas

    show bebe tiempo at right:
        xzoom 3.5 yzoom 3.5 
    Dipper "El bebé del tiempo..."
    Dipper "No le caemos bien, desde que hicimos modificaciones en el tiempo nos tiene cierto odio, no se sabe mucho sobre el"
    hide bebe tiempo

    Dipper "Debo ser rapido, no puedo ver todo, el asesino sospecharia mucho y tratara de matarme, solo tengo 5 oportunidades para ver lo que paso, ya sea personajes, lugares y armas"

    $caso = random.randint(1,5)
    

label casos:
 if (caso==1):
     jump pistas1 
 if (caso==2):
     jump pistas2     
 if (caso==3):
     jump pistas3
 if (caso==4):
     jump pistas4
 if (caso==5):
     jump pistas5


label pistas1:
    scene noche_gf
    menu:
     "Personajes":
         jump personajes1

     "Lugares": 
         jump lugares1

     "Armas":
         jump armas1

label pistas2:
    scene noche_gf
    menu:
     "Personajes":
         jump personajes2

     "Lugares": 
         jump lugares2

     "Armas":
         jump armas2

label pistas3:
    scene noche_gf
    menu:
     "Personajes":
         jump personajes3

     "Lugares": 
         jump lugares3

     "Armas":
         jump armas3

label pistas4:
    scene noche_gf
    menu:
     "Personajes":
         jump personajes4

     "Lugares": 
         jump lugares4

     "Armas":
         jump armas4

label pistas5:
    scene noche_gf
    menu:
     "Personajes":
         jump personajes5

     "Lugares": 
         jump lugares5

     "Armas":
         jump armas5


label personajes1:
    menu:
     "Gideon":
         show gideon at right:
             xzoom .25 yzoom .25
         Gideon "Yo estaba en su cuarto viendo las cosas de mi amada Mabel"
         jump contador

     "Bill":
         show bill at right
         Bill "Yo estaba en la zona del portal pero primero queria ver como eran los baños de los humanos, pase por su cuarto y no habia nadie, el fantasma estaba conmigo"
         jump contador

     "Fantasma":
         show fantasma at left:
             xzoom .9 yzoom .9
         Fantasma "Yo estaba en la zona del portal, me encontre con el triangulo parlante"
         jump contador

     "Cambiaformas":
         show cambiaformas at left:
             xzoom 1.5 yzoom 1.5
         Cambiaformas "Yo estaba en la zona de recuerdos, vi al bebe, su vista estaba perdida en los arboles"
         jump contador
     
     "Bebé Tiempo":
         show bebe tiempo at right:
             xzoom 3.5 yzoom 3.5 
         Bebé "Yo estaba en el bosque admirando la naturaleza, me parecio ver algo blanco adentro de la tienda de recuerdos"
         jump contador

     "Volver":
         jump pistas1

label personajes2:
    menu:
     "Gideon":
         show gideon at right:
             xzoom .25 yzoom .25
         Gideon "Yo estaba en la tienda de recuerdos, quería burlarme de su mercancía tan barata, vi una criatura blanca convertirse en un pájaro"
         jump contador

     "Bill":  
         show bill at right
         Bill "Yo estaba en la parte de atrás de la cabaña, veia el feo sillón que tienen ahí"
         jump contador

     "Fantasma":
         show fantasma at left:
             xzoom .9 yzoom .9
         Fantasma "Yo estaba viendo la recamara que tienen los niños en estos tiempos, mucha tecnología, de camino vi un bebe gigante en la parte de atrás de la cabaña"
         jump contador

     "Cambiaformas":
         show cambiaformas at left:
             xzoom 1.5 yzoom 1.5
         Cambiaformas "Estaba en el bosque viendo a las aves volar, trate de hacerlo se veía divertido, un niño me estaba viendo desde la ventana"
         jump contador
     
     "Bebé Tiempo":
         show bebe tiempo at right:
             xzoom 3.5 yzoom 3.5 
         Bebé "Estaba en la parte de atrás la cabaña, vi a un hombre flotador en la recámara, pero no había nadie más que yo en esa parte de la cabaña"
         jump contador 

     "Volver":
         jump pistas2   

label personajes3:

    menu:
     "Gideon":
         show gideon at right:
             xzoom .25 yzoom .25
         Gideon "Yo estaba viendo el bosque y vi como el triángulo parlante se iba hacia la parte de atrás de la cabaña"
         jump contador

     "Bill":
         show bill at right
         Bill "Yo estaba en la parte de atrás de la cabaña, vi a Gideon en la parte del bosque, parece un hombrecito con traje, siempre me da risa verlo"
         jump contador

     "Fantasma":
         show fantasma at left:
             xzoom .9 yzoom .9
         Fantasma "Yo estaba en la tienda de recuerdos, viendo artilugios que colgaban de unas pequeñas cadenas, llaveros creo que los llaman"
         jump contador

     "Cambiaformas":
         show cambiaformas at left:
             xzoom 1.5 yzoom 1.5
         Cambiaformas "Yo estaba en el cuarto donde hay una gran estructura, creo que es para hacer un portal, de camino hacia allí vi al bebe gigante"
         jump contador
     
     "Bebé Tiempo":
         show bebe tiempo at right:
             xzoom 3.5 yzoom 3.5 
         Bebé "Yo estaba en la tienda de recuerdos, vi a una criatura blanca, dirigirse hacia un cuarto con mucha tecnología, solo lo he visto a él"
         jump contador

     "Volver":
         jump pistas3

label personajes4:

    menu:
     "Gideon":
         show gideon at right:
             xzoom .25 yzoom .25
         Gideon "Yo estaba en la tienda de recuerdos, quería ver que cosas tan absurdas venden, vi al bebe dirigirse hacia una zona secreta que tienen"
         jump contador

     "Bill":
         show bill at right
         Bill "Yo estaba viendo la recamara, tienen muchas cosas raras, muy sombrío tu lado del cuarto y el lado de Mabel está lleno de brillo, vi al fantasma ir a la parte trasera de la cabaña"
         jump contador

     "Fantasma":
         show fantasma at left:
             xzoom .9 yzoom .9
         Fantasma "Yo estaba en la parte trasera de la casa, quería observar si tenían algo interesante, lo único interesante que encontré fue al triángulo parlante, que iba a la recamara "
         jump contador

     "Cambiaformas":
         show cambiaformas at left:
             xzoom 1.5 yzoom 1.5
         Cambiaformas "Yo estaba en el portal, buscando imágenes de criaturas nuevas que yo no conociera, no encontré ninguna criatura "
         jump contador
     
     "Bebé Tiempo":
         show bebe tiempo at right:
             xzoom 3.5 yzoom 3.5 
         Bebé "Estaba en la zona del portal, la tecnología que tienen ahi es muy compleja incluso para mi, estaba solo, pero me encontré a un niño con un peinado muy grande "
         jump contador                

     "Volver":
         jump pistas4

label personajes5:
    menu:
     "Gideon":
         show gideon at right:
             xzoom .25 yzoom .25
         Gideon "Estaba en la zona del portal, estaba buscando el baño, antes de llegar a donde estaba me encontré con el fantasma"
         jump contador

     "Bill":
         show bill at right
         Bill "Estaba en el bosque viendo los árboles, en mi mundo no tenemos esas cosas, vi que el cambiaformas estaba en tu recamara"
         jump contador

     "Fantasma":
         show fantasma at left:
             xzoom .9 yzoom .9
         Fantasma "Estaba en la parte de atrás de la cabaña, extraño este plano terrenal, las flores, los animales, de camino para acá vi a un hombrecito con traje, no habia nadie conmigo"
         jump contador

     "Cambiaformas":
         show cambiaformas at left:
             xzoom 1.5 yzoom 1.5
         Cambiaformas "Estaba en la recamara, estaba viendo los libros de animales que tienen, vi algo amarrillo flotante de mi camino acá "
         jump contador
     
     "Bebé Tiempo":
         show bebe tiempo at right:
             xzoom 3.5 yzoom 3.5 
         Bebé "Estaba en la parte de atrás de la cabaña, analizaba el sofá que está ahí, en mi tiempo no hay nada de eso"
         jump contador  

     "Volver":
         jump pistas5                         


label lugares1:
    menu:
     "Tienda de recuerdos":
         scene recuerdo
         Dipper "Las tazas y los peluches estan movidos, parece que alguien estaba viendo las cosas"
         jump contador

     "Portal de Ford":
         scene portal
         Dipper "Hay rastro paranormal aquí"
         jump contador

     "Recamara de Dipper y Mabel":
         scene recamara
         Dipper "Esta todo como lo dejamos Mabel y yo en la mañana, pero falta algo, lo estaba usando para investigar acerca de la mitologia griega"
         jump contador

     "Bosque":
         scene bosque
         Dipper "Me encontre un pañal maloliente en el bote de basura cerca del bosque "
         jump contador
     
     "Parte trasera de la cabaña":
         scene atras
         Dipper "Aqui hay un monton de rocas y los lentes de mi tío Stan"
         Dipper "Esto no se quedara así Stan, te lo prometo"
         jump contador  

     "Volver":
         jump pistas1

label lugares2:
    menu:
     "Tienda de recuerdos":
         scene recuerdo
         Dipper "Aquí apesta a la loción de Gideon, como odio ese olor"
         jump contador

     "Portal de Ford":
         scene portal
         Dipper "El cuerpo de Stan está en el suelo con una extraña marca en el cuello"
         Dipper "Pagarán por lo que hicieron "
         jump contador

     "Recamara de Dipper y Mabel":
         scene recamara
         Dipper "Aquí hay ectoplasma, y algunas quemaduras en las esquinas "
         jump contador

     "Bosque":
         scene bosque
         Dipper "Las aves están asustadas unas de otras, parece como si creyeran que hay una impostora en algún lugar, que raro, el columpio no esta"
         jump contador
     
     "Parte trasera de la cabaña":
         scene atras
         Dipper "Aquí solo hay un biberon gigante, creo que ya se a quien le pertenece "
         jump contador 
     "Volver":
         jump pistas2

label lugares3:
    menu:
     "Tienda de recuerdos":
         scene recuerdo
         Dipper "Algunos peluches están llenos de saliva, parece como si alguien se los hubiera puesto en la boca"
         jump contador

     "Portal de Ford":
         scene portal
         Dipper "Los sensores del tío Ford se activaron, dicen que el cambiaformas los activo, se me olvidaba que Ford estudio al cambiaformas, quiza penso en que si él sale de esta dimensión podría ser muy peligroso"
         jump contador

     "Recamara de Dipper y Mabel":
         scene recamara
         Dipper "Mi cuarto esta lleno de sangre, y hay restos de un material verde, me resulta familiar ese residuo"
         jump contador

     "Bosque":
         scene bosque
         Dipper "Vi la suela de un zapato con la forma del nombre de Gideon, ese niño es el ser más narcisista que conozco"
         jump contador
     
     "Parte trasera de la cabaña":
         scene atras
         Dipper "Me encontré en una piedra la forma de un triángulo, tal parece que alguien se quería retratar a sí mismo en piedra"
         jump contador 
     "Volver":
         jump pistas3

label lugares4:
    menu:
     "Tienda de recuerdos":
         scene recuerdo
         Dipper "Tal parece que cierto niño de cabello gigante quería meter su propia mercancía en nuestra tienda de recuerdos, siempre quiere opacarnos"
         jump contador

     "Portal de Ford":
         scene portal
         Dipper "Aquí alguien olvidó su sonaja gigante, debió impresionarse cuando vio el portal, no lo culpo si es intimidante"
         jump contador

     "Recamara de Dipper y Mabel":
         scene recamara
         Dipper "Ese triángulo se quiso hacer el gracioso y nos invoco una cabra de 2 cabezas que no para de gritar "
         jump contador

     "Bosque":
         scene bosque
         Dipper "Aquí se encuentra el cuerpo de Stan, no parece tener nada pero lo atravesaron con algo tan caliente que pudo cauterizar la herida de inmediato"
         jump contador
     
     "Parte trasera de la cabaña":
         scene atras
         Dipper "Aqui todo esta normal, a excepción de que hay algunas quemaduras en el sofá que hay aquí"
         jump contador 

     "Volver":
         jump pistas4

label lugares5:
    menu:
     "Tienda de recuerdos":
         scene recuerdo
         Dipper "Encontré el cuerpo de Stan sin su cabeza, la colocaron en uno de los anaqueles, el corte no es limpio, como si el asesino no supiera usar el arma con la que lo asesinó"
         jump contador

     "Portal de Ford":
         scene portal
         Dipper "Aquí hay un pedazo de un trajecito azul, y un botón con la imagen de un peinado ridículo, ya sé quién estuvo aquí "
         jump contador

     "Recamara de Dipper y Mabel":
         scene recamara
         Dipper "Encontre mucho pelo, todos diferentes, y curiosamente un diente de tiburón, como si muchos animales hubieran estado en el mismo lugar, pero como entró un tiburón a mi cuarto"
         jump contador

     "Bosque":
         scene bosque
         Dipper "Alguien trato de hacer una figura en un árbol, se pensaría que es un corazón con el nombre de 2 enamorados, pero en realidad es la forma de un triángulo"
         jump contador
     
     "Parte trasera de la cabaña":
         scene atras
         Dipper "Aquí hay rastros paranormales, fuego azul, ectoplasma y tal parece que los animales están muy asustados como si hubieran visto a un muerto"
         jump contador 
     "Volver":
         jump pistas5


label armas1:
    menu:
     "Cabeza de medusa":
         show medusa at truecenter
         Dipper "La cabeza de medusa, no esta, yo la habia puesto en mi cuarto para evitar que Pato se hiciera piedra"
         jump contador

     "Cuerda irrompible": 
         show soga at truecenter:
              xzoom .5 yzoom .5
         Dipper "La cuerda la use para un columpio improvisado en el bosque, sigue ahí"
         jump contador

     "Pistola de portales":
         show pistola at truecenter:
             xzoom .25 yzoom .25
         Dipper "La pistola de portales del amigo de mi tío Ford esta en la tienda de recuerdos, les encanta presumir a esos dos"
         jump contador
             
     "Lightsaber":
         show sable at truecenter
         Dipper "El Lightsaber lo deje en la zona de portales para una pelicula que Mabel esta haciendo"
         Dipper "No tiene nada que ver con Star Wars, es una pena"
         jump contador

     "Hacha de guerra":
         show hacha at truecenter:
             xzoom .35 yzoom .35
         Dipper "El hacha de calabozos, calabozos y más calabozos, esta en la zona de atras de la cabaña pero esta limpia"
         jump contador

     "Volver":
         jump pistas1

label armas2:
    menu:
     "Cabeza de medusa":
         show medusa at truecenter
         Dipper "La cabeza está en su lugar, la guardamos en la zona del portal para que nadie la viera por error, solo alguien paranormal sobreviviría a su mirada "
         jump contador

     "Cuerda irrompible": 
         show soga at truecenter:
              xzoom .5 yzoom .5
         Dipper "La cuerda no esta en el bosque, la usamos para un columpio, pero desaparecio"
         jump contador

     "Pistola de portales":
         show pistola at truecenter:
             xzoom .25 yzoom .25
         Dipper "La pistola de Rick está donde la deje, se la robe a Ford y la puse en la recámara para analizarla después"
         jump contador
             
     "Lightsaber":
         show sable at truecenter
         Dipper "El Lightsaber de mi tío Ford está en la tienda de recuerdos, Stan lo puso ahí para hacer enojar a su hermano"
         jump contador

     "Hacha de guerra":
         show hacha at truecenter:
             xzoom .35 yzoom .35
         Dipper "El hacha la dejamos en el bosque para poder sacar un poco de leña"
         jump contador

     "Volver":
         jump pistas2

label armas3:
    menu:
     "Cabeza de medusa":
         show medusa at truecenter
         Dipper "La cabeza de medusa está en la tienda de recuerdos tapada con una manta, con un letrero que dice: aquellos que vean por debajo de esta manta serán convertidos en piedra "
         Dipper "No pasa muy seguido pero a Stan le gustaba ver a la gente curiosa convertirse en estatuas"
         jump contador

     "Cuerda irrompible": 
         show soga at truecenter:
              xzoom .5 yzoom .5
         Dipper "La soga está en sosteniendo algo del portal que Ford dijo que arreglaría"
         Dipper "Lleva ahí 2 semanas…"
         jump contador

     "Pistola de portales":
         show pistola at truecenter:
             xzoom .25 yzoom .25
         Dipper "Que raro, la pistola de portales no está, si el amigo de Ford se entera sera nuestro fin, recuerdo ponerla en la parte de atrás de la casa, bien escondida para evitar problemas"
         jump contador
             
     "Lightsaber":
         show sable at truecenter
         Dipper "Encontré el lightsaber con sangre de Stan en mi recamara, parece que donde lo deje fue en la zona donde más sangre hubo "
         jump contador

     "Hacha de guerra":
         show hacha at truecenter:
             xzoom .35 yzoom .35
         Dipper "El hacha está clavada en un tronco en el bosque, alguien estaba practicando su lanzamiento con hachas, creo que era Ford"
         jump contador

     "Volver":
         jump pistas3
    
label armas4:
    menu:
     "Cabeza de medusa":
         show medusa at truecenter
         Dipper "La cabeza de medusa la escondí en el bosque porque Stan la quería vender, no puedes vender eso, pones en riesgo a las personas, sigue en el lugar que la puse"
         jump contador

     "Cuerda irrompible": 
         show soga at truecenter:
              xzoom .5 yzoom .5
         Dipper "La soga está en la tienda de recuerdos sosteniendo algunos letreros de los productos que vendemos ahí"
         jump contador

     "Pistola de portales":
         show pistola at truecenter:
             xzoom .25 yzoom .25
         Dipper "La pistola de portales está en la zona del portal, Ford quería hacer una versión más pequeña de su portal y su amigo Rick le prestó su pistola para que el pudiera hacer la suya"
         jump contador
             
     "Lightsaber":
         show sable at truecenter
         Dipper "El lightsaber lo había puesto en la zona trasera de la cabaña para practicar un poco con él, no lo encontre por ningun lado"
         jump contador

     "Hacha de guerra":
         show hacha at truecenter:
             xzoom .35 yzoom .35
         Dipper "El hacha la puse en mi recamara para que cuando jugara calabozos, calabozos y más calabozos fuera una experiencia más inmersiva  "
         jump contador

     "Volver":
         jump pistas4

label armas5:
    menu:
     "Cabeza de medusa":
         show medusa at truecenter
         Dipper "Pusimos la cabeza en la hielera que hay en la zona trasera de la casa, para evitar que se pudriera, nos ha sacado un susto más de una vez"
         jump contador

     "Cuerda irrompible": 
         show soga at truecenter:
              xzoom .5 yzoom .5
         Dipper "La soga está en la recamara, Mabel salta con ella de vez en cuando, pero es muy larga y se cae a veces, se levanta como si nada, quisiera ser positivo como ella "
         jump contador

     "Pistola de portales":
         show pistola at truecenter:
             xzoom .25 yzoom .25
         Dipper "La pistola esta en el bosque, el amigo de Ford la lanzó por lo ebrio que estaba, la encontré y la escondí para evitar accidentes, sigue donde la deje "
         jump contador
             
     "Lightsaber":
         show sable at truecenter
         Dipper "El lightsaber está en la tienda de recuerdos como decoración y para llamar la atención de los clientes, está bajo llave y el candado sigue intacto"
         jump contador

     "Hacha de guerra":
         show hacha at truecenter:
             xzoom .35 yzoom .35
         Dipper "Que raro, el hacha no esta, estaba en la zona del portal, estaba ahí en caso de que Ford la necesitará para defenderse de algo que traspasara el portal"
         jump contador

     "Volver":
         jump pistas5


label finales:
 scene noche_gf
 if (caso==1):
     jump final1 
 if (caso==2):
     jump final2     
 if (caso==3):
     jump final3
 if (caso==4):
     jump final4
 if (caso==5):
     jump final5

# Gideon, atras de la cabaña, cabeza de medusa

label final1:
 Dipper "Ya reuni toda la información que pude"
 Dipper "Debo de saber quien fue el asesino"
 jump culpable1

label culpable1:
    menu:
     "Gideon":
         Dipper "Claro, debe de ser Gideon, nadie sabe donde estaba..."
         Dipper "Pero..."
         Dipper "¿Donde lo mato?"
         jump escena1

     "Bill":
         jump yamamo

     "Fantasma":
         jump yamamo

     "Cambia Formas":
         jump yamamo

     "Bebé Tiempo":
         jump yamamo

label escena1:
    menu:
     "Tienda de recuerdos":
         jump yamamo

     "Portal de Ford":
         jump yamamo

     "Recamara de Dipper y Mabel":
         jump yamamo

     "Bosque":
         jump yamamo
     
     "Parte trasera de la cabaña":
         scene atras
         Dipper "Es cierto habia muchas rocas de forma extraña, pero no habia sangre"
         Dipper "Eso solo significa una cosa, el arma que uso fue..."
         jump artefacto1 

label artefacto1:
    menu:
     "Cabeza de medusa":
         show medusa at truecenter
         Dipper "Por supuesto, ahora todo cuadra"
         jump victoria1

     "Cuerda irrompible": 
         jump yamamo
     
     "Pistola de portales":
         jump yamamo
     
     "Lightsaber":
         jump yamamo

     "Hacha de guerra":
         jump yamamo
     
label victoria1:
 scene tienda
 show dipper2 at left:
     xzoom 1.75 yzoom 1.75
 Dipper "Gideon, tu mataste a Stan"
 show gideon at right:
     xzoom .25 yzoom .25
 Gideon "Estas loco, claro que no"
 Dipper "Reuní toda la informacion, nadie te vio durante el asesinato"
 Dipper "Encontre todas las armas donde las había dejado, pero no encontre la cabeza de medusa que Ford trajo de su viaje en el tiempo"
 Dipper "Y cuando encontre unos piedras de forma sosechosa en la parte de atras de la cabaña junto con los lentes de Stan, ya sabía todo"
 Gideon "Te maldigo Diper Pines y tu maldito cerebro curioso, primero mate a Stan y después a ti pero me descubriste"
 Gideon "Mabel iba a ser mia"
 Gideon "MIIIIIIIAAAAAAA!!!"
 Dipper "Pues ya te descubrí, y pagarás por lo que hiciste"
 jump ganamos

# Bill, Portal, Cuerda irrompible

label final2:
 Dipper "Ya reuni toda la información que pude, debo de saber quien fue el asesino"
 jump culpable2

label culpable2:
    menu:
     "Gideon":
         jump yamamo

     "Bill":
         Dipper "Claro, debe de ser Bill, nadie sabe donde estaba..."
         Dipper "Pero..."
         Dipper "¿Donde lo mato?"
         jump escena2

     "Fantasma":
         jump yamamo

     "Cambia Formas":
         jump yamamo

     "Bebé Tiempo":
         jump yamamo

label escena2:
    menu:
     "Tienda de recuerdos":
         jump yamamo

     "Portal de Ford":
         scene portal
         Dipper "Por supuesto, ahí estaba el cuerpo de Stan con unas marcas en el cuello"
         Dipper "Eso solo significa una cosa, el arma que uso fue..."
         jump artefacto2 

     "Recamara de Dipper y Mabel":
         jump yamamo

     "Bosque":
         jump yamamo
     
     "Parte trasera de la cabaña":
         jump yamamo

label artefacto2:
    menu:
     "Cabeza de medusa":
         jump yamamo

     "Cuerda irrompible":
         show soga at truecenter:
              xzoom .5 yzoom .5
         Dipper "Por supuesto, ahora todo cuadra"
         jump victoria2
     
     "Pistola de portales":
         jump yamamo
     
     "Lightsaber":
         jump yamamo

     "Hacha de guerra":
         jump yamamo
     
label victoria2:
 scene tienda
 show dipper2 at left:
     xzoom 1.75 yzoom 1.75
 Dipper "Bill, tu mataste a Stan"
 show bill at right:
 Bill "Perdiste la cabeza niño, claro que no"
 Dipper "Reuní toda la informacion, nadie te vio durante el asesinato"
 Dipper "Desapareció la cuerda que estaba en el bosque y solo una entidad paranormal podría sobrevivir a la mirada de medusa"
 Dipper "Lo ahorcaste hasta su muerte maldito triangulo amarillo"
 Bill "Maldito niño flacucho, como lograste descubrirme"
 Bill "Lo maté porque su gran bocota siempre me molestaba, quería ver como la insignificante vida de tu tío salía durante cada aliento que él desesperadamente trataba de dar"
 Bill "Y después te iba a matar a ti "
 Dipper "Te encerraré en una burbuja dimensional y te quedaras ahí por el resto de la eternidad"
 jump ganamos

# Fantasma, recamara, pistola de portales

label final3:
 Dipper "Ya reuni toda la información que pude, debo de saber quien fue el asesino"
 jump culpable3

label culpable3:
    menu:
     "Gideon":
         jump yamamo

     "Bill":
         jump yamamo

     "Fantasma":
         Dipper "Claro, debe de ser el fantasma, nadie sabe donde estaba..."
         Dipper "Pero..."
         Dipper "¿Donde lo mato?"
         jump escena3

     "Cambia Formas":
         jump yamamo

     "Bebé Tiempo":
         jump yamamo

label escena3:
    menu:
     "Tienda de recuerdos":
         jump yamamo

     "Portal de Ford":
         jump yamamo

     "Recamara de Dipper y Mabel":
         scene recamara
         Dipper "Por supuesto, la sangre era de Stan y no hay ningun otro rastro"
         Dipper "Eso solo significa una cosa, el arma que uso fue..."
         jump artefacto3 

     "Bosque":
         jump yamamo
     
     "Parte trasera de la cabaña":
         jump yamamo

label artefacto3:
    menu:
     "Cabeza de medusa":
         jump yamamo

     "Cuerda irrompible":
          jump yamamo
     
     "Pistola de portales":
         show pistola at truecenter:
             xzoom .25 yzoom .25
         Dipper "Por supuesto, ahora todo cuadra"
         jump victoria3

     
     "Lightsaber":
         jump yamamo

     "Hacha de guerra":
         jump yamamo
     
label victoria3:
 scene tienda
 show dipper2 at left:
     xzoom 1.75 yzoom 1.75
 Dipper "Oye Fantasma, tu mataste a Stan"
 show fantasma2 at right:
      xzoom 2 yzoom 2
 Fantasma "Como te atreves a decir tal falsedad, por supuesto que yo no lo hice"
 Dipper "Reuní toda la informacion, nadie te vio durante el asesinato"
 Dipper "La pistola de portales no estaba en el lugar donde yo la puse, y mi cuarto estaba lleno de sangre"
 Dipper "Lo mandaste a la dimesion de las trituradoras, un lugar que Ford nos dijo que era peligroso"
 Fantasma "Maldigo a la tecnología que es tan complicada"
 Fantasma"El se burlaba de la gente del pueblo, igual que los Noroeste se burlaron de mi, por eso lo mate, me recordo mi propio sufrimiento"
 Fantasma "No podía usar un hacha porque sería muy obvio pero me descubriste de todas formas "
 Dipper "Estarás en un espejo de plata por el resto de tu existencia en este plano terrenal "
 jump ganamos

# Cambiaformas, Bosque, lightsaber

label final4:
 Dipper "Ya reuni toda la información que pude, debo de saber quien fue el asesino"
 jump culpable4

label culpable4:
    menu:
     "Gideon":
         jump yamamo

     "Bill":
         jump yamamo

     "Fantasma":
         jump yamamo

     "Cambia Formas":
         Dipper "Claro, debe de ser el Cambiaformas, nadie sabe donde estaba..."
         Dipper "Pero..."
         Dipper "¿Donde lo mato?"
         jump escena4

     "Bebé Tiempo":
         jump yamamo

label escena4:
    menu:
     "Tienda de recuerdos":
         jump yamamo

     "Portal de Ford":
         jump yamamo

     "Recamara de Dipper y Mabel":
         jump yamamo

     "Bosque":
         scene bosque
         Dipper "Por supuesto, la herida que hay en cuerpo de Stan es algo que solo un arma muy sofisticada puede hacer"
         Dipper "Eso solo significa una cosa, el arma que uso fue..."
         jump artefacto4     
     
     "Parte trasera de la cabaña":
         jump yamamo

label artefacto4:
    menu:
     "Cabeza de medusa":
         jump yamamo

     "Cuerda irrompible":
          jump yamamo
     
     "Pistola de portales":
         jump yamamo
     
     "Lightsaber":
         show sable at truecenter
         Dipper "Por supuesto, ahora todo cuadra"
         jump victoria4

     "Hacha de guerra":
         jump yamamo
     
label victoria4:
 scene tienda
 show dipper2 at left:
     xzoom 1.75 yzoom 1.75
 Dipper "Oye Cambiaformas, tu mataste a Stan"
 show cambiaformas at right:
      xzoom 1.5 yzoom 1.5
 Cambiaformas "No se de lo que me hablas, eso no es cierto"
 Dipper "Reuní toda la informacion, nadie te vio durante el asesinato"
 Dipper "El lightsaber no estaba en el lugar donde yo lo puse, y encontre a Stan con una herida muy precisa y sofisticada"
 Dipper "Ninguna otra arma puede a hacer eso, lo apuñalaste a sangre fria"
 Cambiaformas "Maldito niño con gorra de pino, si, yo lo mate"
 Cambiaformas"De todas las criaturas que conozco tu tío era la que más asco me daba, inventaba criaturas absurdas y siempre que queria replicarlas no podía"
 Cambiaformas "Use esa arma porque pense que el bebe del tiempo sería a quien inculparias, pero me descubriste"
 Dipper "Te congelare y no saldras del cuarto de crigenización nunca"
 jump ganamos

# Bebe, recuerdo, hacha

label final5:
 Dipper "Ya reuni toda la información que pude, debo de saber quien fue el asesino"
 jump culpable5

label culpable5:
    menu:
     "Gideon":
         jump yamamo

     "Bill":
         jump yamamo

     "Fantasma":
         jump yamamo

     "Cambia Formas":
         jump yamamo

     "Bebé Tiempo":
         Dipper "Claro, debe de ser el bebé del tiempo, nadie sabe donde estaba..."
         Dipper "Pero..."
         Dipper "¿Donde lo mato?"
         jump escena5

label escena5:
    menu:
     "Tienda de recuerdos":
         scene recuerdo
         Dipper "Por supuesto, la herida que hay en el cuello de Stan no es limpia y parece que el arma que usó nunca la hubiera usado antes, como si fuera muy antiguo para el "
         Dipper "Eso solo significa una cosa, el arma que uso fue..."
         jump artefacto5   


     "Portal de Ford":
         jump yamamo

     "Recamara de Dipper y Mabel":
         jump yamamo

     "Bosque":
         jump yamamo
     
     "Parte trasera de la cabaña":
         jump yamamo

label artefacto5:
    menu:
     "Cabeza de medusa":
         jump yamamo

     "Cuerda irrompible":
          jump yamamo
     
     "Pistola de portales":
         jump yamamo
     
     "Lightsaber":
         jump yamamo

     "Hacha de guerra":
         show hacha at truecenter:
             xzoom .35 yzoom .35
         Dipper "Por supuesto, ahora todo cuadra"
         jump victoria5
     
label victoria5:
 scene tienda
 show dipper2 at left:
     xzoom 1.75 yzoom 1.75
 Dipper "Bebé del tiempo, tu mataste a Stan"
 show bebe tiempo at right:
     xzoom 3.5 yzoom 3.5 
 Bebé "Claro que no, eso alteraria las cosas en la linea del tiempo"
 Dipper "Reuní toda la informacion, nadie te vio durante el asesinato"
 Dipper "El hacha no estaba en el lugar donde yo lo puse, y encontre a Stan con un corte en cuello muy mal hecho, como nunca usaste un hacha no supiste como usarla adecuadamente"
 Dipper "Trataste de cortarle la cabeza varias veces y lo mataste de una manera cruel"
 Bebé "Maldito ser inferior, como lo dedujiste"
 Bebé"Su mera existencia era una bomba de tiempo, si no lo eliminaba hubiera causado una catastrofe temporal"
 Bebé "Trate de usar un arma que no me relacionará de manera directa, pero mi inexperiencia con un arma tan primitiva me delato"
 Dipper "Yo me encargaré de que la linea del tiempo sea una catastrofe que no podrás arreglar"
 jump ganamos


label ganamos:
 scene noche_gf
 show dipper2 at left:
     xzoom 1.75 yzoom 1.75
 Dipper "Lo logre Stan,puedes descansar en paz"
 return

label yamamo:
 scene noche_gf
 show dipper2 at left:
     xzoom 1.75 yzoom 1.75
 Dipper "No...."
 Dipper "La evidencia no cuadra..."
 Dipper "No lo puedo resolver"
 Dipper "Stan, te fallé"
 Dipper "Perdonamé"
 return