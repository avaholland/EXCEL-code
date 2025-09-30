import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
with fits.open("rcat_ngc6866_v0.fits") as hdu:
	data = hdu[1].data
	clusterdata = data['MEMBOOL']
	cluster = clusterdata == 1
	not_cluster = clusterdata == 0
	parallax_cluster = data['GAIAEDR3_PARALLAX_CORRECTED'][cluster]
	parallax_not_cluster = data['GAIAEDR3_PARALLAX_CORRECTED'][not_cluster]
	dec_cluster = data['GAIAEDR3_PMDEC'][cluster]
	dec_not_cluster = data['GAIAEDR3_PMDEC'][not_cluster]
	ra_cluster = data['GAIAEDR3_PMRA'][cluster]
	ra_not_cluster = data['GAIAEDR3_PMRA'][not_cluster]

	fig1, ax1 = plt.subplots()
	ax1.scatter(dec_cluster, parallax_cluster, s=15, c="blue", alpha=0.8, label="Cluster members")
	ax1.scatter(dec_not_cluster, parallax_not_cluster, s=10, c="lightgrey", alpha=0.5, label="Non-members")
	margin_factor = 0.5
	x_min, x_max = np.min(dec_cluster), np.max(dec_cluster)
	y_min, y_max = np.min(parallax_cluster), np.max(parallax_cluster)
	x_range = x_max - x_min
	y_range = y_max - y_min
	ax1.set_xlim(x_min - margin_factor * x_range, x_max + margin_factor * x_range)
	ax1.set_ylim(y_min - margin_factor * y_range, y_max + margin_factor * y_range)
	ax1.set_xlabel("Proper motion in DEC")
	ax1.set_ylabel("Parallax")
	ax1.set_title("Parallax vs Proper motion in DEC")
	ax1.legend()
	plt.show()

	fig2, ax2 = plt.subplots()
	ax2.scatter(ra_cluster, parallax_cluster, s=15, c="blue", alpha=0.8, label="Cluster members")
	ax2.scatter(ra_not_cluster, parallax_not_cluster, s=10, c="lightgrey", alpha=0.5, label="Non-members")
	x_min, x_max = np.min(ra_cluster), np.max(ra_cluster)
	y_min, y_max = np.min(parallax_cluster), np.max(parallax_cluster)
	x_range = x_max - x_min
	y_range = y_max - y_min
	ax2.set_xlim(x_min - margin_factor * x_range, x_max + margin_factor * x_range)
	ax2.set_ylim(y_min - margin_factor * y_range, y_max + margin_factor * y_range)
	ax2.set_xlabel("Proper motion in RA")
	ax2.set_ylabel("Parallax")
	ax2.set_title("Parallax vs Proper motion in RA")
	ax2.legend()
	plt.show()

