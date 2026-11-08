def tulosta_varastot(mehu, olut):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehu}")
    print(f"Olutvarasto: {olut}")

    print("Olut getterit:")
    print(f"saldo = {olut.saldo}")
    print(f"tilavuus = {olut.tilavuus}")
    print(f"paljonko_mahtuu = {olut.paljonko_mahtuu()}")


def testaa_mehu(mehu):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehu.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehu}")

    print("Otetaan 3.14")
    mehu.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehu}")


def testaa_virhetilanteet():
    print("Virhetilanteita:")

    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def testaa_lisaaminen(mehu, olut):
    print(f"Olutvarasto: {olut}")
    print("olutta.lisaa_varastoon(1000.0)")
    olut.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olut}")

    print(f"Mehuvarasto: {mehu}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehu.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehu}")


def testaa_ottaminen(mehu, olut):
    print(f"Olutvarasto: {olut}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olut.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olut}")

    print(f"Mehuvarasto: {mehu}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehu.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehu}")


def main():
    mehu = Varasto(100.0)
    olut = Varasto(100.0, 20.2)

    tulosta_varastot(mehu, olut)
    testaa_mehu(mehu)
    testaa_virhetilanteet()
    testaa_lisaaminen(mehu, olut)
    testaa_ottaminen(mehu, olut)


if __name__ == "__main__":
    main()
