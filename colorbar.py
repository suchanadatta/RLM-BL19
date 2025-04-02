import numpy as np
import matplotlib.pyplot as plt

# setup some generic data 
N = 37
x, y = np.mgrid[:N, :N]
Z = (np.cos(x * 0.2) + np.sin(y * 0.3))

# mask out the negative and positive values 
Zpositive = np.ma.masked_less(Z, 0)
Znegative = np.ma.masked_greater(Z, 0)

fig, (ax1, ax2, ax3) = plt.subplots(figsize=(13, 3),
                                    ncols=3)

# plot just the positive data and save the 
# color "mappable" object returned by ax1.imshow 
pos = ax1.imshow(Zpositive, cmap='Blues')

# add the colorbar using the figure's method, 
fig.colorbar(pos, ax=ax1)

# repeat everything above for the negative data 
neg = ax2.imshow(Znegative, cmap='Reds_r')
fig.colorbar(neg, ax=ax2)

# Plot both positive and negative values between +/- 1.2 
pos_neg_clipped = ax3.imshow(Z, cmap='RdBu',
                             vmin=-1.2,
                             vmax=1.2)

# Add minorticks on the colorbar to make  
# it easy to read the values off the colorbar. 
color_bar = fig.colorbar(pos_neg_clipped,
                         ax=ax3,
                         extend='both')

color_bar.minorticks_on()
plt.show() 