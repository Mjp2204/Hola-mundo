Pintas = [ "Picas", "Treboles", "Diamantes", "Corazones" ]
valores = ["A", "J", "Q", "K"] + [str(i) for i in range (2,11)]
mazo = [(u,p) for u in valores for p in Pintas]
for c in mazo:
    print (c)