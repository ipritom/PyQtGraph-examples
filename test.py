import pyqtgraph as pg
import numpy as np

# data - that will be visualized
t = np.arange(0,5,0.01) # x-axis
y = np.sin(2*np.pi*2*t) # y-ax

pg.plot(t, y)  # plot x vs y in red

pg.mkQApp().exec_()

