def solution(wallet, bill):
    answer = 0
    queue = [bill]
    while queue:
        w, h = queue.pop()
        if min(wallet) >= min(w, h) and max(wallet) >= max(w, h):
            break
        elif min(wallet) < min(w, h):
            queue.append([(max(w, h) // 2), min(w, h)])
            answer += 1
            continue
        elif max(wallet) < max(w, h):
            queue.append([(max(w, h) // 2), min(w, h)])
            answer += 1
            continue
    return answer