import pygame
from math import sqrt,sin,cos,radians
import sys

WIDTH = 400
HEIGHT = 400

pygame.init()

window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

# text = pygame.font.Font(None, 20)
# text_surface = text.render('Distance',False, 'yellow')
# text_surface_rectangle = text_surface.get_rect(center = (200,200))

#Line surface

angle = 0
count = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	def green_arrow():

		if event.type == pygame.MOUSEMOTION:


			def quadrant_checker(position):
				x = position[0]
				y = position[1]

				if x > 200 and y < 200:
					return 'FIRST Quadrant - I'
				elif x < 200 and y < 200:
					return 'SECOND Quadrant - II'
				elif x < 200 and y > 200:
					return 'THIRD Quadrant - III'
				elif x > 200 and y > 200:
					return 'FOURTH Quadrant - IV'
				else:
					return "Maybe GOD knows and we don't"

			mouse_pos_x = pygame.mouse.get_pos()[0]
			mouse_pos_y = pygame.mouse.get_pos()[1]

			#print(mouse_pos_x,mouse_pos_y)

			midpoint = ((mouse_pos_x + 200)/2,(mouse_pos_y + 200)/2)

			mouse_pos = pygame.mouse.get_pos()
			pygame.draw.line(window,'green',(200,200), mouse_pos)
			pygame.draw.circle(window, 'blue', mouse_pos, 5)
			text = pygame.font.Font(None, 20)
			text_surface = text.render('{}'.format(quadrant_checker(mouse_pos)),True, 'yellow')
			text_surface_rectangle = text_surface.get_rect(center = midpoint)

			window.blit(text_surface, text_surface_rectangle)

	window.fill((0,0,0))

	
	x_value = cos(radians(angle))
	y_value = sin(radians(angle))

	pos_x = 100 * x_value 
	pos_y = 100 * y_value

	#change angle by 1
	angle -= 1

	pygame.draw.circle(window, 'red',(200,200), 10)
	pygame.draw.circle(window, 'red', (200,200), 100,2)
	pygame.draw.circle(window, 'green', (pos_x + 200,pos_y + 200), 10)
	pygame.draw.line(window,'blue',(200,200),((pos_x + 200,pos_y + 200)))
	label_surface = pygame.font.Font(None,20)
	label_surface_render = label_surface.render("x:: {}  ,y:: {}  . Angle: {}".format(round(x_value,5),round(y_value,5),angle * -1), True, 'green')
	revolutions_surface =pygame.font.Font(None,20)
	revolutions_surface_render = label_surface.render("Revolutions: {}".format(count), True, 'white')


	angle_details = pygame.font.Font(None, 20)
	angle_details_render = angle_details.render('Angle:{} Degrees'.format(angle * -1), True, 'yellow')
	angle_details_rectangle = angle_details_render.get_rect(midleft = (pos_x + 210,pos_y + 200))

	#Count Number of revolutions
	if angle <= -360:
		angle = 0
		count += 1

	window.blit(angle_details_render,angle_details_rectangle)
	window.blit(label_surface_render, (5,5))
	window.blit(revolutions_surface_render, (5,20))
	green_arrow()

	pygame.display.update()

	clock.tick(60)


