from ezgraphics import GraphicsWindow

win = GraphicsWindow(400, 400)

canvas = win.canvas()

canvas.setColor("Blue")
canvas.drawOval(20,20,50,50)

canvas.setColor("Red")
canvas.drawOval(120,20,50,50)

canvas.setColor("yellow")
canvas.drawOval(220,40,50,50)

canvas.setColor("green")
canvas.drawOval(320,60,50,70)

win.wait()