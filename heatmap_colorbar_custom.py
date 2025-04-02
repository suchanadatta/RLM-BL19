import sys
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description='Generate a heatmap from a correlation matrix.')
parser.add_argument('--input', type=str, help='The CSV file containing the correlation matrix.', required=True)
parser.add_argument('--r1', type=str, help='The retrieval 1 - pre/post.', required=True)
parser.add_argument('--r2', type=str, help='The retrieval 2 - pre/post.', required=True)
parser.add_argument('--y', action='store_true', default=False, help='Display y-axis labels (default: True).')
parser.add_argument('--colorbar', action='store_true', default=False, help='Displa  y intensity scale (default: True).')


args = parser.parse_args()
input_file = args.input

retrieval1 = args.r1 # pre/post
retrieval2 = args.r2 # pre/post

#input_file = sys.argv[1] if len(sys.argv) > 1 else ""
#if not input_file:
#    print("Usage: python3 heatmap.py <.csv file path>")
#    sys.exit(0)

#input_file = 'pre_post_pearsons_DL.csv'
corr_matrix = np.around(np.genfromtxt(input_file, delimiter=',', dtype=np.float32), 2)
#print(corr_matrix)

qpp_preret = ['MaxIDF', 'AvgIDF', 'SumSCQ', 'MaxSCQ', 'AvgSCQ', 'SumVAR',
              'AvgVAR', 'MaxVAR', 'AvP', 'AvNP']
qpp_postret = ['NQC', 'WIG', 'Clarity', 'UEF-NQC', 'UEF-WIG', 'UEF-Clarity',
              'NeuralQPP', 'qppBERT-PL', 'Deep-QPP', 'BERT-QPP']

x_list = qpp_preret
y_list = qpp_preret

if retrieval1.lower() == "post":
    x_list = qpp_postret

if retrieval2.lower() == "post":
    y_list = qpp_postret

min_correlation = -0.2


fig, ax = plt.subplots()
im = ax.imshow(corr_matrix, cmap='cividis', vmin=min_correlation)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(x_list)), labels=x_list, fontsize=16)
ax.set_yticks(np.arange(len(y_list)), labels=y_list, fontsize=16)
#ax.set_yticklabels([])
if not args.y:
    ax.set_yticklabels([])  # Remove y-axis labels if the parameter is False

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(x_list)):
    for j in range(len(y_list)):
        text = ax.text(j, i, corr_matrix[i, j], ha="center", va="center", color="w")

# ax.set_title("Correlation b/w QPP Scores")
fig.tight_layout()

# Add a colorbar to indicate the scale
# Display colorbar if the parameter is True
print(args.colorbar)
if args.colorbar:
    print("Here")
    cbar = plt.colorbar(im)
    cbar.set_label('Correlation Coefficient')  # Label for the colorbar

output_file = "".join(input_file.split(".")[0:len(input_file.split("."))-1])+".pdf"
plt.savefig(output_file, dpi=300, bbox_inches='tight')
subprocess.run(['pdfcrop', output_file, output_file])

#plt.show()
