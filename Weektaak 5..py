#Dit stuk maakt een variabele aan met de inhoud van het bestand
print("Je kunt kiezen uit de volgende organismen: \nGallus gallus\nMus musculus\nPseudomonas syringae\nZea Mays\nSaccharomyces cerevisiae")

organisme = str(input("Wat is de naam van het eerste organisme wat je wilt vergelijken? "))
organisme2 = str(input("Wat is de naam van het tweede organisme wat je wilt vergelijken? "))
bestand1 = open(organisme + " Eno1 protein raar.txt","r")
bestand2 = open(organisme2 + " Eno1 protein raar.txt","r")

#Lege variabelen voor het tellen
Total1 = ""
Total2 = ""
teller = 0

#Filteren van bestanden
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
    print(difference, "verschillen")
    return difference

Verschil = Differences(Total1a, Total2a)
print(Verschil)
#En hier berekent hij het percentage.
percentage = (Verschil / len(Total2a)) * 100
print("Het percentage identity bij de twee gekozen sequenties is ", percentage)
