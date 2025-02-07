# BOOLEANS
# """

verdadero = True
falso = False
Verdadero = True
autentico = True
print(id(verdadero))
print(id(Verdadero))
print(id(autentico))

print (verdadero == autentico)
print (verdadero is Verdadero)

# # Algunos valores tienen asignado False
# # 0 -> el número 0
# # "" -> string vacío
# # [] -> lista vacía

print(bool(0))

if 0:
    print("El 0 es verdadero")
else:
    print("El 0 es falso")

if []:
    print("La lista está vacía")
    

