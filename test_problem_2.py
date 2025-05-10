def is_intuitive(element_name, abbreviation):
    
    element_name_lower = element_name.lower()
    abbreviation_lower = abbreviation.lower()

    # For each letter in the abbreviation check if in the element name
    for letter in abbreviation_lower:
        if letter not in element_name_lower:
            return "NO"
    
    return "YES"
