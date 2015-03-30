#import and initialize pygame
import pygame
pygame.init()
#classes
#stdsprite: a basic sprite used in the createButton function
class stdSprite(pygame.sprite.Sprite):
	def __init__(self, posX, posY, imageLocation):
		pygame.sprite.Sprite.init()
		self.posX = posX
		self.posY = posY
		self.image = pygame.image.load(imageLocation)
	def update(self):
		self.rect.center = (self.posX, self.posY)

	posX = 0
	posY = 0


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

def createButton			

def main():
	print "This is not a standalone program, import into your pygame program"

if __name__ == "__main__":
	main()  