def sistema_experto_videojuegos_señorazo():
    aventura = input("¿Te gustan los juegos de aventura? (s/n): ").lower() == 's'
    accion = input("¿Te gustan los juegos de acción? (s/n): ").lower() == 's'
    rpg = input("¿Te gustan los juegos de RPG? (s/n): ").lower() == 's'

    if aventura and accion and rpg:
        return "Podrias jugar Lies of P"
    elif aventura and accion:
        return "Podrias jugar God of War"
    elif accion and not aventura and not rpg:
        return "Podrias jugar Call of Duty"
    elif rpg and not aventura and not accion:
        return "Podrias jugar Dark Souls"
    elif rpg and accion and not aventura:
        return "Podrias jugar Dark Souls o Lies of P"
    else:
        return "Diabloo, que dificil me la pusite, igual juga god of war que es el mejor."

print(sistema_experto_videojuegos_señorazo())
