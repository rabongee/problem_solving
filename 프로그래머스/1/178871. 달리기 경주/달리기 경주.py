def solution(players, callings):
    player_dict = {player: i for i, player in enumerate(players)}

    for calling in callings:
        current_rank = player_dict[calling]
        outpace = current_rank - 1
        players[outpace], players[current_rank] = players[current_rank], players[outpace]
        player_dict[players[outpace]] = outpace
        player_dict[players[current_rank]] = current_rank
    return players