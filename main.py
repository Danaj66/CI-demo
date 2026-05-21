from probability import distribute_dons, calculate_probability


def main():
    hand_size = int(input("Opponent hand size: "))
    lives = int(input("Opponent lives: "))

    leader = int(input("Leader attack: "))

    characters = input(
        "Character attacks separated by commas: "
    )

    print(f"Opponent has {hand_size} cards and {lives} lives.")

    character_list = [int(x.strip()) for x in characters.split(",")]

    attacks = [leader] + character_list

    print("\nGenerating attack combinations...\n")

    combinations = distribute_dons(attacks)

    for combo in combinations[:10]:
        print(f"Attack setup: {combo}")

        for counter in [0, 1000, 2000]:
            probability = calculate_probability(combo, counter)

            print(
                f"  vs {counter} counter: "
                f"{probability}% success"
            )

        print()


if __name__ == "__main__":
    main()
