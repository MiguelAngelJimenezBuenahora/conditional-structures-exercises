#El joven periodista Solarrabietas debe relatar un partido de tenis, pero no conoce las reglas del deporte. En particular, no ha logrado aprender cómo saber si un set ya terminó, y quién lo ganó.

#Un partido de tenis se divide en sets. Para ganar un set, un jugador debe ganar 6 juegos, pero además debe haber ganado por lo menos dos juegos más que su rival. Si el set está empatado a 5 juegos, el ganador es el primero que llegue a 7. Si el set está empatado a 6 juegos, el set se define en un último juego, en cuyo caso el resultado final es 7-6.

#Sabiendo que el jugador A ha ganado m juegos, y el jugador B, n juegos, al periodista le gustaría saber:

#    si A ganó el set, o
#    si B ganó el set, o
#    si el set todavía no termina, o
#    si el resultado es inválido (por ejemplo, 8-6 o 7-3).

#Desarrolle un programa que solucione el problema de Solarrabietas:

#Juegos ganados por A: 4
#Juegos ganados por B: 5
#Aun no termina

#Juegos ganados por A: 5
#Juegos ganados por B: 7
#Gano B

#Juegos ganados por A: 5
#Juegos ganados por B: 6
#Aun no termina

#Juegos ganados por A: 3
#Juegos ganados por B: 7
#Invalido

#Juegos ganados por A: 6
#Juegos ganados por B: 4
#Gano A

playerA = int(input("Games wins for player A: "))
playerB = int(input("Games wins for player B: "))

def select_a_winner(m,n):
    m = playerA
    n = playerB

    if m >= 6 and m - n >= 2:
        return f"Win the set the player A: {m}-{n}"
    elif n >= 6 and n - m >= 2:
        return f"Win the set the player B: {m}-{n}"
    elif m == 5 and n == 6:
        return "The set is score: 5-6, win the first to arrive 7."
    elif m == 6 and n == 5:
        return "The set is score: 6-5, win the first to arrive 7."
    elif m == 6 and n == 6:
        return "the set is draw with score: 6-6, last game."
    else:
        return "The set not finish ."
print (select_a_winner(playerA , playerB))


