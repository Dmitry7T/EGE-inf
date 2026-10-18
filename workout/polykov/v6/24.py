s = open('24.txt').read().strip()

y_indices = [i for i, char in enumerate(s) if char == 'Y']

max_length = 0

for i in range(len(y_indices) - 79):
    left_boundary = y_indices[i - 1] + 1 if i > 0 else 0

    right_boundary = y_indices[i + 80] if i + 80 < len(y_indices) else len(s) 
    
    substring = s[left_boundary : right_boundary]
    
    if substring.count("2025") >= 90:
        current_length = len(substring)
        if current_length > max_length:
            max_length = current_length

print(max_length)