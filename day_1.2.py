def filter_string(s, indx):
    # Build trie of strings:
    trie = {
        "o": {"on": {"one": 1}},
        "t": {"tw": {"two": 2}, "th": {"thr": {"thre": {"three": 3}}}},
        "f": {"fo": {"fou": {"four": 4}}, "fi": {"fiv": {"five": 5}}},
        "s": {"si": {"six": 6}, "se": {"sev": {"seve": {"seven": 7}}}},
        "e": {"ei": {"eig": {"eigh": {"eight": 8}}}},
        "n": {"ni": {"nin": {"nine": 9}}},
    }

    # Set current_node to root of trie:
    current_node = trie
    built_string = ""

    for i in range(indx, len(s)):
        # Set current character and string to test against current_node in trie
        c = s[i]
        test_string = built_string + c

        # Try to find current built string in trie:
        try:
            test_node = current_node[test_string]
        except:
            # If it didn't work, character could be a numeric
            try:
                test_node = int(test_string)
            except:
                # If it's not in the trie, and not a numeric, reset built string and current node
                return []
                break

        # test_node is either a numeric, a node, or a leaf in the trie
        if isinstance(test_node, dict):
            # If we're partway down the trie (on a node), set the built_string to the test_string
            built_string = test_string
            current_node = test_node

        elif isinstance(test_node, int):
            # If it's an int (a leaf or numeric in the string), we've found a number, return
            return str(test_node)


calibration_total = 0

# Loop through input string, breaking on \n char
for i, line in enumerate(input.split(f"\n")):
    # Loop through input, based on the current indx into it
    nums_in_line = []

    for n in range(0, len(line)):
        # Stop on each letter, send it to the number filter function, then move pointer
        current_char = line[n]

        # filter function returns number found (if any)
        filtered_res = filter_string(line, n)

        if filtered_res is None:
            continue

        if len(filtered_res) != 0:
            filtered_num = filtered_res
            nums_in_line.append(str(filtered_num))

        if n > len(line) - 1:
            break

    # Now get the calibration for the line:
    calibration = nums_in_line[0] + nums_in_line[len(nums_in_line) - 1]
    calibration_total += int(calibration)


print(calibration_total)