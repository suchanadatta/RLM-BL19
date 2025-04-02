import numpy as np
import matplotlib.pyplot as plt

input_file = '/home/suchana/PycharmProjects/victeur/data/nonfic_heatmap_data.csv'
corr_matrix = np.around(np.genfromtxt(input_file, delimiter=',', dtype=np.float32), 3)
# corr_matrix = np.flipud(corr_matrix)
corr_matrix = corr_matrix.T
print(corr_matrix)

topics = ['immigrant', 'emigrant', 'foreign', 'newcomer', 'alien', 'enslaved', 'colony', 'vampire',
          'engagement', 'proposal', 'wedding', 'suitor', 'lover', 'betrothal', 'eligible', 'consent',
          'love', 'mesalliance', 'heiress', 'eviction', 'crime', 'murder', 'mystery', 'villain', 'adventure']
decade = ['1831-40', '1841-50', '1851-60', '1861-70', '1871-80', '1881-90', '1891-99']

fig, ax = plt.subplots()
im = ax.imshow(corr_matrix, cmap='cividis')

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(topics)), labels=topics, fontsize=18)
ax.set_yticks(np.arange(len(decade)), labels=decade, fontsize=18)
# ax.set_yticklabels([])
# ax.set_xticklabels([])

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(decade)):
    for j in range(len(topics)):
        text = ax.text(j, i, corr_matrix[i, j], ha="center", va="center", color="w", fontsize=12)

# ax.set_title("Correlation b/w QPP Scores")
fig.tight_layout()

# Add a colorbar to indicate the scale
# cbar = plt.colorbar(im)
im_ratio = 7/25
level_min, level_max = np.min(corr_matrix), np.max(corr_matrix)
# level_min, level_max = np.float32(-0.16), np.float32(0.256)
cb = plt.colorbar(im, fraction=0.047 * im_ratio, ticks=np.linspace(level_min, level_max, 5))
cb.ax.tick_params(labelsize=10)
cb.set_label('Correlation Coefficient', fontsize=12)  # Label for the colorbar

plt.savefig('fic_heatmap.pdf', dpi=300, bbox_inches='tight')

plt.show()