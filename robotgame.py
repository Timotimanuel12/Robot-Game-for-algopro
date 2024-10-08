import random
Zones = {
    "town": ['power cells', 'enemy', 'batteries'],
    "village": ['batteries', 'power cells', 'enemy'],
    "city": ['batteries', 'enemy', 'power cells']
}

# Initial Specs
Inventory = []
power_cells = 0
default_battery = 100
current_zone = "Space"
total_power_cells = 3

#Scoring Criteria
total_moves = 0
total_enemies = 0
total_batteries = 0

def move_zone_to_zone(zone): #Moving from zone to zone
    global current_zone
    while zone not in Zones:
        print("Zone is invalid, Please enter a valid zone! ")
        zone = input("Please enter another zone (town, city or village): ")
    print(f'Moving from {current_zone} to {zone}')
    current_zone = zone
    item = random.choice(Zones[zone])
    print(f'You are in {zone} and have acquired some/encountered an {item}')
    return item
            

def collect_item(item): # What happens when you collect the items
    global power_cells, default_battery, total_enemies, total_batteries
    if item == 'power cells':
        Inventory.append(item)
        power_cells += 1
        print("Yay you have acquired a power cell! Collect all 3 to win")
    elif item == 'batteries':
        default_battery += 10
        total_batteries += 1
        print("Yay! You have acquired batteries! 10% would be added to your current battery level.")
    elif item == 'enemy':
        default_battery -= 10
        total_enemies += 1
        print("You have encountered an enemy! You managed to defeat them, but 10% is drained from your current battery level")
    else:
        print("There are no items to be added :(")

def display_inventory(): #Displays the player's current inventory as a list
    print(f'Inventory = {Inventory}')

def calculate_score(): #Scoring system
    global power_cells, default_battery, total_moves, total_enemies, total_batteries
    score = ((power_cells) + (default_battery) + (total_moves) + (total_enemies) + (total_batteries))/5
    return score



#Game Loop
while default_battery > 0 and power_cells < total_power_cells:
    print(f'Battery Percentage = {default_battery}')
    print("Collect all 3 Power Cells to win the game!")
    zone = input("Please enter a zone (town, village or city): ")
    total_moves += 1
    items = move_zone_to_zone(zone)
    collected = collect_item(items)
    display_inventory()

    if len(Inventory) == total_power_cells: #Finish The game if all power cells are collected
        print("Yay!! Congratulations! You have finished the game!!")
        break

    elif default_battery == 0: #finish the game if battery runs out
        print("Oh no! You ran out of battery :( Game over.")
        break

print()

final_score = calculate_score() #Displays final score after winning
print("--- Game Summary ---")
print(f'Final Score: {final_score}')
print(f'Total Moves: {total_moves}')
print(f'Enemies fought: {total_enemies}')
print(f'Battery packs Collected: {total_batteries}')
print(f'Battery Left: {default_battery}%')
print(f'Power Cells Collected: {power_cells}/{total_power_cells}')

