class Menu:
  def __init__(self, name, items, start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return self.name + ' menu available from: ' + str(self.start_time) + ' to  ' + str(self.end_time)
  
  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items[item]
    return total

class Franchise:
  def __init__(self,address,menus):
     self.address = address
     self.menus = menus
  def __repr__(self):
      return self.address

  def available_menus(self, time):
    retorno = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        retorno.append(menu)
    return retorno

class Business:
  def __init__(self,name, franchises):
    self.name = name
    self.franchises = franchises


brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)

early_dinner_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}


early_dinner = Menu('early_bird', early_dinner_items, 1500, 1800)

dinner_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner_menu = Menu('dinner', dinner_items, 1700, 2300)

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu = Menu('kids', kids_items, 1100, 2100)

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu('arepa', arepas_items, 1000, 2000)

menuss = [kids_menu, dinner_menu, early_dinner, brunch_menu, arepas_menu]


flagship_store = Franchise('1232 West End Road', menuss)

new_installment = Franchise('12 East Mulberry Street', menuss)

arepas_place = Franchise('189 Fitzgerald Avenue', menuss)

new_business = Business('Basta Fazoolin\' with my Heart',[flagship_store, new_installment])

business = Business('Take a\' Arepa', [flagship_store, new_installment, arepas_place])