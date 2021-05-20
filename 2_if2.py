def main():
    line1 = input("Введите строку ")
    line2 = input("Введите строку ")
    if type(line1) != str or type(line2) != str:
        print(0)
    if line1 == line2:
        print(1)
    elif len(line1)>len(line2):
        print(2)
    elif line2 == "learn":
        print(3)
if __name__ == "__main__":
    main()








    

