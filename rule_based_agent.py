def rule_based_agent(temperature):
    if temperature > 100:
        return "cool"
    else:
        return "normal"


# Test cases
temperatures = [80, 100, 101, 120]

for temp in temperatures:
    action = rule_based_agent(temp)

    print(f"Temperature: {temp}")
    print(f"Agent action: {action}")
    print("_" * 30)


def calculator():
    print("Calculator Agent")
    print("_" * 30)


calculator()

