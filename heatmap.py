import numpy as np
import matplotlib.pyplot as plt

input_file = '/home/suchana/NetBeansProjects/QPPScores/correlation/pre_post_pearsons_DL.csv'
corr_matrix = np.around(np.genfromtxt(input_file, delimiter=',', dtype=np.float32), 2)
print(corr_matrix)

qpp_preret = ['MaxIDF', 'AvgIDF', 'SumSCQ', 'MaxSCQ', 'AvgSCQ', 'SumVAR',
              'AvgVAR', 'MaxVAR', 'AvP', 'AvNP']
qpp_postret = ['NQC', 'WIG', 'Clarity', 'UEF-NQC', 'UEF-WIG', 'UEF-Clarity',
              'NeuralQPP', 'qppBERT-PL', 'Deep-QPP', 'BERT-QPP']

fig, ax = plt.subplots()
im = ax.imshow(corr_matrix, cmap='cividis')

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(qpp_postret)), labels=qpp_postret, fontsize=16)
ax.set_yticks(np.arange(len(qpp_preret)), labels=qpp_preret, fontsize=16)
ax.set_yticklabels([])

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(qpp_preret)):
    for j in range(len(qpp_postret)):
        text = ax.text(j, i, corr_matrix[i, j], ha="center", va="center", color="w")

# ax.set_title("Correlation b/w QPP Scores")
fig.tight_layout()

# Add a colorbar to indicate the scale
cbar = plt.colorbar(im)
cbar.set_label('Correlation Coefficient')  # Label for the colorbar

plt.savefig('dl_pre_post.pdf', dpi=300, bbox_inches='tight')

plt.show()