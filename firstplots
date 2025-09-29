#import pathlib
#import tarfile
import matplotlib.pyplot as plt
#from glob import glob
#import os
import numpy as np
from astropy.io import fits
#with fits.open("rcat_ngc6866_v0.fits") as hdu:
	#print(hdu.info())
	#print(hdu[1].data.dtype.names)
	#data = hdu[1].data
	#print(data[1])
	#plt.savefig('G_vs_P-RP.png')
with fits.open("rcat_ngc6866_v0.fits") as hdu:
	data = hdu[1].data
	x1data = data['GAIAEDR3_BP']
	x2data = data['GAIAEDR3_RP']
	xdata = x1data - x2data
	ydata = data['GAIAEDR3_RP']
	plt.scatter(xdata, ydata)
	plt.xlabel("BP-RP")
	plt.ylabel("RP")
	plt.show()






	


