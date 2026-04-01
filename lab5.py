# # importing functools for reduce()
# import functools

# # initializing list
# lis = [1, 3, 5, 6, 2]

# # using reduce to compute sum of list
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(lambda a, b: a + b, lis))

# # using reduce to compute maximum element from list
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))


# n=input('introduceti un numar')

# def fib(n):
#     if n<=0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
    
 # print(fib(int(n)))

# EX3
# while True:
#     j1 = input("Jucatorul 1 (piatra/hartie/foarfeca): ")
#     j2 = input("Jucatorul 2 (piatra/hartie/foarfeca): ")

#     if j1 == j2:
#         print("Egalitate!")
#     elif (j1 == "piatra" and j2 == "foarfeca") or \
#          (j1 == "foarfeca" and j2 == "hartie") or \
#          (j1 == "hartie" and j2 == "piatra"):
#         print("Jucatorul 1 a castigat!")
#     else:
#         print("Jucatorul 2 a castigat!")

#     again = input("Doriti sa mai jucati? (da/nu): ")
#     if again != "da":
#         break

my_list = [1, 2, 3]

rezultat = list(map(lambda x: x**2, my_list))

print(rezultat)

def genereaza_factura(nume_client, **kwargs):
    print("===== FACTURA =====")
    print("Client:", nume_client)
    
    total = 0
    
    for produs, pret in kwargs.items():
        print(f"{produs} - {pret} lei")
        total += pret
    
    print("-------------------")
    print("Total de plata:", total, "lei")

genereaza_factura(
    "Ion Popescu",
    paine=13,
    lapte=7,
    oua=22,
)


a = [(0, 2), (4, 3), (9, 9), (10, -1)]

sorted_a = sorted(a, key=lambda x: x[1])

print(sorted_a)


preturi_produse=[1000,None,500,23,None]
fara_none = list(filter(lambda x: x is not None, preturi_produse))

reduse = list(map(lambda x: x * 0.99, fara_none))

print(reduse)