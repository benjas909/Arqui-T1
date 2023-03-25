def main():

    file = open("numeros.txt")
    regs = 0

    for line in file:
        regs += 2

    print(regs)
    file.close()


if __name__ == "__main__":
    main()
