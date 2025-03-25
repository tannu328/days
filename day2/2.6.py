#A fruit juice company tags their fruit juices by concatenating the first three letters of the words in a flavor's name, with its capacity.Create a Program that creates product IDs for different fruit juices.

def product_id(flavor, capacity):
    words = flavor.split()


    product_id = "".join([word[:3].lower() for word in words])

    product_id += str(capacity)

    return product_id


flavor = input("Enter the flavor of the fruit juice: ")
capacity = int(input("Enter the capacity of the juice in milliliters: "))


product_id = product_id(flavor, capacity)
print(f"The product ID for {flavor} with {capacity}ml capacity is: {product_id}")
