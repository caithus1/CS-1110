# Christopher Geier (cpg3rb)
def primes(x):
    prime_list = [2]
    prim = 3
    while prim < x:
        for i in range(0,len(prime_list)):
            if prim % prime_list[i] == 0:
                break
            if i == len(prime_list)-1:
                prime_list.append(prim)
        prim += 2
    return prime_list
