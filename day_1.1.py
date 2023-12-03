line_num_string = ""
string_total = 0

# Loop through each line of the input
for _, j in enumerate(input.split(f"\n")):
    # Loop through ea character in line
    for _, d in enumerate(j):
        # Try to cast d as an int, throw error
        try:
            if type(int(d)) == int:
                # If d can be cast as int, check that we're not going over a len of 2
                if len(line_num_string) >= 2:
                    line_num_string = line_num_string[:1] + d
                else:
                    line_num_string += d
        except:
            continue
    
    # Check for single number case in line (num is both first and last)
    if len(line_num_string) == 1:
        line_num_string += line_num_string

    # Add line string to total:
    try:
        string_total += int(line_num_string)
    except:
        continue

    # Reset line string
    line_num_string = ""

print(string_total)