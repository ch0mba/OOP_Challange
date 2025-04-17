from pet import Pet  # Import the Pet class from the pet module

def main():
    # Create a new pet object
    my_pet = Pet("Kitty")

    # Test the pet's initial status
    print("\n--- Initial Status ---")
    my_pet.get_status()

    # Feed the pet
    print("\n--- Feeding the Pet ---")
    my_pet.eat()
    my_pet.get_status()

    # Play with the pet
    print("\n--- Playing with the Pet ---")
    my_pet.play()
    my_pet.get_status()

    # Let the pet sleep
    print("\n--- Letting the Pet Sleep ---")
    my_pet.sleep()
    my_pet.get_status()

    # Train the pet some tricks
    print("\n--- Training the Pet ---")
    my_pet.train("Fetch")
    my_pet.train("Roll Over")
    my_pet.show_tricks()

    # Final status of the pet
    print("\n--- Final Status ---")
    my_pet.get_status()

# Run the main function
if __name__ == "__main__":
    main()