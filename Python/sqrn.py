while True:
    n = input("Pleae enter a positive number (0 to exit): ")
    n = int(n)
    if n<0:
        print("Only positive number allowed. Please try again.")
        continue
    if n == 0:
        break
    print("Square of", n, "is", n*n)