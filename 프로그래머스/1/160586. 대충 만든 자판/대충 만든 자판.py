def solution(keymap, targets):
    answer = []
    keymap_dict = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] in keymap_dict:
                keymap_dict[key[i]] = min(i + 1, keymap_dict[key[i]])
            else:
                keymap_dict[key[i]] = i + 1
    for word in targets:
        value = 0
        for spelling in word:
            if spelling in keymap_dict:
                value += keymap_dict[spelling]
            else:
                value = -1
                break
        answer.append(value)
    return answer