import math

#LISTAS
Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
Centena=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
Millar = ["", "M", "MM", "MMM"]

#INPUT
Numero=int(input("Ingresa numero entero\n"))
ind_unidad= Numero % 10
ind_decena=int(math.floor(Numero/10))%10
ind_centena=int(math.floor(Numero/100))%10
ind_millar=int(math.floor(Numero/1000))

if(Numero>=1000): 
    print(Millar[ind_millar]+Centena[ind_centena])+Decena[ind_decena]+Unidad[ind_unidad])
elif(Numero>=100): 
    print(Centena[index_centena]+Decena[ind_decena]+Unidad[ind_unidad])
elif(Numero>=10):
    print(Decena[ind_decena]+Unidad[ind_unidad])
else:
    print(Unidad[Numero])