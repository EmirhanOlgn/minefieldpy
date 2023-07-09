import random
import map

print("Starting...")

scores = ["🟩", "🟨", "🟪"]
score = 0

row1 = ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜"]
row4 = ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜"]
row5 = ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜"]
row6 = ["⬜", "⬜", "⬜", "⬜", "⬜", "⬜"]
map_row = [row1, row2, row3, row4, row5, row6]

map_r = map.getmap(map_row)
print(map_r)

bomb_1_x = random.randint(1, 6)
bomb_1_y = random.randint(1, 6)
bomb_1_xy = f"{bomb_1_x}{bomb_1_y}"

bomb_2_x = random.randint(1, 6)
bomb_2_y = random.randint(1, 6)
bomb_2_xy = f"{bomb_2_x}{bomb_2_y}"

bomb_3_x = random.randint(1, 6)
bomb_3_y = random.randint(1, 6)
bomb_3_xy = f"{bomb_3_x}{bomb_3_y}"

bomb_4_x = random.randint(1, 6)
bomb_4_y = random.randint(1, 6)
bomb_4_xy = f"{bomb_4_x}{bomb_4_y}"

bomb_5_x = random.randint(1, 6)
bomb_5_y = random.randint(1, 6)
bomb_5_xy = f"{bomb_5_x}{bomb_5_y}"

for x in range(15):
    location = input(
        "Enter X-Y coordinate | Example: 13 ➡ X: 1, Y: 3 | Min: 1, Max: 6\nEnter: ")
    if (not len(location) == 2) or (int(location[0]) < 1 or int(location[0]) > 6 or int(location[1]) < 1 or int(location[1]) > 6) or (not map_row[int(location[1]) - 1][int(location[0]) - 1] == "⬜"):
        print("⛔ | U need be rules!")
    else:
        if not (int(location[0]) == bomb_1_x and int(location[1]) == bomb_1_y) or (int(location[0]) == bomb_2_x and int(location[1]) == bomb_2_y) or (int(location[0]) == bomb_3_x and int(location[1]) == bomb_3_y) or (int(location[0]) == bomb_4_x and int(location[1]) == bomb_4_y) or (int(location[0]) == bomb_5_x and int(location[1]) == bomb_5_y):
            score_rand = random.randint(1, 3)
            score += score_rand
            map_row[int(location[1]) - 1][int(location[0]) -
                                          1] = scores[score_rand - 1]
            map_r = map.getmap(map_row)
            print(map_r)
            print(f"You have got {score} score")
        else:
            map_row[int(location[1]) - 1][int(location[0]) - 1] = "💣"
            map_r = map.getmap(map_row)
            print(map_r)
            print(f"Game Over! You finish the game with {score} score")
            exit()

print(f"Game Finished! You finish the game with {score} score")
