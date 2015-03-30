import joshPyLib
import pygame
pygame.init()

def main():
	screen = joshPyLib.createMainWindow((800, 600), "Hello world")
	background = joshPyLib.createSurface(screen, (255, 255, 255))

	square = pygame.Surface((25, 25))
	square.fill((0, 255, 0))
	square.convert()

	keepGoing = True
	clock = pygame.time.Clock()
	while keepGoing:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				keepGoing = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if joshPyLib.surfaceClicked(joshPyLib.getClickLocation(event), square, 50, 50):
					print "square clicked"
				else:
					print "Nothing clicked"
		screen.blit(background, (0, 0))
		screen.blit(square, (50, 50))

		pygame.display.flip()

if __name__ == "__main__":
	main()
	pygame.quit()