def anagrammi(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(anagrammi("Listen", "Silent"))  # True
print(anagrammi("Hello", "World"))  # False
```

```python
def anagrammi(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

print(anagrammi("Listen ", "Silent"))  # True
print(anagrammi("Hello", "World"))  # False
```

```python
def anagrammi(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return set(s1) == set(s2)

print(anagrammi("Listen ", "Silent"))  # True
print(anagrammi("Hello", "World"))  # False
