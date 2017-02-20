"""
Compress a string like so

aabbb -> a2b3

if the string cannotbe compressed return orginal

assume all lowercase

IT FAILS BECAUSE OF DUPLICATE LETTERS

instead use a counter instead of 2 pointers!
"""

def compress(str):
    if len(str) == 0 or len(str) == 1:
        return str

    # act as a string buffer
    res = []
    i = 0
    j = i + 1

    # append the first letter
    res.append(str[i])

    while j < len(str):
        # not the same char
        if str[i] != str[j]:
        #     append the length
            res.append(str.index(str[j]) - str.index(str[i]))
        #     append the new string
            res.append(str[j])
        #     update the position of i
            i = j

        # else they are not the same
        else:
        # iterate the 2nd pointer
            j += 1

    # append the last
    res.append(len(str) - i)

    print res
    return

def better_compr(str):
    if len(str) == 0 or len(str) == 1:
        return str

    count = 0
    i = 0
    str_buffer = []
    while i < len(str):
        count += 1
        if i + 1 == len(str) or str[i] != str[i + 1]:
            str_buffer.append(str[i])
            str_buffer.append(count)
            # reset count
            count = 0
        i += 1

    if len(str) < len(str_buffer):
        return str
    return str_buffer
