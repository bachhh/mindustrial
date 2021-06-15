#!/usr/bin/python3

# Extending MASM language to the ability to use label, labels are just marker
# for jumping to line number, making the code more intuitive to debug

# Usage:

# 1. use with jump
# jump <L2> equal a 1
# L2:
# op add a a 1

# 2. use with `set @counter`

# set @counter <L2>
# L2:
# op add a a 1


# Caveats:

# Any blank line preceeding / following the label will be removed
# Label must be uniquely defined, dupliate label names will be treated as error
# label are define with <NAME>: all capitalized



if __name__ == "__main__":
    main()

def main()
    #label regex
    label_regex = "^[ \t]*([A-Z0-9]+):[\t ]*$"
# label_map label
    label_map = {'label_name' : {'line': 10}}

