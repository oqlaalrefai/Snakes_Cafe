from typing import Counter


print ('************************************** \n **    Welcome to the Snakes Cafe!   ** \n **    Please see our menu below.    ** \n ** \n ** To quit at any time, type "quit" ** \n **************************************')

Appetizers = ['Wings', 'Cookies', 'Spring Rolls']
print('\n Appetizers \n ---------- \n Wings \n Cookies \n Spring Rolls \n')

Entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
print('\n Entrees \n ------- \n Salmon \n Steak \n Meat Tornado \n A Literal Garden')

Desserts = ['Ice Cream', 'Cake', 'Pie']
print('\n Desserts \n -------- \n Ice Cream \n Cake \n Pie \n')

Drinks = ['Coffee','Tea','Unicorn Tears']
print('\n Drinks \n ------- \n Coffee \n Tea \n Unicorn Tears \n')
print('***********************************')
print('** What would you like to order? **')
print('***********************************')




def order_fun():
    
    x = True
    orders =[]
    while x== True:
        customer_input = input('>')

        if customer_input != 'quit':
            orders.append(customer_input)
            counter = orders.count(customer_input)
            print(f'** {counter} orders of {customer_input} have been added to your meal **')
        else :
            print(orders)
            x = False
order_fun()
