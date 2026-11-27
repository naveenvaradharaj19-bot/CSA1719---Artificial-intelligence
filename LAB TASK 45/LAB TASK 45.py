
# Markov Chain

# Transition table
transition = {
    "Sunny": [("Sunny", 0.8), ("Rainy", 0.2)],
    "Rainy": [("Sunny", 0.4), ("Rainy", 0.6)]
}

current = "Sunny"

print("Current state:", current)

# Predict the most probable next state
for i in range(5):

    choices = transition[current]

    next_state = max(
        choices,
        key=lambda item: item[1]
    )[0]

    current = next_state

    print("Next state:", current)
