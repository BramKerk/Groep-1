from tkinter.filedialog import askopenfilename

def main():
    aantal_organismen = int(input("Hoeveel organismen wil je bekijken? "))
    print("Je hebt gekozen om ", aantal_organismen, "organismen te bekijken.")
    bestandinhoud, bestanddingetje = bestandkiezer(aantal_organismen)
    soort_seq = soort_sequentie(bestandinhoud, aantal_organismen)
    GCPRC = GCpercentage(bestandinhoud, aantal_organismen, soort_seq)
    PRT_gewicht = gewicht_teller(bestandinhoud, aantal_organismen, soort_seq)
    percentage_ID = percentage_identity(aantal_organismen, bestandinhoud, bestanddingetje)



def bestandkiezer(aantal_organismen):
    bestandinhoud_lijst = []
    leeg = ""
    for n in range (aantal_organismen):
        bestandpath = askopenfilename()
        bestanddingetje = open(bestandpath,"r")
        for regel in bestanddingetje:
            if not regel.startswith(">"):
                bestand =leeg + regel
                bestandinhoud_lijst.append(bestand)
        bestandinhoud_lijst.append("bestandsplitser")
    return bestandinhoud_lijst, bestanddingetje

def soort_sequentie(bestandinhoud, aantal_organismen):
    A = 0
    C = 0
    G = 0
    T = 0
    D = 0
    E = 0
    R = 0
    K = 0
    length = 0
    for n in range(aantal_organismen):
        for line in bestandinhoud:
            if not line.startswith(">"):
                line.replace("\n", "")
                A = A + line.count("A")
                C = C + line.count("C")
                G = G + line.count("G")
                T = T + line.count("T")
                D = D + line.count("D")
                E = E + line.count("E")
                R = R + line.count("R")
                K = K + line.count("K")
                length = length + len(line) - 1

        CGAT = C + G + A + T
        CGATDERK = C + G + A + T + D + E + R + K
        print("C+G+A+T = ", CGAT)
        print("C+G+A+T+D+E+R+K = ", CGATDERK)

        if CGAT == CGATDERK:
            is_XNA = True
            print("Dit is DNA of RNA")
        else:
            is_XNA = False
            print("Dit is een eiwit")
        return is_XNA


def GCpercentage(bestandinhoud,aantal_organismen, is_XNA):
    if aantal_organismen == 1 and is_XNA == True:
        for n in range(aantal_organismen):
            c = 0
            g = 0
            a = 0
            t = 0
            for regel in bestandinhoud:
                    c = c + regel.count("C")
                    g = g + regel.count("G")
                    a = a + regel.count("A")
                    t = t + regel.count("T")
            print("Het aantal C is ", c)
            print("Het aantal G is ", g)
            print("De totale lengte is ", c+g+a+t)
            kip = (g + c) / (g+c+a+t) *100


            print ("Het GC% is", kip)
            return kip
    else:
        print("Dit is geen DNA of RNA of er zijn meer dan een sequenties, dus het CG% wordt niet berekend.")

def gewicht_teller(bestandinhoud, aantal_organismen, is_XNA):
    leeg = ""
    if aantal_organismen == 1 and is_XNA == False:
        for tekst in bestandinhoud:
            if not tekst.startswith(">"):
                leeg = tekst + leeg
            A = leeg.count("A") * 89
            R = leeg.count("R") * 174
            N = leeg.count("N") * 132
            D = leeg.count("D") * 133
            C = leeg.count("C") * 121
            E = leeg.count("E") * 146
            Q = leeg.count("Q") * 147
            G = leeg.count("G") * 75
            H = leeg.count("H") * 155
            I = leeg.count("I") * 131
            L = leeg.count("L") * 131
            K = leeg.count("K") * 146
            M = leeg.count("M") * 149
            F = leeg.count("F") * 165
            P = leeg.count("P") * 115
            S = leeg.count("S") * 105
            T = leeg.count("T") * 119
            W = leeg.count("W") * 204
            Y = leeg.count("Y") * 181
            V = leeg.count("V") * 117
        bestandinhoud_slecht = leeg.replace("\n", "")
        bestandinhoud_goed = bestandinhoud_slecht.replace("bestandsplitser", "")
        gewicht = (A+R+N+D+C+E+Q+G+H+I+L+K+M+F+P+S+T+W+V+Y)
        water = len(bestandinhoud_goed)
        water = water * 18
        water = water - 18
        goed_gewicht = gewicht - water
        print("Het eiwit in Eno1 fase weegt" , goed_gewicht, "DA")
def percentage_identity(aantal_organismen, bestandinhoud, bestanddingetje):
    if aantal_organismen == 2:
        #Lege variabelen voor het tellen
        Total1 = ""
        Total2 = ""
        teller = 0
        bestand = ""
        leger = ""

        #Filteren van bestanden
        keep_going = True
        while keep_going == True:
            for regel in bestandinhoud:
                bestand = regel + bestand
                if regel != "bestandsplitser":
                    keep_going = True
                elif regel == "bestandsplitser":
                    keep_going = False
                    bestand1 = bestand
                    print(bestand1)
                

##        i = 0
##        while i == 0:
##            for regel in bestandinhoud:
##                bestand = regel + bestand
##            print(bestand)
##            bestand1, bestand2 = bestand.split("bestandsplitser")
            
        
        for tekst1 in bestand1:
            if not tekst1.startswith(">"):
                Total1 += tekst1

        for tekst2 in bestand2:
            if not tekst2.startswith(">"):
                Total2 += tekst2

        #Dit stuk zorgt dat het kleinste bestand in een vaste variabele gaat zitten (Total1a)
        Total1a = ""
        Total2a = ""
        if len(Total1) < len(Total2):
            print("Het organisme met de grootse sequentie is ", organisme)
            Total1a = Total1
            Total2a = Total2
        elif len(Total1) > len(Total2):
            print("Het organisme met de grooste sequentie is ", organisme2)
            Total1a = Total2
            Total2a = Total1
        #Hier laat ik hem de verschillen tellen.
        def Differences(Total1a, Total2a):
            difference = 0
            print("De totale lengte van het grootste organisme is ", len(Total2a))
            print("De totale lengte van het kleinste organisme is ", len(Total1a))
            for i in range(len(Total1a)):
                if Total2a[i] != Total1a[i]:
                    difference += 1
            print(difference, "Gelijken")
            return difference

        Verschil = Differences(Total1a, Total2a)
        print(Verschil)
        #En hier berekent hij het percentage.
        percentage = (Verschil / len(Total2a)) * 100
        print("Het percentage identity bij de twee gekozen sequenties is ", percentage)
        
        
main()
