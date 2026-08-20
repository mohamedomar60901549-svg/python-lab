from utils import square, is_even, celsius_to_fahrenheit, greet

def main():
    try:
        user_input = float(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    squared = square(user_input)
    parity = "even" if is_even(user_input) else "odd"
    fahrenheit = celsius_to_fahrenheit(user_input)
    
    print(f"\nResults for {user_input}:")
    print(f"  Square: {squared}")
    print(f"  Parity: {parity}")
    print(f"  Fahrenheit: {fahrenheit:.2f}°F")
    
    # Greeting
    print(greet("Student"))

if __name__ == "__main__":
    main()