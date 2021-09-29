

def display_cities(first, second):
    '''
    Displays the two cities on a single line.
    '''

    print(f'{first} -> {second}')


cities = ['Mexico City, Mexico', 'Pheonix, AZ', 'Newport, CA']
cities.append('Paris, France')
cities.append('Tokyo, Japan')

# prints the list
# print(cities)

# for i in range(len(cities)):
#     print(f'{i + 1}. {cities[i]}')

# print(f'{cities[0]} -> {cities[1]}')
# print(f'{cities[1]} -> {cities[2]}')

display_cities(cities[0], cities[1])
display_cities(cities[1], cities[2])
