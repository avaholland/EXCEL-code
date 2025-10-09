import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
with fits.open("rcat_ngc6866_v0.fits") as hdu:
	data = hdu[1].data
	ids = data["GAIAEDR3_ID"]
	rvs = data["vrad"]
	period = data["Teff"]
	mask = ~np.isnan(rvs)
	valid_ids = ids[mask]
	unique_valid_ids = np.unique(valid_ids)

	print(f"Total rows with valid RVs: {mask.sum()}")
	print(f"Unique stars with RVs: {len(unique_valid_ids)}")
	print("Example IDs:", unique_valid_ids[:10])