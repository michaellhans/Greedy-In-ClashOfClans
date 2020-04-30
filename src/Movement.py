# Movement.py

import random
from Point import *

# Membangkitkan titik-titik dalam Simulasi secara random
def RandomBuildingPosition(N):
    B = []
    for i in range (N):
        x = random.randint(0,9)
        y = random.randint(0,9)
        if (x == 0) and (y == 0):
            continue
        else:
            B.append(Point(x,y))
    return B

# Add Something to Certain Coordinates
def AddBuilding(M, S):
    M[S.y][S.x] = 1

# Add Troop to Certain Coordinates
def AddTroop(M, T):
    M[T.y][T.x] = 2

# Troop bergerak 1 satuan ke arah Action
def Move(T, Action):
    if (Action == "North"):
        T.y -= 1
    elif (Action == "South"):
        T.y += 1
    elif (Action == "West"):
        T.x -= 1
    elif (Action == "East"):
        T.x += 1

# Menambahkan setiap building dalam B ke dalam peta M
def BuildingToMap(M, B):
    for Building in B:
        AddBuilding(M, Building)

# Menuliskan peta permainan ke dalam layar
def PrintMap (B, T):
    # Representasi Peta dalam Bentuk Matriks
    M = [[0 for j in range(10)] for i in range(10)]
    BuildingToMap(M, B)
    AddTroop(M, T)
    print("IF2211 - Strategi Algoritma")
    print("Simulasi Pergerakan BOT dalam Clash of Clans")
    print("Created by: 13518056 / Michael Hans")
    print("--------------------------------")
    for i in range(10):
        print("|", end="")
        for j in range(10):
            if (M[i][j] == 0):
                print('   ', end="")
            elif (M[i][j] == 1):
                print(' D ', end="")
            elif (M[i][j] == 2):
                print(' T ', end="")
        print("|")
    print("--------------------------------")

# Mencari bangunan defense terdekat dari titik Troop
def GetNearestDefense (B, T):
    P = None
    MinDistance = 9999
    for Building in B:
        Distance = Building.distance(T)
        if (Distance < MinDistance):
            MinDistance = Distance
            P = Building
    return P