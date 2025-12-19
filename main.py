from transport.vehicle import vehicle
from transport.transportcompany import TransportCompany 
from transport.truck import truck
from transport.ship import ship
from transport.client import client

company = TransportCompany()

while True:
    
    print("\n === TRANSPORT COMPANY === ")
    print("1 - Добавить транспорта")
    print("2 - Добавить клиента")
    print("3 - Вывести список всех клиентов")
    print("4 - Вывести список всего транспорта")
    print("5 - Распределить грузы")
    print("6 - Выйти из программы")
    try:
        user_choose = int(input("Выберите действие (1-6): "))
    except ValueError:
        print("Ошибка! Введите число от 1 до 6")
        continue

    print(" ")

    if user_choose == 1:
        user_transport = int(input("Корабль(1) или авто(2)?: "))

        if user_transport == 1:
            new_vehicle = ship()

        elif user_transport == 2:
            new_vehicle = truck()

        else:
            new_vehicle = vehicle()
        company.add_vehicle(new_vehicle)

    if user_choose == 2:
        new_client = client()
        company.add_client(new_client)

    if user_choose == 3:
        for client in company.clients:
            print(client)

    if user_choose == 4:
        for vehicle in company.vehicles:
            print(vehicle)

    if user_choose == 5:
        company.optimize_cargo_distribution()

    if user_choose == 6:
        print("все данные сохранены в файл data.json.")
        break