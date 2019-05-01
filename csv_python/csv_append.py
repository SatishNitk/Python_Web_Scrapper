def print_cities(title):
    print title.center(40,'*')
    with open('cities.csv') as citylist:
        print 'Cities:\n',citylist.read()
def add_city(city_info):
    with open('cities.csv','a') as citylist:
        citylist.write('%s, %i, %i\n' % city_info)
print_cities('Before')
new_city = ('Espoio', 123, 212)
add_city(new_city)
print_cities('After')
