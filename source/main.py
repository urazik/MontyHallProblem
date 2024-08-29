#####################################################################
#                              Import                               #
#####################################################################
import tkinter as tk
import random
from GridTkinter import GridTkinter
from DoorsLMAD import DoorsLMAD

#####################################################################
#                          Some functions                           #
#####################################################################
def process(numberTrys: int, numberDoors: int, gridStatic: GridTkinter, gridChange: GridTkinter, gridNew: GridTkinter):
    gridStatic.reset()
    gridChange.reset()
    gridNew.reset()
    for i in range(numberTrys):
        doorsLMAD = DoorsLMAD(numberDoors=numberDoors)
        doorsLMAD.selectDoor(random.randint(1, numberDoors))
        doorsLMAD.openEmptyDoors()
        if doorsLMAD.isWin():
            gridStatic.fillSquare()
        else:
            gridStatic.skipSquare()

        doorsLMAD = DoorsLMAD(numberDoors=numberDoors)
        doorsLMAD.selectDoor(random.randint(1, numberDoors))
        doorsLMAD.openEmptyDoors()
        doorsLMAD.changeChoice()
        if doorsLMAD.isWin():
            gridChange.fillSquare()
        else:
            gridChange.skipSquare()

        new = bool(random.getrandbits(1))
        if doorsLMAD.isWin() and new or not doorsLMAD.isWin() and not new:
            gridNew.fillSquare()
        else:
            gridNew.skipSquare()

#####################################################################
#                               Main                                #
#####################################################################
if __name__ == "__main__":
    windowWidth  = 1600
    windowHeight = 800
    offset       = 50
    rows         = 30
    cols         = 30
    cellSize     = min((windowHeight - offset * 3) / rows, (windowWidth - offset * 4) / (cols * 3))
    windowWidth  = int(offset * 4 + cols * cellSize * 3)
    windowHeight = int(offset * 3 + rows * cellSize)
    numberDoors  = 3

    root = tk.Tk()
    root.title("Парадокс Монти Холла")
    root.geometry(f"{windowWidth}x{windowHeight}")

    height = 20

    label = tk.Label(root, text=f"Число дверей: ", font=("Helvetica", 10))
    label.place(x=offset + 120, y=(offset-height)/2, height=height)

    entry = tk.Entry(root)
    entry.place(x=offset + 220, y=(offset-height)/2, width=100, height=height)

    button = tk.Button(root, text="Запустить", command=lambda: process(rows*cols, numberDoors if entry.get() == "" else int(entry.get()), gridStatic, gridChange, gridNew))
    button.place(x=offset, y=(offset-height)/2, width=100, height=height)

    gridStatic = GridTkinter(root, rows=rows, cols=cols, cellSize=cellSize, startX=offset * 1 + (windowWidth - 200) / 3 * 0, startY=offset * 2, label="Без изменения решения")
    gridChange = GridTkinter(root, rows=rows, cols=cols, cellSize=cellSize, startX=offset * 2 + (windowWidth - 200) / 3 * 1, startY=offset * 2, label="Постоянное изменение решения")
    gridNew    = GridTkinter(root, rows=rows, cols=cols, cellSize=cellSize, startX=offset * 3 + (windowWidth - 200) / 3 * 2, startY=offset * 2, label="Принятие решения перед последней дверю")

    root.mainloop()
