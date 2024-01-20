from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO.1: Print report
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
#Warunek do wylaczania maszyny
machine_on = True
#Obiekt klasy Menu()
order_name = Menu()
#Tworzenie obiektu dla klas CoffeeMaker i MoneyMachine
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while machine_on:
    # Options - wybór kawy spośród dostepnych opcji(metoda get.items())
    options = input(f'What would you like: {order_name.get_items()} ?\n')
    if options == "off":
        machine_on = False
    elif options == "report":
        # Drukowanie raportów dla ilosci hajsu i zasobow z obu klas powyzej
        coffee_maker.report()
        money_machine.report()
    else:
        # Find drink to nazwa Twojego zamówienia, Twojej kawusi
        find_drink = order_name.find_drink(options)


# TODO.2: Check resources sufficient
    #Tworzenie obiektu dla zasobow konkretnej kawusi ktora zostala wybrana z find_drink
    sufficient_drink = coffee_maker.is_resource_sufficient(find_drink)

# TODO.3: Process coins
    if sufficient_drink:
        # TODO.4: Check transaction succesful ?
        if money_machine.make_payment(find_drink.cost):
            # TODO.5: Make coffee
            coffee_maker.make_coffee(find_drink)
