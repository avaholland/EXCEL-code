import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
with fits.open("rcat_ngc6866_v0.fits") as hdu:
	data = hdu[1].data
	clusterdata = data['MEMBOOL']
	cluster = clusterdata == 1
	not_cluster = clusterdata == 0
	#id = data['GAIADR3_ID']
	rv_cluster = data['vrad'][cluster]
	rv_not_cluster = data['vrad'][not_cluster]
	rverror = data['vrad_err']
	rverror_cluster = data['vrad_err'][cluster]
	rverror_not_cluster = data['vrad_err'][not_cluster]
	Teff_cluster = data['Teff'][cluster]
	Teff_not_cluster = data['Teff'][not_cluster]
	fix, ax = plt.subplots()
	ax.scatter(Teff_not_cluster, rv_not_cluster, s=10, c='lightgrey', alpha=0.3, label='Non-members')
	ax.scatter(Teff_cluster, rv_cluster, s=10, c='blue', alpha=0.8, label='Cluster members')
	plt.errorbar(Teff_cluster, rv_cluster, yerr=rverror_cluster, fmt='none', zorder = 1, color = 'blue')
	#plt.errorbar(x, y, xerr=rverror_notcluster, fmt='none', zorder = -1, color = 'lightgrey')
	ax.set_xlabel('T')
	margin_factor = 0.1
	x_min, x_max = np.min(Teff_cluster), np.max(Teff_cluster)
	y_min, y_max = np.min(rv_cluster), np.max(rv_cluster)
	x_range = x_max - x_min
	y_range = y_max - y_min
	#ax.set_xlim(4000, 9000)
	#ax.set_xlim(x_min - margin_factor * x_range, x_max + margin_factor * x_range)
	#ax.set_ylim(y_min - margin_factor * y_range, y_max + margin_factor * y_range)
	ax.set_ylabel('RV')
	ax.legend()
	plt.show()





