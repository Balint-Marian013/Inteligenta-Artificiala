#
# #EX1
# BRAD = [
# [0,0,0,1,0,0,0],
# [0,0,1,1,1,0,0],
# [0,1,1,1,1,1,0],
# [1,1,1,1,1,1,1],
# [0,0,0,1,0,0,0],
# [0,0,0,1,0,0,0]]
#
# for rand in BRAD:
#     for steluta in rand:
#         if steluta == 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#
# #EX2
#
# import random
#
# nota = random.randint(0, 10)
#
# print("Nota generată este:", nota)
#
# if nota >= 9:
#     print("Excelent")
# elif nota >= 7:
#     print("Bine")
# elif nota >= 5:
#     print("Suficient")
# else:
#     print("Reexaminare")
#
# #EX3
#
# numar_secret = 8
# incercari = 0
#
# while True:
#     ghicire = int(input("Ghicește numărul (1-50): "))
#     incercari += 1
#
#     if ghicire < numar_secret:
#         print("Numărul este mai mare!")
#     elif ghicire > numar_secret:
#         print("Numărul este mai mic!")
#     else:
#         print(f"Felicitări! Ai ghicit numărul în {incercari} încercări.")
#         break
#
        #Ex4
orase = ["București", "Cluj-Napoca", "Timișoara", "Iași", "Constanța"]

for index, oras in enumerate(orase, start=1):
  # print(f"{index}. {oras}")

    #EX5

  # import random
  # numere = []
  # for i in range(6):
  #     numar = int(input(f"Numărul {i + 1}: "))
  #     numere.append(numar)
  # extrase = random.sample(range(1, 50), 6)
  #
  # ghicite = []
  # for n in numere:
  #     if n in extrase:
  #         ghicite.append(n)
  # print("Numere extrase:", extrase)
  # print("Ai ghicit:", ghicite)
  # print("Numere ghicite:", len(ghicite))
  # if len(ghicite) >= 3:
  #
  #     print("Felicitări! Ai câștigat un premiu mic!")
  # else:
  #     print("Mai încearcă, noroc data viitoare!")
  #
  # print("Numere extrase:", extrase)
  # print("Ai ghicit:", ghicite)
  # print("Numere ghicite:", len(ghicite))

  # import random
  #
  # print("Bine ai venit în pădurea magică!")
  # print("Pregătește-te pentru o aventură plină de surprize!")
  #
  # inventar = []
  #
  # # Prima alegere
  # alegere1 = input("Vrei să mergi la stânga sau la dreapta? ").lower()
  #
  # if alegere1 == "stânga":
  #     print("Mergi pe poteca din stânga și vezi un lup! Trebuie să fugi repede.")
  # elif alegere1 == "dreapta":
  #     print("Mergi pe poteca din dreapta și găsești o comoară strălucitoare!")
  #     inventar.append("comoară")
  # else:
  #     print("Nu ai ales o direcție corectă și te rătăcești puțin.")
  #
  # # A doua alegere
  # alegere2 = input("Vrei să continui înainte sau să te întorci? ").lower()
  #
  # if alegere2 == "înainte" or alegere2 == "inainte":
  #     evenimente = ["un râu misterios", "un copac vorbitor", "un iepure magic", "un pod vechi"]
  #     descoperire = random.choice(evenimente)
  #     print(f"Mergi mai departe și întâlnești {descoperire}!")
  #     if descoperire == "un iepure magic":
  #         inventar.append("iepure magic")
  #     elif descoperire == "un pod vechi":
  #         print("Podul scârțâie, dar reușești să treci și găsești o piatră magică.")
  #         inventar.append("piatră magică")
  # elif alegere2 == "întoarce" or alegere2 == "intoarce":
  #     print("Te întorci și găsești un mic cufăr cu aur!")
  #     inventar.append("aur")
  # else:
  #     print("Nu ai ales corect și te plimbi fără scop.")
  #
  # # A treia alegere
  # alegere3 = input("Vrei să explorezi o peșteră sau să urci pe deal? ").lower()
  #
  # if alegere3 == "peșteră" or alegere3 == "pestera":
  #     print("Intrând în peșteră, găsești o lampă fermecată!")
  #     inventar.append("lampă fermecată")
  #     print("Dar un șarpe magic apare și trebuie să fugi.")
  # elif alegere3 == "deal":
  #     print("Urcând pe deal, vezi o panoramă minunată și un copac cu fructe aurii!")
  #     inventar.append("fructe aurii")
  # else:
  #     print("Nu ai ales corect și pierzi timp prețios.")
  #
  # # A patra alegere
  # alegere4 = input("Vrei să te apropii de un lac sau să mergi prin pădurea densă? ").lower()
  #
  # if alegere4 == "lac":
  #     print("La lac găsești un peștișor strălucitor care îți aduce noroc!")
  #     inventar.append("peștișor norocos")
  # elif alegere4 == "pădure" or alegere4 == "padure":
  #     print("În pădure întâlnești o bufniță înțeleaptă care îți dă o baghetă magică.")
  #     inventar.append("baghetă magică")
  # else:
  #     print("Nu ai ales corect și te pierzi în pădure.")
  #
  # # Finalul aventurii
  # print("\nAventura ta s-a terminat!")
  # if inventar:
  #     print("Obiecte găsite în inventar:", inventar)
  # else:
  #     print("Nu ai găsit niciun obiect, dar ai supraviețuit aventurii!")


  cuvinte_pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
  cuvinte_negative = ["urât", "prost", "groaznic", "dezamăgitor"]

  # Introducem comentariul utilizatorului
  comentariu = input("cuvantul este : ").lower()


  pozitiv = any(cuv in comentariu for cuv in cuvinte_pozitive)
  negativ = any(cuv in comentariu for cuv in cuvinte_negative)


  if pozitiv:
      print("Comentariu pozitiv!")
  elif negativ:
      print("Comentariu negativ!")
  else:
      print("Comentariu neutru.")