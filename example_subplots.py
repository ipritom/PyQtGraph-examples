import pyqtgraph as pg
import numpy as np

################################
# data - that will be visualized
################################
t = np.arange(0,5,0.01) # x-axis
# sine wave 
y1 = np.sin(2*np.pi*2*t) # y-ax
# cosinse wave 
y2 = np.cos(2*np.pi*2*t) # y-ax

#################################
# Plotting
#################################
#creating a window with a title
win = pg.GraphicsLayoutWidget(show=True, title="Trigonometric Functions")
# subplot 1
p1 = win.addPlot(x=t, y=y1, title='Sine Wave', row=0, col=0) # row, col for adjusting subplot position
# subplot 2
p2 = win.addPlot(x=t, y=y2, title='Cosine Wave',row=1, col=0) # row, col for adjusting subplot position
# showing plots
pg.mkQApp().exec_()
win.clear()

