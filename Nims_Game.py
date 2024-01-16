def nim_game():
    piles = [3, 4, 5]  # Initial number of objects in each pile

    while any(piles):  # Continue the game until there are no objects left
        print("Current Piles:", piles)

        # Player's turn
        pile_choice = int(input("Choose a pile (1, 2, or 3): ")) - 1
        while pile_choice < 0 or pile_choice >= len(piles) or piles[pile_choice] == 0:
            print("Invalid choice. Try again.")
            pile_choice = int(input("Choose a pile (1, 2, or 3): ")) - 1

        objects_to_remove = int(input(f"Remove how many objects from pile {pile_choice + 1}: "))
        while objects_to_remove <= 0 or objects_to_remove > piles[pile_choice]:
            print("Invalid number of objects. Try again.")
            objects_to_remove = int(input(f"Remove how many objects from pile {pile_choice + 1}: "))

        piles[pile_choice] -= objects_to_remove

        # Check if the player wins
        if all(pile == 0 for pile in piles):
            print("Congratulations! You win!")
            break

        # Opponent's turn
        print("\nOpponent's Turn:")
        for i in range(len(piles)):
            if piles[i] > 0:
                objects_to_remove = piles[i]
                print(f"Opponent removes {objects_to_remove} objects from pile {i + 1}.")
                piles[i] -= objects_to_remove
                break

        # Check if the opponent wins
        if all(pile == 0 for pile in piles):
            print("You lose. Better luck next time!")

if __name__ == "__main__":
    nim_game()


