# Task 4, 5, 6

import collections

# склады: основной склад и склады подразделений

 class Warehouse():
     def __init__( self, name ):
         self.name = name = name
         self.items = []

     def __str__(self):
         strres = f'Состояние склада "{self.name}":\n'
         if self.items:
             for i, item in enumerate(self.items):
                 strres += f"{i}: {item}\n"
         else:
             strres += 'пусто!\n'
         return strres

     # оприходовать оборудование на склад warehouse
     def debit( self, equipment ):
         self.items.append( equipment )

     # "списать" оборудование со склада
     def _credit( self, equipment ):
         if not equipment in self.items:
             raise KeyError( equipment )
         self.items.remove( equipment )
         # # найдём нужное нам оборудование: того же производителя и модели и спишем
         # for item in self.items:
         #     if item.shortname() == equipment.shortname():

     # оприходовать оборудование на склад warehouse
     def moveto( self, equipment, another_warehouse ):
         self._credit( equipment )
         another_warehouse.debit( equipment )

 # --> я буду только контролировать цену и вес оборудования при создании объекта Equipment
 class Equipment():
     def __init__( self, brandname, model, price, weight ):
         if not ( (type(price) is int or type(price) is float) and price > 0 ):
             raise ValueError('price should be positive number')
         if not ( (type(weight) is int or type(weight) is float) and weight > 0 ):
             raise ValueError('weight should be positive number')

         self.brandname = brandname
         self.model = model
         self.price = price
         self.weight = weight

     def __str__(self):
         return f'{self.itemname} {self.model} ценою {str(self.price)} ₽ и весом {str(self.weight)} кг.'

     # краткое наименование
     def shortname(self):
         return f'{self.itemname} {self.model}'

 class Printer(Equipment):
     itemname = 'Принтер'

 class Scanner(Equipment):
     itemname = 'Сканер'

 class Xerox(Equipment):
     itemname = 'Ксерокс'


 e1 = Printer( 'LG', 'pocket photo pd239', 12340, 2.54 )
 print( e1 )

 e2 = Scanner( 'LG', 'fu667d', 4625, 4.533 )
 print( e2 )

 e3 = Xerox( 'Xerox', 'SXD5', 45632, 12.46 )
 print( e3 )

 warehouse_main = Warehouse( 'main' )
 warehouse_moscow = Warehouse( 'MoscowCityOffice' )
 warehouse_samara = Warehouse( 'SamaraOffice' )

 warehouse_main.debit( e1 )
 warehouse_main.debit( e2 )
 warehouse_main.debit( e3 )

 print(warehouse_main)

 warehouse_main.moveto( e1, warehouse_moscow )

 print(warehouse_main)

 warehouse_main.moveto( e2, warehouse_moscow )

 print(warehouse_main)

 warehouse_main.moveto( e3, warehouse_samara )

 print(warehouse_main)

 try:
     warehouse_main.moveto( e1, warehouse_samara )
 except KeyError as e:
     print('оборудование не найдено и не может быть списано')

 print(warehouse_main)

 try:
     e4 = Xerox( 'Xerox', 'SXD55', -45632, -12.46 )
     print( e4 )
 except ValueError as e:
     print(e)

print("That's all, folks!")
