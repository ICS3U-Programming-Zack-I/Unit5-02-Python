# Created by: Zack Isingoma
# Created on: 19th Jan 2022.
# calculates area of triangle
def calc_area(base, height):
    area = (1/2)*base*height
    print("Given {}cm and {}cm the area is {}cm^2"
          .format(base, height, area))


def main():
    print("Welcome")
    user_base = input("Enter the base of the triangle(cm): ")
    user_height = input("Enter height of triangle(cm): ")
    try:
        base_from_user = float(user_base)
        height_from_user = float(user_height)
    except Exception:
        print("Invalid input")

    calc_area(base_from_user, height_from_user)


if __name__ == "__main__":
    main()
