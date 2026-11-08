heslo = "pepek321"
auth = "657 822"
pokusy_heslo = 3


def zadej_kod():
    pokusy_kod = 3
    while pokusy_kod > 0:
        kod = input("Zadejte autorizační kód: ")
        if kod == auth:
            print("Přístup povolen.")
            return

        pokusy_kod -= 1
        if pokusy_kod > 0:
            print(
                "Přístup zamítnut, zadejte kód znovu. Zbývající počet pokusů:",
                pokusy_kod,
            )

    print("Přístup odepřen, účet byl zablokován.")


while pokusy_heslo > 0:
    zadej_heslo = input("Zadej heslo: ")
    if zadej_heslo == heslo:
        zadej_kod()
        break
    else:
        pokusy_heslo -= 1
        if pokusy_heslo == 0:
            print("Přístup odepřen, opakujte akci.")
            break
        else:
            print("Heslo není správné, zbývající počet pokusů:", pokusy_heslo)
            continue