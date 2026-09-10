# ===================================
# Automatic Bulk Discount Alert
# ===================================
# Developed by. Demas Fadel Anggara
# JCDS - 34


# /************************************/


# /===== Data Model =====/
# Create your data model here

# Example data model
product = [{
    "id_product": 1,
    "product_name": "Air mineral",
    "price": 6500,
    "stock": 150,
    "bulk_threshold": 10,
    "discount": 1-1-2030
}]


# /===== Feature Program =====/
# Create your feature program here
def read():
    """Function for read the data
    """
    print(f"""
          Berikut adalah datamu:
          {product}""")
    return

def create():
    """Function for create the data
    """
    return

def update():
    """Function for update the data
    """
    return

def delete():
    """Function for delete the data
    """
    return

def search():
    """Function for searching the data
    """
    return

def transaction():
    """Function for transaction
    """
    return

def back():
    """Function for go back to the main menu
    """
    return

# /===== Main Program =====/
# Create your main program here
def main():
    """Function for main program
    """
    while True:
        print("=" * 15 + " Automatic Bulk Discount Alert " + "=" * 15)
        print("""
                [1] Create
                [2] Read
                [3] Update
                [4] Delete
                [5] Search
                [6] Exit
                """)    

        input_user = input("Insert your option: ")
        if input_user == "1":
            read()
        elif input_user == "2":
            create()
        elif input_user == "3":
            update()
        elif input_user == "4":
            delete()
        elif input_user == "5":
            search()
        elif input_user == "6":
            break
        else:
            print("Input is not valid !")


if __name__ == "__main__":
    main()