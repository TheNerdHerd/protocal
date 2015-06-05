#in animation sprite....
#TODO: use a queue to store all queued movements
#TODO: fix a bug where if one sets a sprite to go to a new position right after he did likewise, the sprite acts weird; unable to induce bug

#import and initialize pygame
from fractions import gcd
from collections import deque
import pygame
pygame.init()
#classes
#stdsprite: a basic sprite used in the createButton function
#a stdsprite is represented by one image, and is drawn to (posX, posY)... very basic
#you will have to inherit this if create a sprite based off of this
class stdSprite(pygame.sprite.Sprite):
	def __init__(self, posX, posY, imageLocation):
		pygame.sprite.Sprite.__init__(self)
		self.posX = posX
		self.posY = posY
		self.image = pygame.image.load(imageLocation)
		self.rect = self.image.get_rect()
		self.shown = True
		self.oldPosY = self.posY
		self.posX = posX
		self.posY = posY
		#self.shown = False

	def show(self):
		self.posX = self.oldPosX
		self.posY = self.oldPosY
		self.shown = True

	def update(self):
		self.rect.center = (self.posX, self.posY)

	def getPosition(self):
		#if the sprite is shown
		if self.shown:
			return (self.posX, self.posY)
		#if the sprite is hidden
		else:
			return (self.oldPosX, self.oldPosY)

	def toggleVisibility():
		if shown:
			self.hide()
			shown = False
		else:
			self.show()
			shown = True

	posX = -1000
	posY = -1000
	oldPosX = -1000
	oldPosY = -1000
	shown = True

#animatedSprite: provides a sprite whose purpose is moving about programatically, inherits from stdSprite
class animatedSprite(stdSprite):
	def __init__(self, screen, background, posX, posY, imageLocation, speed = 1):
		pygame.sprite.Sprite.__init__(self)
		stdSprite.__init__(self, posX, posY, imageLocation)
		self.destinationX = posX
		self.destinationY = posY
		self.printStats()
		self.speed = speed
		self.paused = False
		self.movementQueue = deque([])
	def update(self):
		#the sprite moves y units up for every x units right, this ratio is obtained by run/rise if run > rise
		#if rise > run, the sprite moves x units right for every y units up and is obtained by rise/run
		#assume that the sprite is moving
		#self.stopped = False
		self.dx = 0
		self.dy = 0
		if self.stopped and self.movementQueue:
			print "stuff"
			temp = self.movementQueue.popleft()
			self.destinationX = temp[0]
			self.destinationY = temp[1]
			self.rise = self.destinationY - self.posY
			self.run = self.destinationX - self.posX
			if self.destinationX > self.posX:
				self.right = True
			else:
				self.right = False

			if self.destinationY > self.posY:
					self.down = True
			else:
				self.down = False
			self.stopped = False

		if not self.paused:
			#if the distance right is greater than the distance up
			if abs(self.run) > abs(self.rise):
				#if the sprite has to go up and that it is moving
				if abs(self.rise) > 0 and self.stopped == False:
					#This sets DX based on if it has to go right
					if self.right:
						self.dx = 1 * self.speed
					else:
						self.dx = -1 * self.speed

					#increment the counter
					self.counter += 1
					#e.g: for every 3 right, go up 1... this checks for the "3 right"
					if self.counter == self.run / self.rise:
						#reset the counter... more efficient to use modulo?
						self.counter = 0
						if self.down:
							self.dy = 1 * self.speed
						else:
							self.dy = -1 * self.speed
					else:
						#print "stuff"
						self.dy = 0

			#if rise and run is equal
			elif self.run == self.rise:
				#if the sprite needs to go down or up
				if self.rise != 0:
					if self.right:
						self.dx = 1 * self.speed
					else:
						self.dx = -1 * self.speed

					if self.down:
						self.dy = 1 * self.speed
					else:
						self.dy = -1 * self.speed

			#if the sprite's run is greater than its rise
			elif abs(self.rise) > abs(self.run):
				#if the sprite has to go up and that it is moving
				if abs(self.run) > 0 and self.stopped == False:
					#This sets DX based on if it has to go right
					#print "stuff"
					if self.right:
						self.dy = 1 * self.speed
					else:
						self.dy = -1 * self.speed
					#increment the counter
					self.counter += 1
					#e.g: for every 3 right, go down 1... this checks for the "3 right"
					if self.counter == self.rise / self.run:
						#reset the counter... more efficient to use modulo?
						self.counter = 0
						if self.down:
							self.dx = 1 * self.speed
						else:
							self.dx = -1 * self.speed
					else:
						print "stuff"
						self.dx = 0

		location = self.getPosition()
		self.posX += self.dx
		self.posY += self.dy
		#if the sprite is within 10 pixels of its destination, just snap it to its destination
		if (location[0] < self.destinationX + 10 and location[0] > self.destinationX - 10) and (location[1] < self.destinationY + 10 and location[1] > self.destinationY - 10):
			self.correct()
		self.rect.center = (self.posX, self.posY)

	#for debugging purposes when i was developing this
	def printStats(self):
		print "Sprite center: " + str(self.rect.center)
		print "Sprite destination: " + str((self.destinationX, self.destinationY))
		print "dx: " + str(self.dx)
		print "dy: " + str(self.dy)

	def moveToLocation(self, destX, destY):
		self.movementQueue.append((destX, destY))
	 	self.printStats()
	def pause(self):
		self.paused = True

	def play(self):
		self.paused = False

	def correct(self):
		self.posX = self.destinationX
		self.posY = self.destinationY

	dx = 0
	dy = 0
	destinationX = 0
	destinationY = 0
	isShown = True
	speed = 0
	rise = 0
	run = 0
	counter = 0
	stopped = True
	right = False
	down = False

#createWindow: creates a window with the size, and the caption title
def createMainWindow(size, caption):
	myWin = pygame.display.set_mode(size)
	pygame.display.set_caption(caption)
	return myWin

#createBackground: creates a Surface for the window you presumably created with the background color of color
def createSurface(window, color):
	background = pygame.Surface(window.get_size())
	background.fill(color)
	background.convert()
	return background

#getClickLocation: returns the position of the cursor when the mouse was clicked
def getClickLocation(event):
	if event.type == pygame.MOUSEBUTTONDOWN:
		return event.pos
	else:
		return False

#mouseButtonDown: returns true if the mouse button was pushed down, else returns false
def mouseButtonDown(event):
	if event.type == pygame.MOUSEBUTTONDOWN:
		return True
	else:
		return False

#mouseButtonUp: returns true if the mouse button was released, else returns false
def mouseButtonUp(event):
	if event.type == pygame.MOUSEBUTTONUP:
		return True
	else:
		return False

#spriteClicked: returns true if clickLocation is touching sprite, else false.
#clickLocation is event.pos if the event is pygame.MOUSEBUTTONDOWN, clickLocation is a tuple of two values representing the x and y coords of the click
def spriteClicked(clickLocation, sprite):
	if sprite.rect.collidePoint(clickLocation):
		return True
	else:
		return False
#surfaceClicked: returns true if surface surface was clicked (clickLocation)
def surfaceClicked(clickLocation, surface, posX, posY):
	if (clickLocation[0] > posX) and (clickLocation[0] < posX + surface.get_width()) and (clickLocation[1] > posY) and (clickLocation[1] < posY + surface.get_height()):
		return True
	else:
		return False

#createButton: creates
def createButton(positionX, positionY, imageLocation):
	mySprite = stdSprite(posX, posY, imageLocation)
	return mySprite


def main():
	print "This is not a standalone program, import into your pygame program"

if __name__ == "__main__":
	main()
