#Napiši program, ki izpiše prvih 200 praštevil.

def Prvih_n_praštevil(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for x in range(2, 201):
    if Prvih_n_praštevil(x):
        print(x)