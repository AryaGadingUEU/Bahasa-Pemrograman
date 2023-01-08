def main():
    pil = 0
    while True:
        print("=== MAIN MENU ===")
        print("0. Exit")
        print("1. Garden")
        pil = int(input("Masukan Pilihan : "))
        
        if pil == 0:
            print("Exit...")
            break
        elif pil == 1:
            print("Menuju Garden")
            garden_menu()
        else:
            print("Menu tidak ada!")

def garden_menu():
    anggrek = Anggrek()
    melati = Melati()
    mawar = Mawar()
    plants = [anggrek, melati, mawar]
    
    pil = 0
    while True:
        print("\n=== GARDEN MENU ===")
        print("0. Exit")
        print("1. Anggrek")
        print("2. Melati")
        print("3. Mawar")
        pil = int(input("Masukan Pilihan : "))
    
        if pil == 0:
            print("Kembali ke menu utama...")
            break
        elif pil == 1:
            anggrek.growth_menu()
        elif pil == 2:
            melati.growth_menu()
        elif pil == 3:
            mawar.growth_menu()
        else:
            print("Menu tidak ada!")

class Plant:
    def __init__(self):
        self.water = 0
        self.fertilizer = 0
        self.growth_stage = 0
        self.growth_stage_names = ["Benih", "Tunas", "Tanaman Kecil", "Tanaman Dewasa", "Berbunga"]
    
    def add_water(self):
        self.water += 1
        self.grow()

    def add_fertilizer(self):
        self.fertilizer += 1
        self.grow()

    def display_plant(self):
        print(f"Status Tumbuh: {self.growth_stage_names[self.growth_stage]}\nJumlah Air: {self.water}\nJumlah Pupuk: {self.fertilizer}")

class Anggrek(Plant):
    def growth_menu(self):
        inp = 0
        print("\n---- Anggrek ----")
        print("Status saat ini:")
        self.display_plant()
        while True:
            print("Masukkan:")
            print("1. untuk memberi air")
            print("2. untuk memberi pupuk")
            print("0. untuk keluar")
            print("Anggrek membutuhkan 2 air dan 3 pupuk")
            inp = int(input("Pilihan : "))
            if inp == 0:
                break
            elif inp == 1:
                self.add_water()
            elif inp == 2:
                self.add_fertilizer()
            else:
                print("Menu tidak ada!")
            
            print("\n---------------")
            self.display_plant()
            print("---------------\n")

    def grow(self):
        if self.water >= 2 and self.fertilizer >= 3:
            self.water -= 2
            self.fertilizer -= 3
            self.growth_stage += 1
        if self.growth_stage >= len(self.growth_stage_names):
            self.growth_stage = len(self.growth_stage_names) - 1


class Melati(Plant):
    def growth_menu(self):
        inp = 0
        print("\n---- Melati ----")
        print("Status saat ini:")
        self.display_plant()
        while True:
            print("Masukkan:")
            print("1. untuk memberi air")
            print("2. untuk memberi pupuk")
            print("0. untuk keluar")
            print("Melati membutuhkan 5 air dan 1 pupuk")
            inp = int(input("Pilihan : "))
            if inp == 0:
                break
            elif inp == 1:
                self.add_water()
            elif inp == 2:
                self.add_fertilizer()
            else:
                print("Menu tidak ada!")
            
            print("\n---------------")
            self.display_plant()
            print("---------------\n")

    def grow(self):
        if self.water >= 5 and self.fertilizer >= 1:
            self.water -= 5
            self.fertilizer -= 1
            self.growth_stage += 1
        if self.growth_stage >= len(self.growth_stage_names):
            self.growth_stage = len(self.growth_stage_names) - 1

class Mawar(Plant):
    def growth_menu(self):
        inp = 0
        print("\n---- Mawar ----")
        print("Status saat ini:")
        self.display_plant()
        while True:
            print("Masukkan:")
            print("1. untuk memberi air")
            print("2. untuk memberi pupuk")
            print("0. untuk keluar")
            print("Mawar membutuhkan 3 air dan 4 pupuk")
            inp = int(input("Pilihan : "))
            if inp == 0:
                break
            elif inp == 1:
                self.add_water()
            elif inp == 2:
                self.add_fertilizer()
            else:
                print("Menu tidak ada!")
            
            print("\n---------------")
            self.display_plant()
            print("---------------\n")

    def grow(self):
        if self.water >= 3 and self.fertilizer >= 4:
            self.water -= 3
            self.fertilizer -= 4
            self.growth_stage += 1
        if self.growth_stage >= len(self.growth_stage_names):
            self.growth_stage = len(self.growth_stage_names) - 1

if __name__ == "__main__":
    main()