n=int(input("\n Digite el numero: "))
n_pares= 0
n_impares=0

while n!=0:
    
    if n%2==0:
        n_pares=n_pares+1
    else: 
        n_impares=n_impares+1
    n=int(input("\n Digite el numero: "))

    
print("la cantidad de numeros impares es: " + str(n_impares) + (" y la cantidad de numeros pares es: " + str(n_pares)))

 