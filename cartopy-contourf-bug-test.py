import pickle
import PyQt6.QtCore
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import xarray as xr
import pandas as pd

proj0 = ccrs.PlateCarree( central_longitude=0 )

x = np.fromfile('x.dat' )
y = np.fromfile('y.dat' )
v = np.fromfile('v.dat' )

shape = ( 61,240 )

x = x.reshape( shape )
y = y.reshape( shape )
v = v.reshape( shape )

levels = [-4.0, -2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 4.0]

### contourf wrong ###### 
ax = plt.subplot( 2, 2, 1, projection=proj0 )
cs = ax.contourf( x, y, v,
                  levels=levels,
                  extend='both',
                  transform_first=False
                  )
plt.colorbar( cs )
ax.set_title('PlateCarree + extend both' )
###########################


ax = plt.subplot( 2, 2, 2, projection=proj0 )
cs = ax.contourf( x, y, v,
                  levels=levels,
                  extend='min',
                  transform_first=False
                  )
plt.colorbar( cs )
ax.set_title('PlateCarree + extend min' )


ax = plt.subplot( 2, 2,3, projection=proj0 )
cs = ax.contourf( x, y, v,
                  levels=levels,
                  extend='both',
                  transform_first=True
                  )
plt.colorbar( cs )
ax.set_title('PlateCarree + transform_first' )

ax = plt.subplot( 2, 2, 4 )
cs = ax.contourf( x, y, v,
                  levels=levels,
                  extend='both',
                  )
plt.colorbar( cs )
ax.set_title('Axes' )

plt.show()


    
