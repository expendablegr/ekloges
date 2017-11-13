import list
psifoi = []
onomata = ["xristina" ,"dionisis"  "kevin", "aourel", "giorgos"]
print "ta onomata ton ipopsifion einai:", onomata
ar_on=raw_input('dose  onoma: ')
if ar_on == "xristina" or "dionisis" or "kevin" or "aourel" or "giorgos": #edo mporoun na prosthetoun k alla onomata etsi oste na ginete elenxos oti einai sosta k oti iparxoun
  while ar_on!="telos":
    if ar_on=="xristina":
      psifoi.insert(0,"xristina")
    elif ar_on=="dionisis":
      psifoi.insert(1,"dionisis")
    elif ar_on=="kevin":
      psifoi.insert(2,"kevin")
    elif ar_on=="aourel":
      psifoi.insert(3,"aourel")
    elif ar_on=="giorgos":
      psifoi.insert(4,"giorgos")
    ar_on=raw_input("dose onoma: ")
    while not (ar_on != "xristina" and "dionisis" and "kevin" and "aourel" and "giorgos"):
      ar_on=raw_input("dose onoma to proigoumeno itan lahos: ")
print "h psifoi ths xristinas einai: ",psifoi.count("xristina")
print "h psifoi toy dionisi einai: ",psifoi.count("dionisis")
print "h psifoi toy kevin einai: ",psifoi.count("kevin")
print "h psifoi toy aourel einai: ",psifoi.count("aourel")
print "h psifoi toy giorgou einai: ",psifoi.count("giorgos")
