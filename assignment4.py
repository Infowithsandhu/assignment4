# Exercise 3-1: Names
names = ['adnan', 'taoqeer', 'ali', 'irfan']
for name in names:
    print(name)
# Exercise 3-2: Greetings
for name in names:    
    print(f'Hello Mr. {name}, How are you')
# Exercise 3-3: Your Own List    
vehicles = ['Yamaha', 'Honda', 'Tesla', 'MG']
for vehicle in vehicles:
    print(f'I would like to own a:', {vehicle})
# Exercise 3-4: Guest List
list_of_guests = ['adnan', 'taoqeer', 'ali', 'irfan']
for guest in list_of_guests:
    print(f'Hello Mr. {guest}, You are invited to attend my birthday party')
# Exercise 3-5: Changing Guest List
print(f'Unfortunatly Mr. {list_of_guests[0]} cannot atten my birth party')
list_of_guests[0] = 'usama'
for guest in list_of_guests:
    print(f'Hello Mr.{guest}: you are welcome to my birthday party')
# Exercise 3-6: More Guests
print(f'Hello Mr.{list_of_guests}: Here is good news, we found a bigger table, we will invite more friends')
list_of_guests.insert(0, 'shamil das chancher')
list_of_guests.insert(3, 'bindas sharma')
list_of_guests.append('younder brother')
for guest in list_of_guests:
    print(f'Hello Mr.{guest}: you are invited to my birthday party')
# Exercise 3-7: Shrinking Guest List
print(f'Dear {list_of_guests}, you are all informed that recently I found that we have short table and I am inviting only two friends')
while len(list_of_guests) > 2:
    remove_guest = list_of_guests.pop()
    print(f'Sorry Mr. {remove_guest}: you cannot attend my birthday party')
for guest in list_of_guests:
    print(f'Dear {guest}: you are still invited for my birthday')
del list_of_guests[0]
del list_of_guests[0]
print(f'Final guest list: {list_of_guests}')

# Exercise 3-8: Seeing the World
jaga_ka_naam = ['Makka', 'Madina', 'Swizerland', 'New York', 'London']
print('kindly print name in original order:', jaga_ka_naam)
print('kindly sort the name alphabatic order:', sorted(jaga_ka_naam))
print('name again in original order:', jaga_ka_naam)
print('print in reverse order:', sorted(jaga_ka_naam, reverse=True))
print('print again in original order:', jaga_ka_naam)
jaga_ka_naam.reverse()
print('reverse order:', jaga_ka_naam)
jaga_ka_naam.reverse()
print('latest reverse order:', jaga_ka_naam)
jaga_ka_naam.sort()
print('sorted again in alphabatic (permanent):', jaga_ka_naam)
jaga_ka_naam.sort(reverse=True)
print('Reverse alphabatic order (permanent):', jaga_ka_naam)

# Exercise 3-9: Dinner Guests
print(f'I am inviting {len(list_of_guests)} people to my birthday party')

# Exercise 3-10: Every Function
north = ['skardu', 'kumrat', 'kalam', 'taobutt', 'naran']
print('print the name in original order:', north)
north.append('Lahore')
print('print fresh:', north)
north.insert(2, 'islmabad')
print('print fresh:', north)
north.remove('kalam')
print('print fresh:', north)
print('popped item name:', north.pop())
north.sort()
print('print the name in alphabatic:', north)
north.reverse()
print('print name in reverse order:', north)

# Exercise 3-11: Intentional Error
try:
    print(north[7]) 
except IndexError:
    print("IndexError found! please correcting your selection.")

   