
class Koira:
    #kontstruktori eli mitä tapahtuu kun luo uuden
    count = 0
    def __init__(self, name, weight):
        print(f"uusi koiraolio ({name}) luotu")
        self.name = name
        self.weight = weight
        Koira.count += 1
    # luokan toiminto eli eli metodi
    def hauku(self, toWho, times):
        print(f"{self.name} haukkuu {toWho}")
        for i in range(times):
            if self.weight < 10:
                print("Wufwuf!")
            else:
                print("Hauhau!")
koira1 = Koira("Rekku", 20)
koira1.hauku("jaskalle", 2)
koira2 = Koira("Ruffe", 8)
koira2.hauku("jaskalle",2)
print(f"koiraolioita on luotu yhteensä {Koira.count}kpl")
#koira1.name = "Rekku"
#koira2.name = "ruffe"
print(koira1.name)
print(koira2.name)
