# IF2211 - Strategi Algoritma
# Simulasi Sederhana - Perilaku BOT dalam Clash of Clans
# Memanfaatkan Algoritma Greedy untuk Shortest Path
# Created by : 13518056 / Michael Hans

from Point import *
from Movement import *
import time
import os

# Posisi Awal
# List of Building
B = []
B = RandomBuildingPosition(15)

# Troop sebagai titik acuan
Archer = Point(0,0)

# Main Program
os.system("cls")
PrintMap(B,Archer)
time.sleep(1)
os.system("cls")

while (len(B) != 0):
    NextP = GetNearestDefense(B, Archer)
    DeltaX = NextP.x - Archer.x
    DeltaY = NextP.y - Archer.y
    MoveList = []

    if (DeltaX > 0):
        for i in range(DeltaX):
            MoveList.append("East")
    elif (DeltaX < 0):
        for i in range(-1 * DeltaX):
            MoveList.append("West")
    if (DeltaY > 0):
        for i in range(DeltaY):
            MoveList.append("South")
    elif (DeltaY < 0):
        for i in range(-1 * DeltaY):
            MoveList.append("North")

    while (len(MoveList) != 0):
        Action = random.choice(MoveList)
        MoveList.remove(Action)
        Move(Archer, Action)
        PrintMap(B, Archer)
        time.sleep(0.3)
        os.system("cls")
    B.remove(NextP)