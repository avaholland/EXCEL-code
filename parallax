import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
with fits.open("rcat_ngc6866_v0.fits") as hdu:
	data = hdu[1].data
	clusterdata = data['MEMBOOL']
	good = clusterdata == 1
	distancearc = data['GAIAEDR3_PARALLAX_CORRECTED']
	distance = 1 / distancearc
	MAG1 = data['GAIAEDR3_G']
	mag1 = -5 + (5 * np.log10(distance)) + MAG1
	x1 = data['GAIAEDR3_BP'][good]
	x2 = data['GAIAEDR3_RP'][good]
	x = x1 - x2
	y = mag1[good]
	scatter = plt.scatter(x, y)
	plt.xlabel("BP-RP")
	plt.ylabel("G")
	ax = scatter.axes
	ax.invert_yaxis()
	plt.show()

