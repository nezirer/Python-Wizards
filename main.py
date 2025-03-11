import getpass
# Modülleri import ediyoruz
from customer import Customer
from cart import Cart
from product import Product
from order import Order

print("-----------E-ticaret otomasyonuma hoş geldiniz.-----------")

def register(customers):
    name = input("İsim: ")
    email = input("Email: ")
    password = getpass.getpass("Şifre: ")
    
    for customer in customers:
        if customer.email == email:
            print("Bu kullanıcı kayıtlı.")
            return None
    
    new_customer = Customer(name, email, password)
    customers.append(new_customer)
    print("Başarıyla oluşturuldu")
    return new_customer

def login(customers):
    email = input("Email: ")
    password = getpass.getpass("Şifre: ")
    
    for customer in customers:
        if customer.email == email and customer.password == password:
            print("Giriş başarılı")
            return customer
    
    print("Hatalı giriş")
    return None

##Main burada başlıyor

customers = []
customer = None

while not customer:
    secim = input("1- Üye Ol\n2- Giriş Yap\nSeçiminiz ")
    
    if secim == "1":
        customer = register(customers)
    elif secim == "2":
        if customers:
            customer = login(customers)
        else:
            print("Önce üye olun! ")
    else:
        print("Geçersiz seçim 1 veya 2 girin!")

## Örnek Ürünler
products = [
    Product("Köpek Maması", 1500, 3),
    Product("Kedi Mmaması", 1000, 9),
    Product("Tasma", 500, 55)
]

cart = Cart()

#SEPETİ DOLDURMA
while True:
    print("\nÜrünler:")
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product}")
    
    print("0. Sepeti Görüntüle Ödeme Yap")
    secim1 = input("Sepete eklemek istediğinzi ürünün numarasını girin: ")
    
    if secim1 == "0":
        break
        
    if not secim1.isdigit() or int(secim1) < 1 or int(secim1) > len(products):
        print("Geçersiz seçim")
        continue
        
    quantity = input("Kaç adet eklemek istiyorsunuz ? : ")
    if not quantity.isdigit() or int(quantity) < 1:
        print("Geçersiz giriş")
        continue
        
    selected_product = products[int(secim1) - 1]
    cart.add_product(selected_product, int(quantity))

print(" Sepetiniz:")
cart.display_cart()

##total para hespalama
total_amount = cart.get_total()

#sipariş onaylama kısmı
if total_amount > 0:
    print("   Sipariş vermek istiyor musunuz? (e/h)")
    confirm = input()
    
    if confirm == "e":
        order = Order(customer, cart)
        order.place_order()
    else:
        print("Sipariş iptal edildi n")
else:
    print("Sepetiniz boş sipariş verilemez")