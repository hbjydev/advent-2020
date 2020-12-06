input = []

# Set the required fields to qualify an entry as a valid passport
required = set([ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ])

with open('input.txt', 'r') as file:
    input = file.read().split('\n\n')

# Replace all newlines with spaces to standardize the input of all passports
for i in range(0, len(input)):
    input[i] = input[i].replace('\n', ' ')

    # Required to remove a 'phantom newline'
    if i == (len(input) - 1):
        input[i] = input[i][:-1]

# Counter to check how many passports are valid
passing = 0

# Loop through each individual passport
for i in range(0, len(input)):
    # Break each passport into individual field strings (key:value)
    field_strs = input[i].split(' ')

    # Create a dictionary to store the passport data
    fields = {}

    # Loop through each field string
    for i2 in range(0, len(field_strs)):
        field = field_strs[i2]

        # Break the field string into its component pieces
        spl = field.split(':')

        # Store the field data as a key and value in the passport field dictionary defined above
        fields[spl[0]] = spl[1] 

    # If the data dictionary contains all required fields...
    if all(key in fields for key in required):
        # Increment our passing counter by one.
        passing += 1

# Report our findings back to the user
print(f'{passing} passports of {len(input)} are valid.')
