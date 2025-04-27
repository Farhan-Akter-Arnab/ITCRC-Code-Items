import math
def calculator():
    def simple_operator():
        def add(x, y):
            return x + y
        def subtract(x, y):
            return x - y
        def multiply(x, y):
            return x * y
        def divide(x, y):
            if y == 0:
                raise ValueError("Cannot divide by zero")
            return x / y
        def exponent(x, y):
            return x ** y
        def modulus(x, y):
            return x % y
        print("Select operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("6. Modulus (%)")
        print("7. Exit")
        operation = int(input("Enter operation (1-7): "))
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        def cal_simple(n1, n2):
            if operation == 1:
                add_result = add(n1, n2)
                print(n1, " + ", n2, " = ", add_result)
            elif operation == 2:
                subtract_result = subtract(n1, n2)
                print(n1, " - ", n2, " = ", subtract_result)
            elif operation == 3:
                multiply_result = multiply(n1, n2)
                print(n1, " * ", n2, " = ", multiply_result)
            elif operation == 4:
                divide_result = divide(n1, n2)
                print(n1, " / ", n2, " = ", divide_result)
            elif operation == 5:
                exponent_result = exponent(n1, n2)
                print(n1, " ^ ", n2, " = ", exponent_result)
            elif operation == 6:
                modulus_result = modulus(n1, n2)
                print(n1, " % ", n2, " = ", modulus_result)
            elif operation == 7:
                print("Exiting the simple calculator.")
                return
            else:
                print("Invalid operation. Please try again.")
                return
        cal_simple(n1, n2)
        print("Do you want to perform another calculation? (yes/no)")
        if input().lower() == 'yes':
            simple_operator()
        elif input().lower() == 'no':
            print("Exiting the simple calculator.")
            calculator()
        else:
            print("Invalid input. Please try again.")
            return
    def scientific():
        def sine(x):
            return math.sin(math.radians(x))
        def cosine(x):
            return math.cos(math.radians(x))
        def tangent(x):
            return math.tan(math.radians(x))
        def cotangent(x):
            return 1 / math.tan(math.radians(x))
        def secant(x):
            return 1 / math.cos(math.radians(x))
        def cosecant(x):
            return 1 / math.sin(math.radians(x))
        def logarithm(x):
            return math.log(x)
        def natural_logarithm(x):
            return math.log(x, math.e)
        def logarithm_base_dif(x, base):
            return math.log(x, base)
        print("Select operation:")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        print("4. Cotangent")
        print("5. Secant")
        print("6. Cosecant")
        print("7. Logarithm (base 10)")
        print("8. Natural Logarithm")
        print("9. Logarithm with different base")
        print("10. Exit")
        operation = int(input("Enter operation (1-10): "))
        n = float(input("Enter number by which you want to calculate: "))
        def cal_sci(x):
            if operation == 1:
                sine_result = sine(x)
                print("sin(", x, ") = ", sine_result)
            elif operation == 2:
                cosine_result = cosine(x)
                print("cos(", x, ") = ", cosine_result)
            elif operation == 3:
                tangent_result = tangent(x)
                print("tan(", x, ") = ", tangent_result)
            elif operation == 4:
                cotangent_result = cotangent(x)
                print("cot(", x, ") = ", cotangent_result)
            elif operation == 5:
                secant_result = secant(x)
                print("sec(", x, ") = ", secant_result)
            elif operation == 6:
                cosecant_result = cosecant(x)
                print("csc(", x, ") = ", cosecant_result)
            elif operation == 7:
                logarithm_result = logarithm(x)
                print("log(", x, ") = ", logarithm_result)
            elif operation == 8:
                natural_logarithm_result = natural_logarithm(x)
                print("ln(", x, ") = ", natural_logarithm_result)
            elif operation == 9:
                base = float(input("Enter base: "))
                logarithm_base_dif_result = logarithm_base_dif(x, base)
                print("log_", base, "(", x, ") = ", logarithm_base_dif_result)
            elif operation == 10:
                print("Exiting the scientific calculator.")
                return
            else:
                print("Invalid operation. Please try again.")
        cal_sci(n)
        print("Do you want to perform another calculation? (yes/no)")
        if input().lower() == 'yes':
            scientific()
        elif input().lower() == 'no':
            print("Exiting the scientific calculator.")
            calculator()
        else:
            print("Invalid input. Please try again.")
            return
    def bmi_calculator(m, h_m, h_cm, h_f, h_in):
        if h_m <= 0 or h_cm <= 0 or h_f <= 0 or h_in <= 0:
            raise ValueError("Height must be natural number! Please try again.")
            bmi_calculator(m, h_m, h_cm, h_f, h_in)
        def bmi_metric(m, h_m):
            return m / (h_m ** 2)
        def bmi_imperial(m, h_f, h_in):
            return (m / (h_f ** 2)) * 703
        print("Select unit system:")
        print("1. Metric (kg/m^2)")
        print("2. Imperial (lb/in^2)")
        unit = int(input("Enter unit system (1-2): "))
        if unit == 1:
            m = float(input("Enter weight in kg: "))
            h_m = float(input("Enter height in meters: "))
            bmi_result = bmi_metric(m, h_m)
            print("BMI: ", bmi_result)
        elif unit == 2:
            m = float(input("Enter weight in pounds: "))
            h_f = int(input("Enter height in feet: "))
            h_in = int(input("Enter height in inches: "))
            total_height_in_inches = (h_f * 12) + h_in
            bmi_result = bmi_imperial(m, total_height_in_inches)
            print("BMI: ", bmi_result)
        else:
            print("Invalid unit system. Please try again.")
        print("Do you want to perform another calculation? (yes/no)")
        if input().lower() == 'yes':
            bmi_calculator()
        elif input().lower() == 'no':
            print("Exiting the BMI calculator.")
            calculator()
        else:
            print("Invalid input. Please try again.")
            return
    def area_calculator():
        def rectangle(length, width):
            return length * width
        def triangle(base, height):
            return 0.5 * base * height
        def circle(radius):
            return math.pi * (radius ** 2)
        def cylinder(radius, height):
            return math.pi * (radius ** 2) * height
        def sphere(radius):
            return (4/3) * math.pi * (radius ** 3)
        def cone(radius, height):
            return (1/3) * math.pi * (radius ** 2) * height
        def square(side):
            return side ** 2
        def triangle_with_sides(a,b,c):
            s = (a + b + c) / 2
            return math.sqrt(s * (s - a) * (s - b) * (s - c))
        def cube(side):
            return 6 * (side ** 2)
        def cuboid(length, width, height):
            return 2 * (length * width + width * height + length * height)
        def trapezium(a, b, height):
            return ((a + b) / 2) * height
        def parallelogram(base, height):
            return base * height
        def rhombus(diagonal1, diagonal2):
            return (diagonal1 * diagonal2) / 2
        print("Select shape:")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle")
        print("4. Cylinder")
        print("5. Sphere")
        print("6. Cone")
        print("7. Square")
        print("8. Triangle with sides")
        print("9. Cube")
        print("10. Cuboid")
        print("11. Trapezium")
        print("12. Parallelogram")
        print("13. Rhombus")
        print("14. Exit")
        shape = int(input("Enter shape (1-14): "))
        def area_cal(shape):
            if shape == 1:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                area_result = rectangle(length, width)
                print("Area of rectangle: ", area_result)
            elif shape == 2:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                area_result = triangle(base, height)
                print("Area of triangle: ", area_result)
            elif shape == 3:
                radius = float(input("Enter radius: "))
                area_result = circle(radius)
                print("Area of circle: ", area_result)
            elif shape == 4:
                radius = float(input("Enter radius: "))
                height = float(input("Enter height: "))
                area_result = cylinder(radius, height)
                print("Area of cylinder: ", area_result)
            elif shape == 5:
                radius = float(input("Enter radius: "))
                area_result = sphere(radius)
                print("Area of sphere: ", area_result)
            elif shape == 6:
                radius = float(input("Enter radius: "))
                height = float(input("Enter height: "))
                area_result = cone(radius, height)
                print("Area of cone: ", area_result)
            elif shape == 7:
                side = float(input("Enter side: "))
                area_result = square(side)
                print("Area of square: ", area_result)
            elif shape == 8:
                a = float(input("Enter side a: "))
                b = float(input("Enter side b: "))
                c = float(input("Enter side c: "))
                area_result = triangle_with_sides(a, b, c)
                print("Area of triangle with sides: ", area_result)
            elif shape == 9:
                side = float(input("Enter side: "))
                area_result = cube(side)
                print("Area of cube: ", area_result)
            elif shape == 10:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                height = float(input("Enter height: "))
                area_result = cuboid(length, width, height)
                print("Area of cuboid: ", area_result)
            elif shape == 11:
                a = float(input("Enter side a: "))
                b = float(input("Enter side b: "))
                height = float(input("Enter height: "))
                area_result = trapezium(a, b, height)
                print("Area of trapezium: ", area_result)
            elif shape == 12:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                area_result = parallelogram(base, height)
                print("Area of parallelogram: ", area_result)
            elif shape == 13:
                diagonal1 = float(input("Enter diagonal 1: "))
                diagonal2 = float(input("Enter diagonal 2: "))
                area_result = rhombus(diagonal1, diagonal2)
                print("Area of rhombus: ", area_result)
            elif shape == 14:
                print("Exiting the area calculator.")
                return
            else:
                print("Invalid shape. Please try again.")
                return
        area_cal(shape)
        print("Do you want to perform another calculation? (yes/no)")
        if input().lower() == 'yes':
            area_calculator()
        elif input().lower() == 'no':
            print("Exiting the area calculator.")
            calculator()
        else:
            print("Invalid input. Please try again.")
            return
    def volume_calculator():
        def cube(side):
            return side ** 3
        def cuboid(length, width, height):
            return length * width * height
        def sphere(radius):
            return (4/3) * math.pi * (radius ** 3)
        def cylinder(radius, height):
            return math.pi * (radius ** 2) * height
        def cone(radius, height):
            return (1/3) * math.pi * (radius ** 2) * height
        print("Select shape:")
        print("1. Cube")
        print("2. Cuboid")
        print("3. Sphere")
        print("4. Cylinder")
        print("5. Cone")
        print("6. Exit")
        shape = int(input("Enter shape (1-6): "))
        def volume_cal(shape):
            if shape == 1:
                side = float(input("Enter side: "))
                volume_result = cube(side)
                print("Volume of cube: ", volume_result)
            elif shape == 2:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                height = float(input("Enter height: "))
                volume_result = cuboid(length, width, height)
                print("Volume of cuboid: ", volume_result)
            elif shape == 3:
                radius = float(input("Enter radius: "))
                volume_result = sphere(radius)
                print("Volume of sphere: ", volume_result)
            elif shape == 4:
                radius = float(input("Enter radius: "))
                height = float(input("Enter height: "))
                volume_result = cylinder(radius, height)
                print("Volume of cylinder: ", volume_result)
            elif shape == 5:
                radius = float(input("Enter radius: "))
                height = float(input("Enter height: "))
                volume_result = cone(radius, height)
                print("Volume of cone: ", volume_result)
            elif shape == 6:
                print("Exiting the volume calculator.")
                return
            else:
                print("Invalid shape. Please try again.")
                return
        volume_cal(shape)
        print("Do you want to perform another calculation? (yes/no)")
        if input().lower() == 'yes':
            volume_calculator()
        elif input().lower() == 'no':
            print("Exiting the volume calculator.")
            calculator()
        else:
            print("Invalid input. Please try again.")
            return
    def perimeter_calculator():
        def rectangle(length, width):
            return 2 * (length + width)
        def triangle(a, b, c):
            return a + b + c
        def circle(radius):
            return 2 * math.pi * radius
        def square(side):
            return 4 * side
        def parallelogram(base, height):
            return 2 * (base + height)
        def trapezium(a, b, c, d):
            return a + b + c + d
        print("Select shape:")
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle")
        print("4. Square")
        print("5. Parallelogram")
        print("6. Trapezium")
        print("7. Exit")
        shape = int(input("Enter shape (1-5): "))
        def perimeter_cal(shape):
            if shape == 1:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                perimeter_result = rectangle(length, width)
                print("Perimeter of rectangle: ", perimeter_result)
            elif shape == 2:
                a = float(input("Enter side a: "))
                b = float(input("Enter side b: "))
                c = float(input("Enter side c: "))
                perimeter_result = triangle(a, b, c)
                print("Perimeter of triangle: ", perimeter_result)
            elif shape == 3:
                radius = float(input("Enter radius: "))
                perimeter_result = circle(radius)
                print("Perimeter of circle: ", perimeter_result)
            elif shape == 4:
                side = float(input("Enter side: "))
                perimeter_result = square(side)
                print("Perimeter of square: ", perimeter_result)
            elif shape == 5:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                perimeter_result = parallelogram(base, height)
                print("Perimeter of parallelogram: ", perimeter_result)
            elif shape == 6:
                a = float(input("Enter side a: "))
                b = float(input("Enter side b: "))
                c = float(input("Enter side c: "))
                d = float(input("Enter side d: "))
                perimeter_result = trapezium(a, b, c, d)
                print("Perimeter of trapezium: ", perimeter_result)
            elif shape == 7:
                print("Exiting the perimeter calculator.")
                return
            else:
                print("Invalid shape. Please try again.")
                return
        perimeter_cal(shape)
        print("Do you want to perform another calculation? (yes/no)")
        if input().lower() == 'yes':
            perimeter_calculator()
        elif input().lower() == 'no':
            print("Exiting the perimeter calculator.")
            calculator()
        else:
            print("Invalid input. Please try again.")
            return
    def temp_calculator():
        def celsius_to_fahrenheit(c):
            return (c * 9/5) + 32
        def fahrenheit_to_celsius(f):
            return (f - 32) * 5/9
        def celsius_to_kelvin(c):
            return c + 273.15
        def kelvin_to_celsius(k):
            return k - 273.15
        def fahrenheit_to_kelvin(f):
            return (f - 32) * 5/9 + 273.15
        def kelvin_to_fahrenheit(k):
            return (k - 273.15) * 9/5 + 32
        print("Select conversion:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")
        conversion = int(input("Enter conversion (1-7): "))
        if conversion == 1:
            c = float(input("Enter temperature in Celsius: "))
            result = celsius_to_fahrenheit(c)
            print(c, "C = ", result, "F")
        elif conversion == 2:
            f = float(input("Enter temperature in Fahrenheit: "))
            result = fahrenheit_to_celsius(f)
            print(f, "F = ", result, "C")
        elif conversion == 3:
            c = float(input("Enter temperature in Celsius: "))
            result = celsius_to_kelvin(c)
            print(c, "C = ", result, "K")
        elif conversion == 4:
            k = float(input("Enter temperature in Kelvin: "))
            result = kelvin_to_celsius(k)
            print(k, "K = ", result, "C")
        elif conversion == 5:
            f = float(input("Enter temperature in Fahrenheit: "))
            result = fahrenheit_to_kelvin(f)
            print(f, "F = ", result, "K")
        elif conversion == 6:
            k = float(input("Enter temperature in Kelvin: "))
            result = kelvin_to_fahrenheit(k)
            print(k, "K = ", result, "F")
        elif conversion == 7:
            print("Exiting the temperature calculator.")
            return
        else:
            print("Invalid conversion. Please try again.")
            return
        print("Do you want to perform another calculation? (yes/no)")
        if input().lower() == 'yes':
            temp_calculator()
        elif input().lower() == 'no':
            print("Exiting the temperature calculator.")
            calculator()
        else:
            print("Invalid input. Please try again.")
            return
    def set_operation():
        def union(set1, set2):
            return set1.union(set2)
        def intersection(set1, set2):
            return set1.intersection(set2)
        def difference(set1, set2):
            return set1.difference(set2)
        def symmetric_difference(set1, set2):
            return set1.symmetric_difference(set2)
        print("Select operation:")
        print("1. Union")
        print("2. Intersection")
        print("3. Difference")
        print("4. Symmetric Difference")
        print("5. Exit")
        operation = int(input("Enter operation (1-5): "))
        set1 = set(map(int, input("Enter first set (space-separated): ").split()))
        set2 = set(map(int, input("Enter second set (space-separated): ").split()))
        def cal_set(op):
            if op == 1:
                result = union(set1, set2)
                if result == set():
                    print("Union: Ø")
                    print("Empty set")
                else:
                    print("Union: ", result)
            elif op == 2:
                result = intersection(set1, set2)
                if result == set():
                    print("Intersection: Ø")
                    print("Empty set")
                else:
                    print("Intersection: ", result)
            elif op == 3:
                result = difference(set1, set2)
                if result == set():
                    print("Difference: Ø")
                    print("Empty set")
                else:
                   print("Difference: ", result) 
            elif op == 4:
                result = symmetric_difference(set1, set2)
                if result == set():
                    print("Symmetric Difference: Ø")
                    print("Empty set")
                else:
                    print("Symmetric Difference: ", result)
            elif op == 5:
                print("Exiting the set operation calculator.")
                return
            else:
                print("Invalid operation. Please try again.")
                return
        cal_set(operation)
        print("Do you want to perform another calculation? (yes/no)")
        if input().lower() == 'yes':
            set_operation()
        elif input().lower() == 'no':
            print("Exiting the set operation calculator.")
            calculator()
        else:
            print("Invalid input. Please try again.")
            return
    def exit_program():
        print("Exiting the calculator program. Goodbye!")
        return
    print("Welcome to the calculator programme!")
    print("Please select the type of calculator you want to use: ")
    print("1. Simple Calculator")
    print("2. Scientific Calculator")
    print("3. BMI Calculator")
    print("4. Area Calculator")
    print("5. Volume Calculator")
    print("6. Perimeter Calculator")
    print("7. Temperature Conversion")
    print("8. Set Operation")
    print("9. Exit")
    choice = int(input("Enter your choice (1-9): "))
    if choice == 1:
        simple_operator()
    elif choice == 2:
        scientific()
    elif choice == 3:
        bmi_calculator()
    elif choice == 4:
        area_calculator()
    elif choice == 5:
        volume_calculator()
    elif choice == 6:
        perimeter_calculator()
    elif choice == 7:
        temp_calculator()
    elif choice == 8:
        set_operation()
    elif choice == 9:
        exit_program()
    else:
        print("Invalid choice. Please try again.")
        calculator()
    print("Do you want to perform another calculation? (yes/no)")
    if input().lower() == 'yes':
        simple_operator()
    elif input().lower() == 'no':
        print("Exiting the scientific calculator.")
        calculator()
    else:
        print("Invalid input. Please try again.")
        return
calculator()
if __name__ == "__main__":
    calculator()