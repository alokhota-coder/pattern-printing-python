"""
Dice Roller Simulation
----------------------
A menu-driven mini project that simulates rolling dice using basic Python.

Python concepts used:
variables, input/output, data types, operators, if/elif/else,
while and for loops, functions, lists, dictionaries,
the random module, string formatting, try/except (error handling).
"""

import random


# ---------- Helper functions ----------

def get_number(message, minimum, maximum):
    """Keep asking until the user enters a whole number in the given range."""
    while True:
        try:
            value = int(input(message))
            if minimum <= value <= maximum:
                return value
            print(f"  Please enter a number between {minimum} and {maximum}.")
        except ValueError:
            print("  Invalid input! Please enter a whole number.")


def roll_die(sides):
    """Roll one die with the given number of sides."""
    return random.randint(1, sides)


def draw_die(number):
    """Print a small ASCII picture of a standard 6-sided die face."""
    faces = {
        1: ["+-------+", "|       |", "|   *   |", "|       |", "+-------+"],
        2: ["+-------+", "| *     |", "|       |", "|     * |", "+-------+"],
        3: ["+-------+", "| *     |", "|   *   |", "|     * |", "+-------+"],
        4: ["+-------+", "| *   * |", "|       |", "| *   * |", "+-------+"],
        5: ["+-------+", "| *   * |", "|   *   |", "| *   * |", "+-------+"],
        6: ["+-------+", "| *   * |", "| *   * |", "| *   * |", "+-------+"],
    }
    for line in faces[number]:
        print(line)


# ---------- Menu options ----------

def roll_one(history, sides):
    """Option 1: roll a single die."""
    result = roll_die(sides)
    history.append(result)
    print(f"\nYou rolled: {result}")
    if sides == 6:
        draw_die(result)


def roll_many(history, sides):
    """Option 2: roll several dice at once and show the total."""
    count = get_number("How many dice do you want to roll (1-10)? ", 1, 10)
    results = []
    for _ in range(count):
        value = roll_die(sides)
        results.append(value)
        history.append(value)
    print("\nResults :", results)
    print("Total   :", sum(results))


def simulate(sides):
    """Option 3: roll the die many times and show how often each side came up."""
    times = get_number("How many times to roll (1-10000)? ", 1, 10000)

    frequency = {}                      # dictionary: side -> count
    for side in range(1, sides + 1):
        frequency[side] = 0

    for _ in range(times):
        frequency[roll_die(sides)] += 1

    print(f"\nSimulation of {times} rolls")
    print("-" * 40)
    for side in frequency:
        count = frequency[side]
        percent = count / times * 100
        bar = "#" * int(percent)        # simple text bar chart
        print(f"Side {side:>2}: {count:>5} ({percent:5.1f}%) {bar}")


def show_history(history):
    """Option 4: show all rolls and some simple statistics."""
    if len(history) == 0:
        print("\nNo rolls yet. Roll a die first!")
        return
    print("\nAll rolls so far:", history)
    print("Total rolls     :", len(history))
    print("Highest roll    :", max(history))
    print("Lowest roll     :", min(history))
    print(f"Average roll    : {sum(history) / len(history):.2f}")


def change_sides(current):
    """Option 5: change the number of sides of the die."""
    new_sides = get_number("Enter number of sides (2-100): ", 2, 100)
    print(f"Die changed to {new_sides} sides.")
    return new_sides


# ---------- Main program ----------

def main():
    print("=" * 40)
    print("      DICE ROLLER SIMULATION")
    print("=" * 40)

    sides = 6
    history = []

    while True:
        print(f"\n--- MENU (die has {sides} sides) ---")
        print("1. Roll one die")
        print("2. Roll multiple dice")
        print("3. Run a simulation (many rolls)")
        print("4. Show roll history and statistics")
        print("5. Change number of sides")
        print("6. Exit")

        choice = get_number("Enter your choice (1-6): ", 1, 6)

        if choice == 1:
            roll_one(history, sides)
        elif choice == 2:
            roll_many(history, sides)
        elif choice == 3:
            simulate(sides)
        elif choice == 4:
            show_history(history)
        elif choice == 5:
            sides = change_sides(sides)
        else:
            print("\nThank you for playing. Goodbye!")
            break


main()