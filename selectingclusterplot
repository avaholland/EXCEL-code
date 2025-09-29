import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
with fits.open("rcat_ngc6866_v0.fits") as hdu:
	data = hdu[1].data
	clusterdata = data['MEMBOOL']
	b = clusterdata < 1
	good = clusterdata == 1
	x1 = data['GAIAEDR3_BP'][good]
	x2 = data['GAIAEDR3_RP'][good]
	x = x1 - x2
	y = data['GAIAEDR3_G_CORRECTED'][good]
	scatter = plt.scatter(x, y)
	plt.xlabel("BP-RP")
	plt.ylabel("G")
	ax = scatter.axes
	ax.invert_yaxis()
	plt.show()
	y1 = data['GAIAEDR3_BP'][good]
	scatter = plt.scatter(x, y1)
	plt.xlabel("BP-RP")
	plt.ylabel("BP")
	ax = scatter.axes
	ax.invert_yaxis()
	plt.show()
	y2 = data['GAIAEDR3_RP'][good]
	scatter = plt.scatter(x, y2)
	plt.xlabel("BP-RP")
	plt.ylabel("RP")
	ax = scatter.axes
	ax.invert_yaxis()
	plt.show()


	

