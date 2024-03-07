from ezgraphics import GraphicsWindow

win = GraphicsWindow(1200, 1200)
canvas = win.canvas()

canvas.setColor("yellow")
canvas.drawOval(20,20,200,200)

canvas.setColor("yellow")
canvas.drawOval(20,220,200,200)

canvas.setColor("yellow")
canvas.drawOval(20,420,200,200)

win.wait()