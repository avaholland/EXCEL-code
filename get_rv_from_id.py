import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
with fits.open("rcat_ngc6866_v0.fits") as hdu:
	data = hdu[1].data
	ids = data['GAIAEDR3_ID']
	print(ids)