
def runSimulation(orePrice, clayPrice, obsidianPrice, geodePrice, minutes = 24):
    inventory = {
            'ore': 0,
            'clay': 0,
            'obsidian': 0,
            'geode': 0
            }

    robots = {
            'ore': 1,
            'clay': 0,
            'obsidian': 0,
            'geode': 0
            }
    # Unpack costs
    geodeCostOre, geodeCostObsidian = geodePrice
    obsidianCostOre, obsidianCostClay = obsidianPrice

    for minute in range(minutes):
        geodeBought = False
        obsidianBought = False
        clayBought = False
        oreBought = False
        print(f"== Minute {minute+1} ==")
        # Check if geode bot can be bought
        if ((inventory['ore'] >= geodeCostOre) and (inventory['obsidian'] >= geodeCostObsidian)):
            print("Geode bot was bought")
            geodeBought = True
            inventory['ore'] -= geodeCostOre
            inventory['obsidian'] -= geodeCostObsidian

        # Check if obsidian bot can be bought
        elif ((inventory['ore'] >= obsidianCostOre) and (inventory['clay'] >= obsidianCostClay)):
            print("Obsidian bot was bought")
            obsidianBought = True
            inventory['ore'] -= obsidianCostOre
            inventory['clay'] -= obsidianCostClay

        # Check if clay robot can be bought

        elif (inventory['ore'] >= clayPrice):
            print("Clay bot was bought")
            clayBought = True
            inventory['ore'] -= clayPrice

        elif (inventory['ore'] >= orePrice):
            print("Ore robot was bought")
            oreBought = True
            inventory['ore'] -= orePrice

        # Calculate earnings from each robot
        inventory['ore'] += robots['ore']
        print(f"{robots['ore']} ore-collecting robots collects {robots['ore']} ore; you now have {inventory['ore']} ore.")
        inventory['clay'] += robots['clay']
        print(f"{robots['clay']} clay-collecting robots collects {robots['clay']} clay; you now have {inventory['clay']} clay.")
        inventory['obsidian'] += robots['obsidian']
        print(f"{robots['obsidian']} obsidian-collecting robots collects {robots['obsidian']} obsidian; you now have {inventory['obsidian']} obsidian.")
        inventory['geode'] += robots['geode']
        print(f"{robots['geode']} geode-collecting robots collects {robots['geode']} geode; you now have {inventory['geode']} geode.")

        if (geodeBought):
            robots['geode'] += 1
        elif (obsidianBought):
            robots['obsidian'] += 1
        elif (clayBought):
            robots['clay'] += 1
        elif (oreBought):
            robots['ore'] += 1

    return inventory['geode']


# Unpack input
lines = []

with open("day19TestInput.txt", 'r') as f:
    lines = f.readlines()

# Sum of all blueprintIds * geodes farmed in 24 minutes
sumQualityLevels = 0

for blueprintId in range(len(lines)):
    splitted = lines[blueprintId].split(" ")
    oreCost = int(splitted[6])
    clayCost = int(splitted[12])
    obsidianCostOre = int(splitted[18])
    obsidianCostClay = int(splitted[21])
    geodeCostOre = int(splitted[27])
    geodeCostObsidian = int(splitted[30])

    # Run simulation
    geodes = runSimulation(oreCost, clayCost, (obsidianCostOre, obsidianCostClay), (geodeCostOre, geodeCostObsidian))

    sumQualityLevels += (blueprintId + 1) * geodes

print(f"{sumQualityLevels = }")

