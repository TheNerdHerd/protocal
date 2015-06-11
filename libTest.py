import joshPyLib
import pygame
pygame.init()

def main():
	screen = joshPyLib.createMainWindow((800, 600), "Hello world")
	background = joshPyLib.createSurface(screen, (255, 255, 255))

	#square = pygame.Surface((25, 25))
	#square.fill((0, 255, 0))
	#square.convert()

	#mySprite = joshPyLib.animatedSprite(200, 100, "back_button.png")
	#mySprite.show()

	#allSprites = pygame.sprite.Group(mySprite)

	mySurface = joshPyLib.superSurface(screen, 50, 50, 50, 50)
	mySurface.show()

	allSprites = pygame.sprite.Group(mySurface)

	keepGoing = True
	clock = pygame.time.Clock()
	while keepGoing:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				keepGoing = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				#mySprite.moveToLocation(50, 50)
				#mySprite.moveToLocation(100,100, 2)
				if joshPyLib.surfaceClicked(event.pos, mySurface.image, mySurface.posX, mySurface.posY):
					mySurface.resize(100, 100)
			#elif event.type == pygame.KEYDOWN:
				#mySprite.stop()
			#elif event.type == pygame.KEYUP:
				#mySprite.play()
		screen.blit(background, (0, 0))
		#screen.blit(square, (200, 200))

		allSprites.clear(screen, background)
		allSprites.update()
		#allSprites.draw(screen)

		pygame.display.flip()

if __name__ == "__main__":
	main()
	pygame.quit()
