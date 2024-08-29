#####################################################################
#                              Import                               #
#####################################################################
import random

#####################################################################
#                         Doors LMAD class                          #
#####################################################################
class DoorsLMAD:
    def __init__(self, prizeDoor: int = -1, numberDoors: int = 3):
        self.choiceChanged = False
        self.doorsOpen     = False
        self.selectedDoor  = -1
        self.numberDoors   = numberDoors
        self.prizeDoor     = random.randint(1, self.numberDoors) if (prizeDoor < 0) or (prizeDoor > self.numberDoors) else prizeDoor

    def getClosedDoors(self):
        if self.doorsOpen:
            return [self.selectedDoor, self.prizeDoor if self.prizeDoor != self.selectedDoor else (self.prizeDoor + 1) % self.numberDoors]
        else:
            return [i for i in range(1, self.numberDoors)]

    def getPrizeDoor(self):
        return self.prizeDoor

    def selectDoor(self, number: int):
        if number >= 0 and number < self.numberDoors:
            self.selectedDoor = number

    def changeChoice(self):
        self.choiceChanged = True

    def openEmptyDoors(self):
        self.doorsOpen = True

    def isWin(self):
        return self.selectedDoor >= 0 and ((self.prizeDoor == self.selectedDoor and not self.choiceChanged) or (self.prizeDoor != self.selectedDoor and self.choiceChanged))
