def solution(players, callings):
    player_indices = {player: i for i, player in enumerate(players)}
    for calling in callings:
        current_index = player_indices[calling]
        swap_index = current_index - 1
        players[swap_index], players[current_index] = players[current_index], players[swap_index]
        player_indices[players[swap_index]] = swap_index
        player_indices[players[current_index]] = current_index
    return players