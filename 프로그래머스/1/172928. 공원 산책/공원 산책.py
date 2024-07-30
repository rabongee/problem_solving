def solution(park, routes):
    d = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
    s_row, s_col = None, None
    for row in range(len(park)):
        for col in range(len(park[row])):
            if park[row][col] == "S":
                s_row, s_col = row, col
                break
        if s_row is not None:
            break

    for route in routes:
        r, c = d[route[0]]
        bool_val = True
        for num in range(1, int(route[2])+1):
            add_row = s_row + r * num
            add_col = s_col + c * num
            if 0 <= add_row < len(park) and 0 <= add_col < len(park[add_row]) and park[add_row][add_col] != "X":
                continue
            else:
                bool_val = False
                break
        if bool_val:
            s_row, s_col = add_row, add_col
    return [s_row, s_col]