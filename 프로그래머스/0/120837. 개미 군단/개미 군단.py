def solution(hp):
    answer = 0
    
    ant_damages=[5,3,1]
    
    for ant_damage in ant_damages:
        d, hp = divmod(hp, ant_damage)
        answer+=d
    
    return answer