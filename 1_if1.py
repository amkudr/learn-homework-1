def main():
    age = int(input("Введите ваш возраст "))
    def selection(age):
        if age < 0:
            raise ValueError("Введите корректный возраст")
        if age < 7:
            return("Вы в детском саду")
        if age < 19:
            return("Вы в школе")
        if age < 24:
            return("Вы в ВУЗе")
        if age <66:
            return("Вы работаете")
        else:
            return("Вы на пенсии или умерли")
    escape = selection(age)
    print(escape)
if __name__ == "__main__":
    main()

    


