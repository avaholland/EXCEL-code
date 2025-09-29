import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
with fits.open("rcat_ngc6866_v0.fits") as hdu:
	data = hdu[1].data
	clusterdata = data['MEMBOOL']
	cluster = clusterdata == 1
	not_cluster = clusterdata == 0
	x_cluster = data['GAIAEDR3_PMRA'][cluster]
	y_cluster = data['GAIAEDR3_PMDEC'][cluster]
	x_not_cluster = data['GAIAEDR3_PMRA'][not_cluster]
	y_not_cluster = data['GAIAEDR3_PMDEC'][not_cluster]
	fig, ax = plt.subplots()
	ax.scatter(x_not_cluster, y_not_cluster, s=10, c="lightgrey", alpha=0.5, label="Non-members")
	ax.scatter(x_cluster, y_cluster, s=15, c="blue", alpha=0.8, label="Cluster members")
	
	margin_factor = 0.5
	x_min, x_max = np.min(x_cluster), np.max(x_cluster)
	y_min, y_max = np.min(y_cluster), np.max(y_cluster)
	x_range = x_max - x_min
	y_range = y_max - y_min
	ax.set_xlim(x_min - margin_factor * x_range, x_max + margin_factor * x_range)
	ax.set_ylim(y_min - margin_factor * y_range, y_max + margin_factor * y_range)

	ax.set_xlabel("Proper motion in RA")
	ax.set_ylabel("Proper motion in Dec")
	ax.set_title("Proper motions")
	ax.legend()
	plt.show()

	#scatter = plt.scatter(x, y)
	#plt.xlabel("Proper motion in RA")
	#plt.ylabel("Proper motion in DEC")
	#ax = scatter.axes
	#plt.show()


