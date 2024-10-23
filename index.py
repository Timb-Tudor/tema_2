text = "Banca Centrală Europeană (BCE), instituţia care stabileşte dobânda de referinţă pentru cele 20 de ţări aflate în zona euro, ar putea anunța o nouă reducere a ratelor, după ce inflaţia a coborât sub nivelul ultimilor trei ani."

lungime = len(text) // 2

prima_parte = text[:lungime]
a_doua_parte = text[lungime:]

prima_parte_upper = prima_parte.upper()
prima_parte_strip = prima_parte_upper.strip()

a_doua_parte_inversare = a_doua_parte[::-1]
a_doua_parte_capitalize = a_doua_parte_inversare.capitalize()

import string
a_doua_parte_punctuatie = a_doua_parte_capitalize.translate(str.maketrans('', '', string.punctuation))

rezultat_final = prima_parte_strip + a_doua_parte_punctuatie
print(rezultat_final)





