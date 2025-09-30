import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
with fits.open("rcat_ngc6866_v0.fits") as hdu:
	data = hdu[1].data
	x1data = data['GAIAEDR3_BP']
	x2data = data['GAIAEDR3_RP']
	xdata = x1data - x2data
	ydata = data['GAIAEDR3_RP']
	scatter = plt.scatter(xdata, ydata)
	plt.xlabel("BP-RP")
	plt.ylabel("RP")
	ax = scatter.axes
	ax.invert_yaxis()
	plt.show()
	xdata = x1data - x2data
	ydata1 = data['GAIAEDR3_G_CORRECTED']
	scatter = plt.scatter(xdata, ydata)
	plt.xlabel("BP-RP")
	plt.ylabel("G")
	ax = scatter.axes
	ax.invert_yaxis()
	plt.show()
	ydata2 = data['GAIAEDR3_BP']
	scatter = plt.scatter(xdata, ydata)
	plt.xlabel("BP-RP")
	plt.ylabel("BP")
	ax = scatter.axes
	ax.invert_yaxis()
	plt.show()
