from PIL import Image

class Cigar:
    def __init__(self, name, size, ring_gauge, vitola, cigar_type, maker, picture=None):
        self.name = name
        self.size = size
        self.ring_gauge = ring_gauge
        self.vitola = vitola
        self.cigar_type = cigar_type
        self.maker = maker
        self.picture = picture

    def __str__(self):
        return f'{self.name} - {self.size} - {self.ring_gauge} - {self.vitola} - {self.cigar_type} - {self.maker}'


def add_cigar(cigar_list):
    name = input("Enter cigar name: ")
    size = float(input("Enter cigar size (in inches): "))
    ring_gauge = int(input("Enter cigar ring gauge: "))
    vitola = input("Enter cigar vitola: ")
    cigar_type = input("Enter cigar type: ")
    maker = input("Enter Cigar Maker: ")
    picture_path = input("Enter path to picture (optional): ")

    if picture_path:
        try:
            picture = Image.open(picture_path)
        except FileNotFoundError:
            print("Picture not found.")
            picture = None
    else:
        picture = None

    cigar = Cigar(name, size, ring_gauge, vitola, cigar_type, maker, picture)
    cigar_list.append(cigar)

    print("Cigar added successfully.")


def display_cigars(cigar_list):
    if not cigar_list:
        print("No cigars have been added.")
    else:
        print("Cigars:")
        for cigar in cigar_list:
            print(cigar)
            if cigar.picture:
                cigar.picture.show()


def main():
    cigar_list = []

    while True:
        print("\n1. Add a cigar")
        print("2. Display cigars")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_cigar(cigar_list)
        elif choice == 2:
            display_cigars(cigar_list)
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()