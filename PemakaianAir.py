print(10*'=', "Pemakaian Air by Arya",'='*10)

class WS:
    def __init__ (self, customer_name, customer_type, water_usage):
        self.customer_name = customer_name
        self.customer_type = customer_type
        self.water_usage = water_usage

    def get_usage_price(self):
        usage_price = 0

        if (self.customer_type == 1):
            usage_price = self.water_usage * 15_000
        if (self.customer_type == 2):
            usage_price = self.water_usage * 13_000
        else:
            usage_price = self.water_usage * 12_000

        return usage_price

user1 = WS("Andi", 1, 120)
user2 = WS("Mesjid A", 2, 250)
user3 = WS("Sekolah B", 2, 300)
user4 = WS("Kantor C", 3, 110)

users = [user1, user2, user3, user4]

for user in users:
    print()
    print("Nama Pelanggan                : ", user.customer_name)
    print("Type Pelanggan                : ", user.customer_type)
    print("Pemakaian Air                 : ", user.water_usage)
    print("Total Harga Penggunaan Air    : Rp", user.get_usage_price())
print()