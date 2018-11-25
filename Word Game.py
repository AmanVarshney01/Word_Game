print "Word Game " \
      "Shuru ho rha hai!!"
print ""
print """1 = Ladka
2 = Ladki"""
gender = (input("App Ladki hai ya Ladka?: "))
if gender == 1:
    story1 = "_ subhe subhe utha or usne dekha kai bohut sare _ uske aas pass chakre lga ke " \
        "uspe _ fek rhe hai."
    story2 = "Jab _ nahane gya toh usne ek bda sa _ apni balti me dekha, " \
        "phir wo ghabra gya ghabrane ke " \
        "baad usne _ ko phone lagaya jo ki bda _ tha."
    story3 = "_ aya or usne _ ko bhaga dia. _ " \
        "ko phir bhook lagi or usne _ ko hi kha lia. "
    name = (raw_input("Apna name daliye: "))
    insect = (raw_input("Ek kide ka name daliye: "))
    food = (raw_input("Ek khane ka name daliye: "))
    animal = (raw_input("Ek janwar ka name daliye: "))
    animal2 = (raw_input("Ek or janwar ka name daliye: "))
    adjective = (raw_input("Apne app ko 1 shabd me btaiye: "))
    STORY1 = story1.replace("_", "%s")
    STORY2 = story2.replace("_", "%s")
    STORY3 = story3.replace("_", "%s")
    print STORY1 % (name, insect, food)
    print STORY2 % (name, animal, animal2, adjective)
    print STORY3 % (animal2, animal, animal2, name)
else:
    story1 = "_ subhe subhe uthi or usne dekha kai bohut sare _ uske aas pass chakre lga ke " \
        "uspe _ fek rhe hai."
    story2 = "Jab _ nahane gyi toh usne ek bda sa _ apni balti me dekha, " \
        "phir wo ghabra gyi ghabrane ke " \
        "baad usne _ ko phone lagaya jo ki bda _ tha."
    story3 = "_ aya or usne _ ko bhaga dia. _ " \
        "ko phir bhook lagi or usne _ ko hi kha lia. "
    name = (raw_input("Apna name daliye: "))
    insect = (raw_input("Ek kide ka name daliye: "))
    food = (raw_input("Ek khane ka name daliye: "))
    animal = (raw_input("Ek janwar ka name daliye: "))
    animal2 = (raw_input("Ek or janwar ka name daliye: "))
    adjective = (raw_input("Apne app ko 1 shabd me btaiye: "))
    STORY1 = story1.replace("_", "%s")
    STORY2 = story2.replace("_", "%s")
    STORY3 = story3.replace("_", "%s")
    print STORY1 % (name, insect, food)
    print STORY2 % (name, animal, animal2, adjective)
    print STORY3 % (animal2, animal, animal2, name)
