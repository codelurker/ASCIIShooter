def draw_circle(at,size):
	Circle = 0
	width=size
	height=size
	CenterX=(width/2)
	CenterY=(height/2)
	circle = []

	for i in range(height):
		for j in range(width+1):
			Circle = (((i-CenterY)*(i-CenterY))/((float(height)/2)*(float(height)/2)))+((((j-CenterX)*(j-CenterX))/((float(width)/2)*(float(width)/2))));
			if Circle>0 and Circle<1.1:
				circle.append((at[0]+(j-(width/2)),at[1]+(i-(height/2))))
	
	return circle