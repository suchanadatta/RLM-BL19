import sys
import xml.etree.ElementTree as ET
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import gensim
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print('Needs 1 arguments - \n1. word2vec file (.txt)\n')
    exit(0)

arg_w2v_file = sys.argv[1]

fw_NN_terms = open('/store/victeur/jcdl-24/wordvecs/1841.NN', 'w')

original_query = 'Immigrant'
qterm_NN_dict = {}

stemmer = PorterStemmer()
original_query = stemmer.stem(original_query)

model = gensim.models.KeyedVectors.load_word2vec_format(arg_w2v_file, binary=False)
# vec = model.wv[original_query]
vector = model.most_similar(positive=[original_query], topn=20)
qterm_NN_dict[original_query] = vector
print(vector)
nn_list = []
for nn_term in vector:
    nn_list.append(nn_term[0])
qterm_NN_dict[original_query] = nn_list
print('dictionary ready...')

for key in qterm_NN_dict:
    fw_NN_terms.writelines(str(key) + '\t')
    for nn in qterm_NN_dict[key]:
        fw_NN_terms.writelines(str(nn) + ',')
    fw_NN_terms.write('\n')


def tsne_plot(model):
    "Creates and TSNE model and plots it"
    labels = []
    tokens = []
    NN = ['immigr', 'duffil', 'jubeaiz', 'nudricar', 'archavai', 'velaria', 'rafl', 'erti',
          'enpland', 'splendidifer', 'howmuch', 'questioningli', 'nugc', 'unthatch', 'aefair', 'duril']

    # for word in model.wv.vocab:
    for nn in NN:
        tokens.append(model[nn])
        print(len(tokens))
        labels.append(nn)

    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)

    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])

    plt.figure(figsize=(50, 50))
    plt.rcParams.update({'font.size': 22})
    for i in range(len(x)):
        plt.scatter(x[i], y[i])
        plt.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.show()

tsne_plot(model)


