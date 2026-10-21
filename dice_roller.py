import random


def get_number(message, minimum, maximum):
    while True:
        try:
            value = int(input(message))
            if minimum <= value <= maximum:
                return value
            print(f"  Please enter a number between {minimum} and {maximum}.")
        except ValueError:
            print("  Invalid input! Please enter a whole number.")


def roll_die(sides):
    return random.randint(1, sides)


def draw_die(number):
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


def roll_one(history, sides):
    result = roll_die(sides)
    history.append(result)
    print(f"\nYou rolled: {result}")
    if sides == 6:
        draw_die(result)


def roll_many(history, sides):
    count = get_number("How many dice do you want to roll (1-10)? ", 1, 10)
    results = []
    for _ in range(count):
        value = roll_die(sides)
        results.append(value)
        history.append(value)
    print("\nResults :", results)
    print("Total   :", sum(results))


def simulate(sides):
    times = get_number("How many times to roll (1-10000)? ", 1, 10000)

    frequency = {}
    for side in range(1, sides + 1):
        frequency[side] = 0

    for _ in range(times):
        frequency[roll_die(sides)] += 1

    print(f"\nSimulation of {times} rolls")
    print("-" * 40)
    for side in frequency:
        count = frequency[side]
        percent = count / times * 100
        bar = "#" * int(percent)
        print(f"Side {side:>2}: {count:>5} ({percent:5.1f}%) {bar}")


def show_history(history):
    if len(history) == 0:
        print("\nNo rolls yet. Roll a die first!")
        return
    print("\nAll rolls so far:", history)
    print("Total rolls     :", len(history))
    print("Highest roll    :", max(history))
    print("Lowest roll     :", min(history))
    print(f"Average roll    : {sum(history) / len(history):.2f}")


def change_sides(current):
    new_sides = get_number("Enter number of sides (2-100): ", 2, 100)
    print(f"Die changed to {new_sides} sides.")
    return new_sides


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
