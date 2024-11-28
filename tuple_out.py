import random

def roll_dice(num):
    """Roll the specified number of dice."""
    return [random.randint(1, 6) for _ in range(num)]

def reroll_unfixed_dice(dice):
    """Handle rerolling unfixed dice until the player decides to stop or 'tuple out'."""
    while True:
        # Check for 'tuple out' condition
        if dice[0] == dice[1] == dice[2]:
            print(f"Tuple out! All dice are {dice[0]}. You score 0 points this turn.")
            return 0  # The player's turn ends with zero points

        # Identify fixed and unfixed dice
        fixed_indices = []
        if dice[0] == dice[1]:
            fixed_indices.extend([0, 1])
        if dice[0] == dice[2]:
            fixed_indices.extend([0, 2])
        if dice[1] == dice[2]:
            fixed_indices.extend([1, 2])
        fixed_indices = list(set(fixed_indices))  # Remove duplicates

        unfixed_indices = [i for i in range(3) if i not in fixed_indices]
        fixed_dice = [dice[i] for i in fixed_indices]
        unfixed_dice = [dice[i] for i in unfixed_indices]

        # If no matches, all dice are unfixed
        if not fixed_indices:
            print("No dice match, no fixed dice.")
            fixed_dice = []
            unfixed_dice = dice
            unfixed_indices = [0, 1, 2]

        print(f"Fixed dice: {fixed_dice}, Unfixed dice: {unfixed_dice}")

        # If all dice are fixed, the player cannot reroll
        if not unfixed_indices:
            print("All dice are fixed. Your turn ends.")
            break

        # Prompt the player to reroll or not, with input validation and exception handling
        try:
            choice = input("Do you want to reroll the unfixed dice? (yes/no): ").lower()
            choice = choice.strip()
            if not choice:
                print("No input detected. Defaulting to 'no'.")
                choice = 'no'
        except EOFError:
            print("Input error detected. Defaulting to 'no'.")
            choice = 'no'

        while choice not in ['yes', 'no']:
            choice = input("Please enter 'yes' or 'no': ").lower()
            choice = choice.strip()
            if not choice:
                print("No input detected. Defaulting to 'no'.")
                choice = 'no'

        if choice == 'yes':
            # Reroll unfixed dice
            new_values = roll_dice(len(unfixed_indices))
            for idx, val in zip(unfixed_indices, new_values):
                dice[idx] = val
            print(f"Dice after reroll: {dice}")
        else:
            print(f"Keeping the unfixed dice as: {unfixed_dice}")
            break

    # After rerolls, check for 'tuple out' one more time
    if dice[0] == dice[1] == dice[2]:
        print(f"Tuple out after reroll! All dice are {dice[0]}. You score 0 points this turn.")
        return 0

    # Calculate the score
    total_score = sum(dice)
    print(f"Final dice: {dice}")
    print(f"Total score this turn: {total_score}")
    return total_score

def play_turn(player_name):
    """Handle a player's turn."""
    print(f"\n{player_name}'s turn:")
    print("Rolling 3 dice...")
    dice = roll_dice(3)
    print(f"Initial roll: {dice}")

    # Handle rerolls and calculate the turn score
    turn_score = reroll_unfixed_dice(dice)
    return turn_score

def main():
    """Main game loop."""
    # Initialize player scores
    player_scores = {'Player 1': 0, 'Player 2': 0}
    target_score = 30
    players = ['Player 1', 'Player 2']
    current_player_index = 0

    while True:
        player_name = players[current_player_index]
        print(f"\n{player_name}'s total score: {player_scores[player_name]}")
        turn_score = play_turn(player_name)
        player_scores[player_name] += turn_score
        print(f"{player_name}'s updated score: {player_scores[player_name]}")

        # Check if the player has reached the target score
        if player_scores[player_name] >= target_score:
            print(f"\n{player_name} wins the game with {player_scores[player_name]} points!")
            break

        # Switch to the next player
        current_player_index = (current_player_index + 1) % len(players)

if __name__ == "__main__":
    main()
