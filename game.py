from config import *

class Game:
  def __init__(self):
    self.rooms = LEVEL
    self.currentRoomIndex = 0
    self.currentRoom = self.getCurrentRoom()

    self.player = None

    self.actors = []
    self.currentActorIndex = 0
    self.currentActor = None

    self.showContextMenu = False
    self.showStatsMenu = False

  def toggleContextMenu(self):
    self.showContextMenu = not self.showContextMenu

  def toggleStatsMenu(self):
    self.showStatsMenu = not self.showStatsMenu

  def setPlayer(self, player):
    self.player = player
    self.addActor(self.player)

  def addActor(self, actor):
    self.actors.append(actor)

  def getCurrentRoom(self):
    return self.rooms[self.currentRoomIndex]

  def nextRoomIndex(self):
    if self.currentRoomIndex < len(self.rooms):
      self.currentRoomIndex += 1
    else:
      self.currentRoomIndex = 0

  def getCurrentActor(self):
    try:
      return self.actors[self.currentActorIndex]
    except IndexError:
      pass

  def setCurrentActor(self):
    self.currentActor = self.getCurrentActor()
    self.currentActor.steps = self.currentActor._steps

  def nextActorIndex(self):
    if self.currentActorIndex < len(self.actors) - 1:
      self.currentActorIndex += 1
    else:
      self.currentActorIndex = 0

  def nextTurn(self):
    self.nextActorIndex()
    self.setCurrentActor()

game = Game()