def solution(points, routes):
    answer = 0
    paths = []
    max_time = -1
    
    for route in routes:
        r, c = points[route[0] - 1]
        path = [(r, c)]
        
        for i in range(1, len(route)):
            tr, tc = points[route[i] - 1]
            
            while r != tr:
                if r < tr:
                    r += 1
                else:
                    r -= 1
                path.append((r, c))
            
            while c != tc:
                if c < tc:
                    c += 1
                else:
                    c -= 1
                path.append((r, c))
                
        paths.append(path)
        max_time = max(max_time, len(path))
    
    for j in range(max_time):
        time_position = {}
        for i in range(len(paths)):
            if len(paths[i]) > j:
                time_position[paths[i][j]] = time_position.get(paths[i][j], 0) + 1
        
        for num in time_position.values():
            if num >= 2:
                answer += 1
                
    return answer