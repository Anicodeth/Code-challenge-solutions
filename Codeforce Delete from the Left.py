def min_moves(s, t):
    len_s = len(s)
    len_t = len(t)
    common_suffix_length = 0
    
    while (common_suffix_length < min(len_s, len_t) and
           s[len_s - common_suffix_length - 1] == t[len_t - common_suffix_length - 1]):
        common_suffix_length += 1
    
    moves_required = len_s + len_t - 2 * common_suffix_length
    return moves_required

s = input()
t = input()

result = min_moves(s, t)
print(result)
