# Jonathan Sonnek
# Sept 17th 2025
# Shipping Cost


# The Fast Freight Shipping Company charges the following rates:

# Weight    	Price Per Pound
# 2 pounds or less   	$1.50
# Over 2 pounds but not more than 6 pounds  	$3.00
# Over 6 pounds but not more than 10 pounds	$4.00
# Over 10 pounds	$4.75

def weight_conversion(weight):
    # Calculate the shipping charge.
    shippingCost = 0.0

    if weight <= 2:
       shippingCost = 1.5
    elif weight > 2 and weight <= 6:
        shippingCost = 3.0
    elif weight > 6 and weight <= 10:
        shippingCost = 4.0
    else:
        shippingCost = 4.75
    
    return shippingCost

if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))