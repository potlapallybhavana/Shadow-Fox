"""
Beginner Task 3: List – Justice League operations
Follow the steps and print the list after each update.
"""

def print_step(title, lst):
    print(f"\n{title}:")
    print(lst)

if __name__ == "__main__":
    justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

    # 1) Count members
    print_step("Initial team", justice_league)
    print("Members count:", len(justice_league))

    # 2) Add Batgirl and Nightwing
    justice_league.extend(["Batgirl", "Nightwing"])
    print_step("After adding Batgirl & Nightwing", justice_league)

    # 3) Make Wonder Woman the leader (move to start)
    justice_league.remove("Wonder Woman")
    justice_league.insert(0, "Wonder Woman")
    print_step("Wonder Woman as leader (moved to index 0)", justice_league)

    # 4) Separate Aquaman and Flash by inserting either GL or Superman
    # ensure Aquaman before Flash
    aq_idx = justice_league.index("Aquaman")
    fl_idx = justice_league.index("Flash")
    if aq_idx > fl_idx:
        aq_idx, fl_idx = fl_idx, aq_idx
    # Choose "Green Lantern" to insert between them
    between = "Green Lantern"
    # Remove original and reinsert positions
    justice_league.remove(between)
    justice_league.insert(aq_idx + 1, between)
    print_step("Inserted Green Lantern between Aquaman and Flash", justice_league)

    # 5) Replace team with new members
    justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
    print_step("New team formed", justice_league)

    # 6) Sort alphabetically and show new leader at index 0
    justice_league.sort()
    print_step("Sorted team (alphabetical)", justice_league)
    print("New leader (index 0):", justice_league[0])
