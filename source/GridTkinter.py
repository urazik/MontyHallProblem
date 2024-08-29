#####################################################################
#                              Import                               #
#####################################################################
import tkinter as tk
import queue

#####################################################################
#                        Grid Tkinter class                         #
#####################################################################
class GridTkinter:
    def __init__(self, root: tk.Tk, rows: int = 10, cols: int = 10, cellSize: int = 50, startX: int = 0, startY: int = 0, label: str = ""):
        self.root         = root
        self.rows         = rows
        self.cols         = cols
        self.cellSize     = cellSize
        self.labelText    = label
        if self.labelText != "":
            self.labelText += ": "

        self.label = tk.Label(root, text=f"{self.labelText}{0:.2f}% (0 / {self.cols * self.rows})", font=("Helvetica", 12))
        self.label.place(x=startX, y=startY - 30)

        self.canvas = tk.Canvas(root, width=cols * cellSize, height=rows * cellSize)
        self.canvas.place(x=startX, y=startY)
        self.reset()

        self.taskQueue = queue.Queue()
        self.__processQueue()

    def __drawGrid(self):
        self.rects = []
        for i in range(self.rows):
            rowRects = []
            for j in range(self.cols):
                x1 = j  * self.cellSize
                y1 = i  * self.cellSize
                x2 = x1 + self.cellSize
                y2 = y1 + self.cellSize
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")
                rowRects.append(rect)
            self.rects.append(rowRects)

    def __clearGrid(self):
        self.canvas.delete("all")
        self.label.config(text=f"{self.labelText}{self.numberFilled * 100 / (self.cols * self.rows):.2f}% ({self.numberFilled} / {self.cols * self.rows})")

    def __processQueue(self):
        try:
            while True:
                task = self.taskQueue.get_nowait()
                if task:
                    task()
        except queue.Empty:
            pass
        self.root.after(100, self.__processQueue)

    def __addTask(self, task):
        self.taskQueue.put(task)

    def __fillSquare(self):
        self.canvas.itemconfig(self.rects[self.currentRow][self.currentCol], fill="red")
        self.numberFilled += 1
        self.label.config(text=f"{self.labelText}{self.numberFilled * 100 / (self.cols * self.rows):.2f}% ({self.numberFilled} / {self.cols * self.rows})")
        self.__nextSquare()

    def __nextSquare(self):
        self.currentCol += 1
        if self.currentCol >= self.cols:
            self.currentCol = 0
            self.currentRow += 1

    def reset(self):
        self.numberFilled = 0
        self.currentRow   = 0
        self.currentCol   = 0
        self.__clearGrid()
        self.__drawGrid()

    def fillSquare(self):
        self.__addTask(self.__fillSquare())

    def skipSquare(self):
        self.__nextSquare()
