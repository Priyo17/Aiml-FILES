def calculate_flames(name1, name2):
    flames_mapping = {
        0: "Friendship",
        1: "Love",
        2: "Affection",
        3: "Marriage",
        4: "Enemy",
        5: "Sibling"
    }

    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    count = 0
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)
            count += 1

    result_index = (len(name1) + len(name2)) % len(flames_mapping)
    result = flames_mapping[result_index]

    return result

# Test the FLAMES calculator
person1 = input("Enter the name of the first person: ")
person2 = input("Enter the name of the second person: ")

relationship = calculate_flames(person1, person2)
print("The relationship between", person1, "and", person2, "is:", relationship)
