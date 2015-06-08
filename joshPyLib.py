#TODO
#in animation sprite....
#can one use decimals to command a location?
#if the sprite stops with stop(), later commands are messed up

#import and initialize pygame
from fractions import gcd
from collections import deque
import pygame
pygame.init()

#stdsprite: a basic sprite used in the createButton function
#a stdsprite is represented by one image, and is drawn to (posX, posY)... very basic
#you will have to inherit this if create a sprite based off of this
#a sprite is always hidden when first created, use show() to display it
class stdSprite(pygame.sprite.Sprite):
	def __init__(self, posX, posY, imageLocation=0):
		pygame.sprite.Sprite.__init__(self)
		self.posX = posX
		self.posY = posY
		self.image = pygame.image.load(imageLocation)
		self.rect = self.image.get_rect()
		self.shown = False
		self.posX = posX
		self.posY = posY

	def show(self):
		self.shown = True

	def hide(self):
		self.shown = False

	def update(self):
		if shown:
			self.rect.center = (self.posX, self.posY)
		else: 
			self.rect.center = (-1000, -1000)

	def getPosition(self):
		return (self.posX, self.posY)

	def toggleVisibility(self):
		if self.shown:
			self.hide()
		else:
			self.show()

	posX = -1000
	posY = -1000
	shown = True

#animatedSprite: provides a sprite whose purpose is moving about programatically, inherits from stdSprite
class animatedSprite(stdSprite):
	def __init__(self, posX, posY, imageLocation, speed = 1):
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
		if self.stopped and self.movementQueue:
			temp = self.movementQueue.popleft()
			self.destinationX = temp[0]
			self.destinationY = temp[1]
			self.rise = self.destinationY - self.posY
			self.run = self.destinationX - self.posX
			self.speed = temp[2]
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
						self.posX += self.speed
					else:
						self.posX -= self.speed
					#increment the counter
					self.counter += 1
					#e.g: for every 3 right, go up 1... this checks for the "3 right"
					if self.counter == self.run / self.rise:
						#reset the counter... more efficient to use modulo?
						self.counter = 0
						if self.down:
							self.posY += self.speed
						else:
							self.posY -= self.speed

			#if rise and run is equal
			elif self.run == self.rise:
				#if the sprite needs to go down or up
				if self.rise != 0:
					if self.right:
						self.posX += self.speed
					else: 
						self.posX -= self.speed
					if self.down:
						self.posY += self.speed
					else: 
						self.posY -= self.speed

			#if the sprite's run is greater than its rise
			elif abs(self.rise) > abs(self.run):
				#if the sprite has to go up and that it is moving
				if abs(self.run) > 0 and self.stopped == False:
					#This sets DX based on if it has to go right
					if self.right:
						self.posY += self.speed
					else:
						self.posY -= self.speed
					#increment the counter
					self.counter += 1
					#e.g: for every 3 right, go down 1... this checks for the "3 right"
					if self.counter == self.rise / self.run:
						#reset the counter... more efficient to use modulo?
						self.counter = 0
						if self.down:
							self.posX += self.speed
						else:
							self.posX -= self.speed
		
		#this is temporary, fix this later
		#if the sprite is within 5 pixels of its destination, just snap it to its destination
		if (self.posX < self.destinationX + 5 and self.posX > self.destinationX - 5) and (self.posY < self.destinationY + 5 and self.posY > self.destinationY - 5):
			self.correct()	
			self.stopped = True
		if self.shown:
			self.rect.center = (self.posX, self.posY)
		else: 
			self.rect.center = (-1000, -1000)

	#for debugging purposes when i was developing this
	def printStats(self):
		print "Sprite center: " + str(self.rect.center)
		print "Sprite destination: " + str((self.destinationX, self.destinationY))

	def moveToLocation(self, destX, destY, speed=1):
		if self.speed > 0:
			self.movementQueue.append((destX, destY, speed))
	 		self.printStats()
	 	else:
	 		return

	def pause(self):
		self.paused = True

	def play(self):
		self.paused = False

	#def stop(self):
	#	self.destinationX = self.posX
	#	self.destinationY = self.posY
	#	self.stopped = True

	def correct(self):
		self.posX = self.destinationX
		self.posY = self.destinationY

	destinationX = 0
	destinationY = 0
	speed = 0
	rise = 0
	run = 0
	counter = 0
	stopped = True
	right = False
	down = False

#a jacked up pygame.Surface object
class superSurface(stdSprite):
	def __init__(self, screen, length, width, posX, posY):
		pygame.sprite.Sprite.__init__(self)
		#stdSprite.__init__(self)
		self.image = pygame.Surface((length, width))
		self.screen = screen
		self.length = length
		self.width = width
		self.posX = posX
		self.posY = posY
		self.rect = self.image.get_rect()
		self.centerX = posX + (0.5 * self.length)
		self.centerY = posY + (0.5 * self.width)

	def update(self):
		self.screen.blit(self.image, (self.centerX - (0.5 * self.length), self.centerY - (0.5 * self.width)))

	#TODO: implement function overloading to determine the type of resize
	def resize(self, length, width):
		self.image = pygame.Surface((length, width))
		self.length = length
		self.width = width
		self.rect = self.image.get_rect()

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