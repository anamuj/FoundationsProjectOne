####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "not muffins"
signature_flavors = ["not vanilla", "not chocolate", "not strawberry"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
   
    for key,value in menu.items():
        print (key,value)



def print_originals():
    """
    Print the original flavor cupcakes.
    """

    print("Our original flavor cupcakes (KD %s each):" % original_price)  # I dont understand how this is written with the brackets
    # your code goes here!
    for original in original_flavors:
        print (original)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for signature in signature_flavors:
        print (signature)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in signature_flavors:
        return True
    elif order in original_flavors:
        return True
    elif order in menu:
        return True
    else:
        return False


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    user_input = input("What would you like to order? Or type exit to checkout \n")

    while user_input.lower()!= "exit":
        
        if is_valid_order(user_input)== True:
            order_list.append(user_input)
            print ("[%s] has been added to your order \n" % user_input )
            user_input=input("Anything else? \n")
        else:
            print ("She doesn't even go here")
            user_input=input("Please enter a flavor on the menu \n" )

    

    return order_list

def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        print ("We can take credit card")
    else:
        print ("cash only")


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for order in order_list:
        if order in original_flavors:
            total += 2
        elif order in signature_flavors:
            total += 2.75
        elif order in menu:
            total += menu[order]

    return total 

        # for original_flavor in original_flavors:
        #     if order == original_flavor
        #     total += 2
        # for signature_flavor in signature_flavors:
        #     if order == signature_flavor:
        #         total += 2.



def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    totalprice = get_total_price(order_list)

    print ("Your order is %s" %order_list)
    print ("%0.3f KWD" %totalprice)

    print 