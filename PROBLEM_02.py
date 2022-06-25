player_one, player_two = input().split(", ")

size = 6
matrix = []

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

current_player, other_player = player_one, player_two
hited_walls = {
    player_one: "GO",
    player_two: "GO"
}

command = input()
while True:
    coordinates = command.strip("()").split(", ")
    row = int(coordinates[0])
    col = int(coordinates[1])
    if hited_walls[current_player] == "PASS":
        hited_walls[current_player] = "GO"
        current_player, other_player = other_player, current_player
        command = input()
        continue
    if matrix[row][col] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    if matrix[row][col] == "T":
        print(f"{current_player} is out of the game! The winner is {other_player}.")
        break
    if matrix[row][col] == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        hited_walls[current_player] = "PASS"
    current_player, other_player = other_player, current_player
    command = input()
