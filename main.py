# ===================================
# Automatic Bulk Discount Alert
# ===================================
# Developed by. Demas Fadel Anggara
# JCDS - 34


# /************************************/

# Tujuan:
# Untuk membantu owner/kasir membuat event diskon bulanan pada semua minimarket untuk menarik pelanggan

# /===== Data Model =====/
# Create your data model here
# import tabulate
from datetime import datetime


# Example data model
products = [
    {
        "id_product": 1,
        "name_product": "Air Mineral",
        "price_product": 6500,
        "stock_product": 15,
        "category_product": "minuman"
    },
    {
        "id_product": 2,
        "name_product": "Mie Instan",
        "price_product": 3500,
        "stock_product": 20,
        "category_product": "makanan"
    },
    {
        "id_product": 3,
        "name_product": "Roti Tawar",
        "price_product": 5500,
        "stock_product": 10,
        "category_product": "makanan"
    },
    {
        "id_product": 4,
        "name_product": "Sabun Mandi",
        "price_product": 18000,
        "stock_product": 5,
        "category_product": "kosmetik"
    },
    {
        "id_product": 5,
        "name_product": "Susu Murni",
        "price_product": 2500,
        "stock_product": 25,
        "category_product": "minuman"
    },
]

promotions = [
    {
        "id_promotion": 1,
        "name_promotion": "Monthly Sale",
        "type_promotion": "percentage",
        "start_date": "01-09-2026",
        "end_date": "30-09-2026",
        "discount": 10
    },
    {
        "id_promotion": 2,
        "name_promotion": "Weekly Sale",
        "type_promotion": "b2g1",
        "start_date": "21-09-2026",
        "end_date": "28-09-2026",
        "discount": 2        
    },
    {
        "id_promotion": 3,
        "name_promotion": "Item Sale",
        "type_promotion": "fixed",
        "start_date": "01-09-2026",
        "end_date": "30-09-2026",
        "discount": 1000
    }
]


# /===== Feature Program =====/
# Create your feature program here   
# /===== Create Program =====/
def create_promotion():                                                                          # CREATE
    """Create a promotion"""
    print("Membuat promosi baru\n" + "-" * 50)    
    
    nama_promosi = name_promotion()
    tipe_promosi, tipe_promosi_angka = type_promotion()
    mulai_tanggal = start_date()
    selesai_tanggal = end_date(mulai_tanggal)
    diskon = discount(tipe_promosi_angka)
    
    new_promotion = {
        # TAMBAHKAN "id_promotion"
        "name_promotion": nama_promosi,
        "type_promotion": tipe_promosi,
        "start_date": mulai_tanggal,
        "end_date": selesai_tanggal,
        "discount": diskon
    }
    
    promotions.append(new_promotion)
    print(f"\n[+] Sukses menambahkan promosi {nama_promosi}\n")
    for key, value in promotions[-1].items():
        print(f"{key}: {value}", end = "\n")
    print("")
            
    return

def name_promotion():
    while True:
        name_promotion = input("Nama promosi yang ingin di buat: ").strip()
        if not name_promotion:
            print("[!] Input tidak valid! Nama promosi tidak boleh kosong!")
            continue
        
        check_name = name_promotion.replace(" ", "").replace(".", "")
        if not check_name.isalnum():
            print("[X] Input tidak valid! Hanya boleh berisi huruf, angka, spasi, dan titik!")
            continue
        return name_promotion

def type_promotion():
    while True:        
        type_promotion = int(input("\nMasukan tipe promosi:\n1. Persentasi\n2. Buy 2 Get 1\n3. Fixed\nMasukkan angka:"))
        if type_promotion not in (1, 2, 3):
            print("[X] Input tidak valid! Tipe promosi harus antara 1 (Persentase), 2 (B2G1), atau 3 (fixed)!")
            continue
        elif type_promotion == 1:
            type_value = 1
        elif type_promotion == 2:
            type_value = 2
        else:
            type_value = 3
        return type_promotion, type_value

def start_date():
    while True:
        start_input = input("\nMasukkan tanggal mulai promosi (DD-MM-YYY): ").strip()
        try:
            start_promotion = datetime.strptime(start_input, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Eror: Format tanggal salah atau kosong! Gunakan DD-MM-YYY (Contoh: 09-11-2026).")
    return start_promotion

def end_date(start_promotion):
    while True:
        end_input = input("\nMasukkan tanggal akhir promosi (DD-MM-YYY): ").strip()
        try:
            end_promotion = datetime.strptime(end_input, "%d-%m-%Y").date()
            if end_promotion < start_promotion:
                print("Eror: Tanggal akhir promosi tidak boleh lebih dulu dari tanggal mulai!")
                continue
            return end_promotion
        except ValueError:
            print("Eror: Format tanggal salah atau kosong! Gunakan DD-MM-YYY (Contoh: 09-11-2026).")

def discount(type_value):
    while True:
        try:
            if type_value == 1:
                discount_amount = int(input("\nMasukkan persentase diskon (1-20): "))
                if not (1 <= discount_amount <= 20):
                    print("[X] Persentase diskon harus di antara 1 sampai 20!")
                    continue
            elif type_value == 3:
                discount_amount = int(input("\nMasukkan berapa banyak potongan (Rupiah): "))
                if discount_amount <= 0:
                    print("[X] Potongan harga harus lebih besar dari 0!")
                    continue
            else:
                discount_amount = 0
            return discount_amount
        except ValueError:
            print("[X] Input tidak valid! Harap masukkan angka bulat!")

def get_product():                                                                          # READ
    """View + Search promotions"""
    print("List promosi saat ini:")
    for i in promotions:
        for key, value in i.items():
            print(f"{key}: {value}", end = " ")
        print("")
    return

def update_promotion():                                                                     # UPDATE
    """Function for update the sale"""
    return

def delete():                                                                               # DELETE
    """Function for delete the sale"""
    return

def search():
    """Function for searching the product"""
    return

def back():
    """Function for go back to the main menu"""
    return

def discount_rule():
    """discount calculations"""
    return

def fixed_discount():
    """fixed discount"""
    
    return

def transaction():
    """Customer purchase"""
    return

# /===== Main Program =====/
# Create your main program here
def main():
    """Function for main program
    """
    while True:
        print("\n" + "=" * 10 + " Automatic Bulk Discount Alert " + "=" * 10)
        print("""
                [1] Create Promotion
                [2] View Discounts
                [3] Update Discounts
                [4] Delete Discounts
                [5] Transaction
                [6] Exit
                """)    
        print("=" * 50 + "\n")

        input_user = input("Insert your option: ")
        print("\n" + "=" * 50 + "\n")

        if input_user == "1":
            create_promotion()
        elif input_user == "2":
            get_product()
        elif input_user == "3":
            update_promotion()
        elif input_user == "4":
            delete()
        elif input_user == "5":
            search()
        elif input_user == "6":
            break
        else:
            print("Input is not valid! Input the correct number")


if __name__ == "__main__":
    main()