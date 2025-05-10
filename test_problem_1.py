def is_power_balanced(n, party_affiliations):
    # Counting how many legislators belong to each party
    counts = {1: 0, 2: 0, 3: 0}
    party_list = list(map(int, party_affiliations.split()))
    
    for party in party_list:
        counts[party] += 1

    # Checking each party to see if it dominates
    if counts[1] > counts[2] + counts[3]:
        return "Future One Dominates"
    elif counts[2] > counts[1] + counts[3]:
        return "Two-gether Dominates"
    elif counts[3] > counts[1] + counts[2]:
        return "Triple Harmony Dominates"
    else:
        return "Power Balanced"
