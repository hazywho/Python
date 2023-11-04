n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]

# Initialize a list to keep track of the sum of each card's values
card_sums = [a + b + c + d for a, b, c, d in cards]
# Sort the cards by their sums in descending order
cards_sorted = sorted(enumerate(card_sums), key=lambda x: x[1], reverse=True)

# Initialize variables to keep track of the best arrangement and maximum points
best_arrangement = [0] * n
max_points = 0

# Iterate through the top m cards and try different arrangements
for i in range(m):
    card_idx = cards_sorted[i][0]
    print(cards_sorted)
    best_arrangement[card_idx] = 1
    max_points += card_sums[card_idx]

# Iterate through the remaining cards and fill in the arrangement
for i in range(m, n):
    card_idx = cards_sorted[i][0]
    best_arrangement[card_idx] = 2

# Print the maximum points Evirir can gain
print(max_points)