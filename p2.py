import numpy as np 
import pandas as pd
import os

def bfs(src, target):
    queue = []
    queue.append(src)
    
    visited = set()
    
    while len(queue) > 0:
        source = queue.pop(0)
        visited.add(tuple(source))
        
        print(source)
        
        if source == target:
            print("Success")
            return
        
        possible_moves_to_do = possible_moves(source, visited)
        
        for move in possible_moves_to_do:
            queue.append(move)

def possible_moves(state, visited_states):
    b = state.index(0)  # Index of the empty spot
    
    # Directions array
    d = []
    if b not in [0, 1, 2]: 
        d.append('u')
    if b not in [6, 7, 8]: 
        d.append('d')
    if b not in [0, 3, 6]: 
        d.append('l')
    if b not in [2, 5, 8]: 
        d.append('r')
        
    poss_moves_it_can = []
    
    for i in d:
        poss_moves_it_can.append(gen(state, i, b))
        
    return [move_it_can for move_it_can in poss_moves_it_can if tuple(move_it_can) not in visited_states]

def gen(state, m, b):
    temp = state.copy()
    
    if m == 'd':
        temp[b + 3], temp[b] = temp[b], temp[b + 3]
    if m == 'u':
        temp[b - 3], temp[b] = temp[b], temp[b - 3]
    if m == 'l':
        temp[b - 1], temp[b] = temp[b], temp[b - 1]
    if m == 'r':
        temp[b + 1], temp[b] = temp[b], temp[b + 1]
    
    return temp

src = [1, 2, 3, 4, 5, 6, 0, 7, 8]
target = [1, 2, 3, 4, 5, 6, 7, 8, 0]         
bfs(src, target)
