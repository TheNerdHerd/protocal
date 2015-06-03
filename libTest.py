import joshPyLib
import pygame
pygame.init()

def main():
	screen = joshPyLib.createMainWindow((800, 600), "Hello world")
	background = joshPyLib.createSurface(screen, (255, 255, 255))

	square = pygame.Surface((25, 25))
	square.fill((0, 255, 0))
	square.convert()

	mySprite = joshPyLib.animatedSprite(screen, background, 50, 50, "back_button.png")

	allSprites = pygame.sprite.Group(mySprite)

	keepGoing = True
	clock = pygame.time.Clock()
	while keepGoing:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				keepGoing = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mySprite.moveToLocation(100, 200)
				mySprite.moveToLocation(200, 400, 2)
				#mySprite.printStats()
				#mySprite.hide()
			#elif event.type == pygame.MOUSEBUTTONUP:
				#mySprite.show()
				#mySprite.stopMoving()
			elif event.type == pygame.KEYDOWN:
				mySprite.pause()
			elif event.type == pygame.KEYUP:
				mySprite.play()
		screen.blit(background, (0, 0))
		screen.blit(square, (200, 200))
		
		allSprites.clear(screen, background)
		allSprites.update()
		allSprites.draw(screen)
		
		pygame.display.flip()

if __name__ == "__main__":
	main()
	pygame.quit()