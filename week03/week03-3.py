def duplicate_city(cities):
    result_city = list()
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)

        if l1 == l2:
            result_city.append(city)
    return  result_city

cities = ["Suwon", "Hwasung", "Incheon", "Bucheon", "Incheon", "Seoul"]

cities.append("Seoul")     # 추가 X
cities.append("Busan")     # 추가 O

print(cities)
print(duplicate_city(cities))

# 출력결과 
# ['Suwon', 'Hwasung', 'Incheon', 'Bucheon', 'Incheon', 'Seoul', 'Seoul', 'Busan']
# ['Incheon', 'Seoul']
