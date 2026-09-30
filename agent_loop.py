def agent(observation):
    # Decide
    if observation > 50:
        return "Turn ON Fan"
    else:
        return "Turn OFF Fan"


# Observe → Decide → Act loop
observations = [70, 40, 60]

for i in range(3):
    # Observe
    observation = observations[i]

    # Decide
    action = agent(observation)

    # Act
    print(f"Iteration {i + 1}")
    print(f"Observation: {observation}")
    print(f"Action: {action}")
    print()