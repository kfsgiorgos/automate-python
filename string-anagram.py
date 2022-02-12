from collections import Counter


def isAnagram(s:str, t:str) -> bool:
    return sorted(s) == sorted(t)


def isAnagram1(s:str, t:str):
    return Counter(s) == Counter(t)




str1 = "Dormitory"
str2 = "Dirtyroom"

print(isAnagram(str1, str2))
print(isAnagram1(str1, str2))