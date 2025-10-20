# funktio esimerkki

#funktio joka ei ota patrametria eikä palauta mitään
def say_hello():
    print('moi')
    print('sinä')

#funktio joka ottaa vastaan parametrejä
def say_hello_v2(username):
    print('moi')
    print(username)

say_hello_v2('eeroh')

# summafunktio
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
def my_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    print(total)
    return total
my_sum(numbers)
my_sum([1, 2, 3, 4, 5])

list1 = [1, 2]
list2 = list1
list2.append(3)
print(f'list1: {list1} ja list2: {list2} viittaa samaan listaan koodissa')
# listasta pitää tehdä kopio list.copy()