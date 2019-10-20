def DeuxVersDix(N): # N (2) -> N (10) | N (2) _doit_ être un String
    digit_array = []
    for char in N:
        digit_array.append("01".index(char))
    base_10_de_N = 0
    for digit_index in range(len(digit_array)):
        base_10_de_N += 2 ** digit_index * digit_array[-digit_index - 1]
    return base_10_de_N

def DixVersDeux(N): # N (10) -> N (2) | N (10) _doit_ être in Integer
    output = ""
    while N != 0:
        output = "{}{}".format(N % 2, output)
        N = N // 2
    return output


while True:
    nom_de_la_fonction = input("Voulez-vous utiliser la fonction \"DeuxVersDix\" ou bien \"DixVersDeux\" (réponse insensible à la case) : ").lower()
    if nom_de_la_fonction == "deuxversdix":
        nombre_binaire = input("Rentrez la représentation binaire d'un nombre, vous pouvez utiliser les chiffres 0 et 1 : ")
        print("La représentation décimale de ce nombre est {}".format( DeuxVersDix(nombre_binaire) ))
    elif nom_de_la_fonction == "dixversdeux":
        nombre_decimal = int(input("Rentrez la représentation décimale d'un nombre, vous pouvez utiliser les chiffres 0, 1, 2, 3, 4, 5, 6, 7, 8 et 9 : "))
        print("La représentation binaire de ce nombre est {}".format( DixVersDeux(nombre_decimal) ))
    else:
        print("erreur : le nom de fonction n'est pas reconnu")
    if input("Voulez-vous recommencer (oui pour recommencer) : ").lower() != "oui":
        print("Vous avez bien quitté le programme")
        break