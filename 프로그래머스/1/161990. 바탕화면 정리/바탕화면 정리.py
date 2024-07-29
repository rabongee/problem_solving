def solution(wallpaper):
    desktop = [list(w) for w in wallpaper]
    x_list = []
    y_list = []
    for y in range(len(desktop)):
        for x in range(len(desktop[y])):
            if desktop[y][x] == '#':
                y_list.append(y)
                x_list.append(x)
    return [min(y_list), min(x_list), max(y_list)+1, max(x_list)+1]