from turtle import *

color('red', 'green')
begin_fill()
while True:
  forward(1000)
  left(90)
  if abs(pos()) < 1:
    break

end_fill()
done()

# draw_triangle(-80, -50, 160, 'forest green')
# draw_triangle(-60, 30, 120, 'dark green')