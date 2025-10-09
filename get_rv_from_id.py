import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
with fits.open("rcat_ngc6866_v0.fits") as hdu:
	data = hdu[1].data
	star_id = input("Enter a star ID:")
	ids = data["GAIAEDR3_ID"]
	rvs = data["vrad"]
	dates = data["DATE-OBS"]
	match = ids == star_id
	star_rvs = rvs[match]
	star_date = dates[match]
	print(ids[match])
	fig, ax = plt.subplots()
	ax.scatter(star_date, star_rvs, s=10, c='blue', alpha=0.8,)
	ax.set_xlabel("Time")
	ax.set_ylabel("RV")
	plt.show()
