import string

def main():
    e = int(input("Please enter the exponent value in the public key: "))
    n = int(input("Please enter the n value in the public key: "))

    print(str(e) + " " + str(n))

    # Factorization only works for numbers with one set of
    # factos (other than 1 and the number)
    factorsList = factors(n)
    p = factorsList[1]
    q = factorsList[2]

    nval = (p+1)*(q+1)

    decrypt_e = invModulo(e, nval)

    inputArray = [51, 12, 51, 39, 31, 21, 14, 10, 20, 17, 7, 25, 14, 26, 33, 52, 15, 7,
             27, 51, 7, 49, 8, 15, 51, 7, 8, 25, 7, 25, 10, 49, 18, 52, 51, 7, 8,
             25, 7, 18, 26, 25, 25, 10, 27, 52, 51, 7, 27, 33, 21, 7, 20, 26, 21,
             7, 25, 10, 49, 18, 52, 51, 39]
    alphabet = list(string.ascii_lowercase)
    alphabet.append(' ')

    # print(alphabet)

    for i in inputArray:
        charval = (i**decrypt_e)%n
        print(str(alphabet[charval-2]), end= "")

def invModulo(a, b):
    for num in range(1, b):
        if ((a * num) % b) == 1:
            return num
    return 1

def factors(r):
    listFactors = []

    i = 1
    while i <= r:
        if r % i == 0:
            listFactors.append(i)
        i = i + 1

    return listFactors

if __name__ == "__main__":
    main()

