from customer import Customer
from product import Product
from cart import Cart
from order import Order

def register(customers):
    name = input("Adınız")
    email = input("Eposta adresiniz")
    password = input("Şifreniz")
    
    for customer in customers:
        if customer.email == email:
            print("Bu adres zaten mevcut")
            return None

    new_customer = Customer(name, email, password)
    customers.append(new_customer)

    print("Üyelik oluşturuldu.")
    return new_customer




def login(customers):
    email = input("E-posta ")
    password = input("Şifre ")

    for customer in customers:
        if customer.email == email and customer.password == password:
            print("Giriş başarılı")
            return customer

    print("Hatalı e-posta veya şifre!\n")
    return None





def main():

    customers = []
    customer = None
    
    while not customer:
        choice = input("1- Üye Ol\n2- Giriş Yap\nSeçiminiz: ")
        if choice == "1":
            customer = register(customers)
        elif choice == "2":
            if customers:
                customer = login(customers)
            else:
                print("Henüz kayıtlı kullanıcı yok, lütfen önce üye olun!\n")
        else:
            print("Geçersiz seçim, lütfen 1 veya 2 girin!\n")
    
    # Ürünleri oluşturma
    products = [
        Product("Laptop", 15000, 5),
        Product("Telefon", 10000, 10),
        Product("Kulaklık", 500, 20)
    ]
    
    # Sepet oluşturma
    cart = Cart()
    
    # Kullanıcıdan ürün eklemesini isteme
    while True:
        print("\nÜrünler:")
        for index, product in enumerate(products, start=1):
            print(f"{index}. {product}")
        print("0. Sepeti Görüntüle ve Ödeme Yap")
        
        choice = input("Sepete eklemek istediğiniz ürünün numarasını girin: ")
        if choice == "0":
            break
        
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(products):
            print("Geçersiz seçim, tekrar deneyin.")
            continue
        
        quantity = input("Kaç adet eklemek istiyorsunuz?: ")
        if not quantity.isdigit() or int(quantity) < 1:
            print("Geçersiz adet, tekrar deneyin.")
            continue
        
        selected_product = products[int(choice) - 1]
        cart.add_product(selected_product, int(quantity))
    
    # Sepeti görüntüleme
    print("\nSepetiniz:")
    cart.display_cart()
    
    # Sepet toplamını hesaplama
    total_amount = cart.get_total()
    if total_amount > 0:
        print("\nSipariş vermek istiyor musunuz? (E/H)")
        confirm = input().strip().lower()
        if confirm == "e":
            order = Order(customer, cart)
            order.place_order()
        else:
            print("Sipariş iptal edildi!\n")
    else:
        print("Sepetiniz boş, sipariş verilemez!\n")

if __name__ == "__main__":
    main()
