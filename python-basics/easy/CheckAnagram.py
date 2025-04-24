def check_anagram(s1: str, s2: str) -> bool:
    normalised_string1 = s1.replace(" ", "").lower()
    normalised_string2 = s2.replace(" ", "").lower()

    if len(normalised_string1) != len(normalised_string2):
        return False

    if sorted(normalised_string1) == sorted(normalised_string2):
        return True


print(check_anagram('Listen', "Silent"))
print(check_anagram("Conversation", "Voices rant on"))
print(check_anagram("Apple", "Pebble"))