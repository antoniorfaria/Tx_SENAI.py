kml=int(input(" km percorrido:"))

if kml > 200:
    valorApagar= 0.45*kml
    print(f"valor a pagar {valorApagar}")
else:
    valorApagar= 0.50*kml
    print(f"valor a pagar {valorApagar}")
    

