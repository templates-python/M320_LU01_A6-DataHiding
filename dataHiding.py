# Dieser Code dient dem Erlebnis der Auswirkungen des data hiding.
# Die Übung basiert auf zwei Klassen, nämlich BankAccountWell und BankAccountUgly.
#
# Mit beiden Klassen wird je eine Einzahlung in auf das Konto sowie 2 Bezüge aus dem Konto
# realisiert.
# Massgebend ist der Unterschied der beiden Klassen in ihrem verhalten.
# Diesen Unterschied zu beschreiben, ist der Sinn der Aufgabe.
class BankAccountWell:
    """
    Diese Klasse stellt ein Bankkonto dar, das korrekt realisiert ist.
    """
    def __init__(self, starting_amount):
        """
        Konstruktor eröffnet das Konto mit einem Startbetrag
        :param starting_amount:
        """
        self.__saldo = starting_amount


    def get_money(self, value):
        """
        Es wird der durch value benannte Betrag vom Bankkonto bezogen.
        Dabei wird sichergestellt, dass der Wert von saldo nicht
        negative wird.
        :param value:
        :return:
        """
        if value < self.__saldo:
            self.__saldo -= value
            return value
        else:
            return 0

    @property
    def saldo(self):
        """
        Liefert den aktuellen Saldo des Kontos
        :return:
        """
        return self.__saldo



class BankAccountUgly:
    """
    Diese Klasse stellt ein Bankkonto dar, das nicht so toll realisiert ist.
    """
    saldo = 0.0

    def __init__(self, starting_amount):
        """
        Konstruktor eröffnet das Konto mit einem Startbetrag
        :param starting_amount:
        """
        self.saldo = starting_amount


if __name__ == "__main__":
    # erstellen eines Bankkontos, das seine Arbeit "well done" erledigt
    account1 = BankAccountWell(1000.0)
    print('vom Bankkonto Nr. 1 mit Saldo ' + str(account1.saldo) + ' wird 300.0 abgehoben')
    money_drawn = account1.get_money(300.0)
    print('neuer Saldo = ' + str(account1.saldo))
    print('vom Bankkonto Nr. 1 mit Saldo ' + str(account1.saldo) + ' wird 900.0 abgehoben')
    money_drawn = account1.get_money(900.0)
    print('neuer Saldo = ' + str(account1.saldo), 'da der Bezug ' + str(money_drawn) + ' liefert')
    print('-----------------------------------------------------------------------------------------')
    # erstellen eines Bankkontos, das seine Arbeit "ugly made" erledigt
    account2= BankAccountUgly(1000)
    print('vom Bankkonto Nr. 2 mit Saldo ' + str(account2.saldo) + ' wird 300.0 abgehoben')
    account2.saldo -= 300
    print('neuer Saldo = ' + str(account2.saldo))
    print('vom Bankkonto Nr. 2 mit Saldo ' + str(account2.saldo) + ' wird 900.0 abgehoben')
    account2.saldo -= 900
    print('neuer Saldo = ' + str(account2.saldo), 'da der Bezug 900.0 liefert')