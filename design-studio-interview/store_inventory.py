import csv 

number_of_products= int(input("Enter the number of products: "))
products=[]

for _ in range(number_of_products):
    productName= str(input("Enter the name of the product:"))
    productPrice= float(input(f"Enter the price of  {productName} :"))
    productQuantity= int(input(f"Enter the quantity of {productName} :"))
    totalValue= productPrice*productQuantity
    products.append([productName,productPrice,productQuantity,totalValue])
    
    
csv_file="store_inventory.csv"

with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name","Product Price","Product Quantity","Total Value"])
    writer.writerows(products)
    
print("The data has been written to the file successfully")