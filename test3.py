#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import click

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_data(destinations, filename):
    with open(filename, 'w') as file:
        json.dump(destinations, file, indent=4)

@click.command()
@click.option('--add-flight', is_flag=True, help='Add a new flight')
@click.option('--destination', default=None, help='Destination to search flights for')
def main(add_flight, destination):
    filename = 'destinations.json'
    destinations_list = load_data(filename)

    if add_flight:
        add_flight_func(destinations_list)
    elif destination:
        display_flights_by_destination(destinations_list, destination)
    else:
        while True:
            print("\n1. Добавить рейс")
            print("2. Вывести рейсы по пункту назначения")
            print("3. Выйти")
            choice = input("Выберите действие (1/2/3): ")

            if choice == '1':
                add_flight_func(destinations_list)
            elif choice == '2':
                search_destination = input("Введите пункт назначения для поиска: ")
                display_flights_by_destination(destinations_list, search_destination)
            elif choice == '3':
                save_data(destinations_list, filename)
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")

def add_flight_func(destinations):
    destination = input("Введите пункт назначения: ")
    flight_number = input("Введите номер рейса: ")
    plane_type = input("Введите тип самолета: ")

    flight_info = {
        'название пункта назначения': destination,
        'номер рейса': flight_number,
        'тип самолета': plane_type
    }

    destinations.append(flight_info)
    destinations.sort(key=lambda x: x['номер рейса'])
    print("Информация о рейсе добавлена.")

def display_flights_by_destination(destinations, search_destination):
    matching_flights = [
        (flight['номер рейса'], flight['тип самолета'])
        for flight in destinations
        if flight['название пункта назначения'] == search_destination
    ]

    if matching_flights:
        print(f"Рейсы в пункт назначения '{search_destination}':")
        for flight_number, plane_type in matching_flights:
            print(f"Номер рейса: {flight_number}, Тип самолета: {plane_type}")
    else:
        print(f"Рейсов в пункт назначения '{search_destination}' не найдено.")

if __name__ == "__main__":
    main()
