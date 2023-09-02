import pandas as pd
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

file_dir = 'data/' #Which folder the data in
img_name = 'pdi_pi_collapsed.fits' #fits format is used to collect astronomical data
img = fits.getdata(file_dir+img_name,ext=1)#Pull data from fits. ext=1 index based 1st extention
#fits data can be read directly by using .getdata
# create a figure
fig = plt.figure(figsize=(8,8))
#plot in the figure
image = plt.imshow(img, origin = 'lower', vmin=-0.001, vmax=0.08)
cbar = fig.colorbar(image,shrink=0.82) #creates a side bar
cbar.set_label('Surface Brightness (arb. units)', rotation=90,fontsize=12)
plt.xlim([60,140])
plt.ylim([60,140])
plt.xlabel(r'$\Delta$ RA [px]',fontsize=12)
plt.ylabel(r'$\Delta$ Dec [px]',fontsize=12)
plt.show()


# Reading 20,000 Rows*97 columns of Data- Closest 20k stars from Gaia Archive (DR2)
stellar=pd.read_csv('closest20kstars.csv')

# Creating a matplotlib (pyplot) figure
fig = plt.figure(figsize = [10,10])

# Plotting the scatter graph with RA on x-axis and Dec on y-axis. alpha tells the opacity, s is the size
plt.scatter(stellar['ra'], stellar['dec'], alpha=0.8, s=12, lw = 0.5, ec = 'k', color='darkorchid')
# Adding labels and a title for the figure
plt.xlim([0,362])
plt.ylim([-75,75])
plt.xlabel('RA [$\degree$]', fontsize = 14)
plt.ylabel('Dec [$\degree$]', fontsize = 14)
plt.title('Closest Stars 20,000 stars from Gaia Archive (DR2)', fontsize = 16)

plt.show()
