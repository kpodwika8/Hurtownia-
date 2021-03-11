import pymysql
import time

def k_logowanie(login, haslo):
    connection = pymysql.connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()
    import pymysql

    # 1 WYPISANIE PRODUKTOW W ZALEZNOSCI OD CENY
    def wypisanie_produktow():
        connection = pymysql.connect(
            host='localhost',
            user="root",
            password="",
            db="hurtownia2",
        )
        cur = connection.cursor()
        cur.execute(
            "SELECT produkt.nazwa_produktu, cena.cena FROM produkt INNER JOIN cena ON cena.id_cena = produkt.id_cena ORDER BY cena.cena DESC;")
        i = 1
        for row in cur.fetchall():
            print("Pozycja: ", i, " ", row[0], "|", row[1])
            i += 1

        connection.close()

    # 4 ZAKTUALIZOWANIE CENY
    def aktualizacja_ceny(nazwa):
        connection = pymysql.Connect(
            host='localhost',
            user="root",
            password="",
            db="hurtownia2",
        )

        cur = connection.cursor()

        sql = "UPDATE cena SET cena.cena = cena.cena* 0.5 WHERE id_cena = (SELECT id_cena FROM produkt WHERE nazwa_produktu LIKE %s);"

        cur.execute(sql, nazwa)
        connection.commit()
        connection.close()

    # 5 USUNIECIE PRODUKTU
    def usuniecie_produktu(nazwa):
        connection = pymysql.Connect(
            host='localhost',
            user="root",
            password="",
            db="hurtownia2",
        )

        cur = connection.cursor()

        sql = "DELETE FROM produkt WHERE nazwa_produktu LIKE %s;"

        cur.execute(sql, nazwa)
        connection.commit()
        connection.close()

    # 11 WYPISANIE PRODUKTU PO NAZWIE
    def nazwa_produkt(nazwa):
        connection = pymysql.connect(
            host='localhost',
            user="root",
            password="",
            db="hurtownia2",
        )
        cur = connection.cursor()

        sql = "SELECT produkt.nazwa_produktu, cena.cena FROM produkt INNER JOIN cena ON produkt.id_cena = cena.id_cena WHERE nazwa_produktu LIKE %s;"

        cur.execute(sql, nazwa)
        for row in cur.fetchall():
            print(row[0], "|", row[1])

        connection.close()

    sql = "SELECT klient.k_login FROM klient WHERE k_login LIKE %s;"
    sql1= "SELECT klient.k_haslo FROM klient WHERE k_haslo LIKE %s;"

    if (cur.execute(sql, login) ) and (cur.execute(sql1,haslo)) ==1:
        print("logowanie pomyslne")
    else:
        print("logowanie nie udało się")
    connection.close()

def p_logowanie(login, haslo):
    connection = pymysql.connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()

    sql = "SELECT pracownik.p_login FROM pracownik WHERE p_login LIKE %s;"
    sql1= "SELECT pracownik.p_haslo FROM pracownik WHERE p_haslo LIKE %s;"

    if (cur.execute(sql, login) ) and (cur.execute(sql1,haslo)) == 1:
        print("logowanie pomyslne")
    else:
        print("logowanie nie udało się")
    connection.close()


# 1 WYPISANIE PRODUKTOW W ZALEZNOSCI OD CENY
def wypisanie_produktow():
    connection = pymysql.connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )
    cur = connection.cursor()
    cur.execute(
        "SELECT produkt.nazwa_produktu, cena.cena FROM produkt INNER JOIN cena ON cena.id_cena = produkt.id_cena ORDER BY cena.cena DESC;")
    i = 1
    for row in cur.fetchall():
        print("Pozycja: ", i, " ", row[0], "|", row[1])
        i += 1

    connection.close()


# 4 ZAKTUALIZOWANIE CENY
def aktualizacja_ceny(nazwa):
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()

    sql = "UPDATE cena SET cena.cena = cena.cena* 0.5 WHERE id_cena = (SELECT id_cena FROM produkt WHERE nazwa_produktu LIKE %s);"

    cur.execute(sql, nazwa)
    connection.commit()
    connection.close()

#5 USUNIECIE PRODUKTU
def usuniecie_produktu(nazwa):
    connection = pymysql.Connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )

    cur = connection.cursor()

    sql = "DELETE FROM produkt WHERE nazwa_produktu LIKE %s;"

    cur.execute(sql, nazwa)
    connection.commit()
    connection.close()

#10 WYPISANIE PRACOWNIKOW
def wypisanie_pracownikow():
    connection = pymysql.connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )
    cur = connection.cursor()
    cur.execute(
        "SELECT stanowisko.stanowisko, pracownik.imie, pracownik.nazwisko FROM pracownik INNER JOIN stanowisko ON pracownik.id_stanowisko = stanowisko.id_stanowisko ORDER BY stanowisko.stanowisko DESC;")
    i = 1
    for row in cur.fetchall():
        print("Pracownik", i, " ", row[0], "|", row[1], "|", row[2])
        i += 1

    connection.close()


# 11 WYPISANIE PRODUKTU PO NAZWIE
def nazwa_produkt(nazwa):
    connection = pymysql.connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )
    cur = connection.cursor()

    sql = "SELECT produkt.nazwa_produktu, cena.cena FROM produkt INNER JOIN cena ON produkt.id_cena = cena.id_cena WHERE nazwa_produktu LIKE %s;"

    cur.execute(sql, nazwa)
    for row in cur.fetchall():
        print(row[0], "|", row[1])

    connection.close()


# 12 WYPISANIE WSZYSTKICH PRODUKTOW WRAZ Z ICH ILOSCIĄ
def wszystkie_produkty():
    connection = pymysql.connect(
        host='localhost',
        user="root",
        password="",
        db="hurtownia2",
    )
    cur = connection.cursor()

    cur.execute("SELECT nazwa_produktu, ilosc_produktow FROM produkt;")
    i = 1
    for row in cur.fetchall():
        print("Pozycja", i, " ", row[0], "|", row[1])
        i += 1

        connection.close()


import datetime

x = datetime.datetime.now()

print(x.strftime("%A"))