# Crystal Cavern Explorer - Q8.py

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def main():
    cavern = input("Enter chamber configuration (8 characters): ").strip().upper()

    if len(cavern) != 8 or any(ch not in "CTE" for ch in cavern):
        print("Invalid configuration! Must be 8 characters: C, T, or E only.")
        return

    print("=== Crystal Cavern Explorer ===")

    health = 100
    crystals_collected = 0
    total_crystal_points = 0

    for chamber in range(1, 9):
        item = cavern[chamber - 1]

        # Crystal chamber
        if item == 'C':
            base_points = 15
            multiplier = 1
            bonus = False

            if is_prime(chamber):
                multiplier *= 2
                bonus = True

            if crystals_collected % 2 == 0:
                multiplier *= 2
                bonus = True

            crystal_points = base_points * multiplier
            total_crystal_points += crystal_points
            crystals_collected += 1

            if bonus:
                print(f"Chamber {chamber} (C): Found crystal! +{crystal_points} points (Bonus applied!)")
            else:
                print(f"Chamber {chamber} (C): Found crystal! +{crystal_points} points")

        # Trap chamber
        elif item == 'T':
            damage = 20
            if health % chamber == 0:
                damage //= 2
            health -= damage
            print(f"Chamber {chamber} (T): Hit trap! -{damage} health")

        # Empty chamber
        elif item == 'E':
            health = min(100, health + 5)
            if chamber == 8:
                print(f"Chamber {chamber} (E): Safe exit!")
            else:
                print(f"Chamber {chamber} (E): Empty chamber, resting... +5 health")

        # Check death
        if health <= 0:
            print("You have fallen in the cavern! Final Score: 0")
            return

    # Final calculations
    final_score = total_crystal_points + (health // 2)

    print(f"Final Status: Health={health}, Crystals={crystals_collected}, Crystal Points={total_crystal_points}")
    print(f"Final Score: {final_score}")


if __name__ == "__main__":
    main()
