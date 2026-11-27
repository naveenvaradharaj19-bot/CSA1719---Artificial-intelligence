
# Q-Learning

# States: 0, 1, 2, 3, 4
# Goal state: 4
# Actions: 0 = Left, 1 = Right

q = [[0, 0] for i in range(5)]

alpha = 0.5
gamma = 0.9

# Train agent
for episode in range(100):

    state = 0

    while state != 4:

        # Always choose right
        action = 1

        next_state = min(4, state + 1)

        if next_state == 4:
            reward = 10
        else:
            reward = -1

        q[state][action] += alpha * (
            reward + gamma * max(q[next_state]) -
            q[state][action]
        )

        state = next_state

print("Q-Table:")

for row in q:
    print([round(value, 2) for value in row])

print("Goal reached: State 4")
