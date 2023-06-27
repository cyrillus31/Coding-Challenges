import sys

def solution(s1, s2):

    results = []
    _htable = {letter: 0 for letter in s2}
    htable = _htable.copy()
    
    left_index = 0
    for right_index in range(len(s1)):
        right_letter = s1[right_index]
        print(right_index, right_letter)
        if right_letter in htable:
            # print("add one")
            htable[right_letter] += 1

            if 0 not in htable.values():
                while left_index <= right_index:
                    print(left_index, right_index, htable, results)
                    if 0 not in htable.values():
                        results.append(right_index - left_index + 1)
                        left_letter = s1[left_index]
                        if left_letter in htable:
                            # print(left_letter, left_index)
                            # print("subtract one")
                            htable[left_letter] -= 1

                        left_index += 1
                    else:
                        # print("break")
                        # left_index = right_index
                        # htable = _htable.copy()
                        # print(htable)
                        break
        else:
            htable = _htable.copy()
            left_index = right_index + 1
            continue
    
        print(results)
    
    if len(results) == 0:
        return (0)
    else:
        return (min(results))

# print(solution("aabbcdd", "abcd"))
# print(solution("cdbcdbdccb", "dcb"))
print(solution("aabbbcaaab", "abc")) # answer: 3




