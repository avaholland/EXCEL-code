import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
with fits.open("rcat_ngc6866_v0.fits") as hdu:
	data = hdu[1].data
	clusterdata = data['MEMBOOL']
	good = clusterdata == 1
	column_names = data.columns.names
	print(column_names)
