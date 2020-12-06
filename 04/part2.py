input = []

# Set the required fields to qualify an entry as a valid passport
required = set([ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ])

with open('input.txt', 'r') as file:
    input = file.read().split('\n\n')

# Replace all newlines with spaces to standardize the input of all passports
for i in range(0, len(input)):
    input[i] = input[i].replace('\n', ' ')

    # Required to remove a 'phantom newline'
    #if i == (len(input) - 1):
    #    input[i] = input[i][:-2]

# Counter to check how many passports are valid
passing = 0

def date_quan(value: int, minimum: int, maximum: int) -> bool:
    if len(str(value)) != 4:
        return False
    if value < minimum:
        return False
    if value > maximum:
        return False
    return True

def length_quan(value: str, minimum: int, maximum: int) -> bool:
    int_val = int(value[:-2])
    if int_val < minimum:
        return False
    if int_val > maximum:
        return False
    return True

def hex_quan(value: str) -> bool:
    if value[0] != '#':
        return False
    if len(value[1:]) != 6:
        return False
    return True

def col_quan(value: str) -> bool:
    possible = [ 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' ]
    if value in possible:
        return True
    return False

def id_quan(value: str) -> bool:
    if value.isdigit():
        if len(value) != 9:
            return False
        return True
    else:
        return False

# Loop through each individual passport
for i in range(0, len(input)):
    # Break each passport into individual field strings (key:value)
    field_strs = input[i].split(' ')

    # Create a dictionary to store the passport data
    fields = {}

    # Loop through each field string
    for i2 in range(0, len(field_strs)):
        field = field_strs[i2]

        if field != '':
            # Break the field string into its component pieces
            spl = field.split(':')

            # Store the field data as a key and value in the passport field dictionary defined above
            fields[spl[0]] = spl[1] 

    # Go through validity checks on each field (if it exists)
    is_passing = True
    if 'byr' in fields:
        result = date_quan(int(fields['byr']), 1920, 2002)
        print(f'{i} -> byr:{fields["byr"]} -> {result}')
        is_passing = result if is_passing else is_passing
    if 'iyr' in fields:
        result = date_quan(int(fields['iyr']), 2010, 2020)
        print(f'{i} -> iyr:{fields["iyr"]} -> {result}')
        is_passing = result if is_passing else is_passing
    if 'eyr' in fields:
        result = date_quan(int(fields['eyr']), 2020, 2030)
        print(f'{i} -> eyr:{fields["eyr"]} -> {result}')
        is_passing = result if is_passing else is_passing
    if 'hgt' in fields:
        result = True
        if 'cm' in fields['hgt']:
            result = length_quan(fields['hgt'], 150, 193)
        elif 'in' in fields['hgt']:
            result = length_quan(fields['hgt'], 59, 76)
        else:
            result = False
        print(f'{i} -> hgt:{fields["hgt"]} -> {result}')
        is_passing = result if is_passing else is_passing
    if 'hcl' in fields:
        result = hex_quan(fields['hcl'])
        print(f'{i} -> hcl:{fields["hcl"]} -> {result}')
        is_passing = result if is_passing else is_passing
    if 'ecl' in fields:
        result = col_quan(fields['ecl'])
        print(f'{i} -> ecl:{fields["ecl"]} -> {result}')
        is_passing = result if is_passing else is_passing
    if 'pid' in fields:
        result = id_quan(fields['pid'])
        print(f'{i} -> pid:{fields["pid"]} -> {result}')
        is_passing = result if is_passing else is_passing

    # If the data dictionary contains all required fields...
    if not all(key in fields for key in required):
        # Increment our passing counter by one.
        is_passing = False

    print(f'\nOverall Verdict: {"invalid" if is_passing == False else "valid"}')
    if is_passing == True:
        passing += 1

    print('\n-------------------------\n')

# Report our findings back to the user
print(f'{passing} passports of {len(input)} are valid.')
