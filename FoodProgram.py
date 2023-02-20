# Author:     Shepard Berry
# Class:      MIS-4322
# Assignment: Classes and OOP
# Due:        2/20/2023



import FoodClass as fc
# this dictionary represents transactions. The key of the dictionary is the 
# transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]
dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}
order_total = 0


# Danni Sellyar
#customer = fc.Customer(customerid=570, name="Danni Sellyar", address="97 Mitchell Way Hewitt Texas 76712", email="sellyarft@gmpg.org", phone="254-555-9362", member_status=False)

# Aubree Himsworth
customer = fc.Customer(customerid=569, name="Aubree Himsworth", address="1172 Moulton Hill Waco Texas 76710", email="ahimsworthfs@list-manage.com", phone="254-555-2273", member_status=True)

print(f'Customer Name: {customer.get_name()}')
print(f'Phone: {customer.get_phone()}')

# get order total/print out items
discount = 0.0
for v in dict.values():
    # make sure transaction matches customerid
    if v[3] == customer.get_customerid():
        print(f'Order Item: {v[1]} Price: ${v[2]:,.2f}')
        order_total += v[2]
        if customer.get_member_status():
            discount += v[2] * 0.2

print(f'Total Cost: ${order_total:,.2f}')

# display discount if customer is a member
if customer.get_member_status():
    print(f'Member Discount: ${discount:,.2f}')
    print(f'Total Cost after discount: ${(order_total-discount):,.2f}')


