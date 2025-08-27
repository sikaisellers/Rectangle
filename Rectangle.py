class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

    def calculate_area(self):
        return self.height * self.width

    def draw_rectangle(self):
        if self.height < 2 or self.width < 2:
            print("Rectangle too small to draw a border.")
            return

        print('*' * self.width)
        for _ in range(self.height - 2):
            print('*' + ' ' * (self.width - 2) + '*')
        print('*' * self.width)

def main():
    while True:
        print("\nRectangle Calculator\n")

        height = int(input("Height: "))
        width = int(input("Width:   "))

        rect = Rectangle(height, width)

        print(f"Perimeter: {rect.calculate_perimeter()}")
        print(f"Area:   {rect.calculate_area()}\n")

        rect.draw_rectangle()

        cont = input("\nContinue? (y/n):    ").strip().lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    main()


