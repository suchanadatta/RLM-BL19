import argparse
import os
import math
import collections
import itertools
import numpy as np
from scipy.spatial import distance

def jenson_shanon(list1, list2):
    return distance.jensenshannon(list1, list2)


def print_js_matrix(list):
    print(list[0], '\t', list[1], '\t', list[2], '\t', list[3], '\t', list[4], '\t', list[5], '\t', list[6], '\t', list[7])
    print(list[8], '\t', list[9], '\t', list[10], '\t', list[11], '\t', list[12], '\t', list[13], '\t', list[14], '\t', list[15])
    print(list[16], '\t', list[17], '\t', list[18], '\t', list[19], '\t', list[20], '\t', list[21], '\t', list[22], '\t', list[23])
    print(list[24], '\t', list[25], '\t', list[26], '\t', list[27], '\t', list[28], '\t', list[29], '\t', list[30], '\t', list[31])
    print(list[32], '\t', list[33], '\t', list[34], '\t', list[35], '\t', list[36], '\t', list[37], '\t', list[38], '\t', list[39])
    print(list[40], '\t', list[41], '\t', list[42], '\t', list[43], '\t', list[44], '\t', list[45], '\t', list[46], '\t', list[47])
    print(list[48], '\t', list[49], '\t', list[50], '\t', list[51], '\t', list[52], '\t', list[53], '\t', list[54], '\t', list[55])
    print(list[56], '\t', list[57], '\t', list[58], '\t', list[59], '\t', list[60], '\t', list[61], '\t', list[62], '\t', list[63])


def print_avg_js_matrix(list, len):
    print(list[0] / len, '\t', list[1] / len, '\t', list[2] / len, '\t', list[3] / len, '\t', list[4] / len, '\t', list[5] / len, '\t', list[6] / len, '\t', list[7] / len)
    print(list[8] / len, '\t', list[9] / len, '\t', list[10] / len, '\t', list[11] / len, '\t', list[12] / len, '\t', list[13] / len, '\t', list[14] / len, '\t', list[15] / len)
    print(list[16] / len, '\t', list[17] / len, '\t', list[18] / len, '\t', list[19] / len, '\t', list[20] / len, '\t', list[21] / len, '\t', list[22] / len, '\t', list[23] / len)
    print(list[24] / len, '\t', list[25] / len, '\t', list[26] / len, '\t', list[27] / len, '\t', list[28] / len, '\t', list[29] / len, '\t', list[30] / len, '\t', list[31] / len)
    print(list[32] / len, '\t', list[33] / len, '\t', list[34] / len, '\t', list[35] / len, '\t', list[36] / len, '\t', list[37] / len, '\t', list[38] / len, '\t', list[39] / len)
    print(list[40] / len, '\t', list[41] / len, '\t', list[42] / len, '\t', list[43] / len, '\t', list[44] / len, '\t', list[45] / len, '\t', list[46] / len, '\t', list[47] / len)
    print(list[48] / len, '\t', list[49] / len, '\t', list[50] / len, '\t', list[51] / len, '\t', list[52] / len, '\t', list[53] / len, '\t', list[54] / len, '\t', list[55] / len)
    print(list[56] / len, '\t', list[57] / len, '\t', list[58] / len, '\t', list[59] / len, '\t', list[60] / len, '\t', list[61] / len, '\t', list[62] / len, '\t', list[63] / len)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fiction_expanded_query_path', default='/store/victeur/jcdl-24/')
    parser.add_argument('--nonfiction_expanded_query_path', default='/store/victeur/ecir-24/')
    args = parser.parse_args()

    fic_global_dict = {}
    nonfic_global_dict = {}

    # read fiction data
    for qid in range(1, 26):
        fic_decade_dict = {}
        for folder in os.listdir(args.fiction_expanded_query_path):
            decade = folder.split('_')[0]
            folder += '/'
            filePath = os.path.join(args.fiction_expanded_query_path, folder)
            filePath += 'q' + str(qid) + '_feedback.terms.sorted'
            print('\nReading from the file : ', filePath)
            if os.path.isfile(filePath):
                fic_exp_query_dist = open(filePath, 'r')
                lines = fic_exp_query_dist.readlines()
                fic_prob_dist_list = []
                for x in lines:
                    fic_prob_dist_list.append(x.split('\t')[1])
                # from list to an array of floats
                for i in range(0, len(fic_prob_dist_list), 1):
                    fic_prob_dist_list[i] = fic_prob_dist_list[i].replace(',','')
                    fic_prob_dist_list[i] = float(fic_prob_dist_list[i])
                fic_exp_query_dist.close()
                fic_decade_dict[decade] = fic_prob_dist_list
            else:
                fic_prob_dist_list = [0.0] * 100
                fic_decade_dict[decade] = fic_prob_dist_list
        fic_decade_dict_sorted = collections.OrderedDict(sorted(fic_decade_dict.items()))
        fic_global_dict[qid] = fic_decade_dict_sorted
        # print(fic_global_dict)

        # read non-fiction data
        nonfic_decade_dict = {}
        for folder in os.listdir(args.nonfiction_expanded_query_path):
            decade = folder.split('_')[0]
            folder += '/'
            filePath = os.path.join(args.nonfiction_expanded_query_path, folder)
            filePath += 'q' + str(qid) + '.expand.query.sorted'
            print('\nReading from the file : ', filePath)
            if os.path.isfile(filePath):
                nonfic_exp_query_dist = open(filePath, 'r')
                lines = nonfic_exp_query_dist.readlines()
                nonfic_prob_dist_list = []
                for x in lines:
                    nonfic_prob_dist_list.append(x.split('\t')[1])
                # from list to an array of floats
                for i in range(0, len(nonfic_prob_dist_list), 1):
                    nonfic_prob_dist_list[i] = nonfic_prob_dist_list[i].replace(',', '')
                    nonfic_prob_dist_list[i] = float(nonfic_prob_dist_list[i])
                nonfic_exp_query_dist.close()
                nonfic_decade_dict[decade] = nonfic_prob_dist_list
            else:
                nonfic_prob_dist_list = [0.0] * 100
                nonfic_decade_dict[decade] = nonfic_prob_dist_list
        nonfic_decade_dict_sorted = collections.OrderedDict(sorted(nonfic_decade_dict.items()))
        nonfic_global_dict[qid] = nonfic_decade_dict_sorted
        # print(nonfic_global_dict)


    avg_jsdiv = np.zeros(64)
    # fiction
    for qid, value in fic_global_dict.items():
        jenson_list = []
        fic_list_of_dist = []
        for decade, list in value.items():
            fic_list_of_dist.append(list)
        # print('\n\n======= : ', fic_list_of_dist)
        # nonfiction
        nonfic_list_of_dist = []
        for decade2, list2 in nonfic_global_dict[qid].items():
            nonfic_list_of_dist.append(list2)
        # print('\n\n------- : ', nonfic_list_of_dist)
        # js divergence
        for fic_list in fic_list_of_dist:
            for nonfic_list in nonfic_list_of_dist:
                jenson_list.append(round(jenson_shanon(fic_list, nonfic_list), 4))
        jenson_list = [0.0 if math.isnan(val) else val for val in jenson_list]
        print('============== :', qid, '============== :\n', jenson_list)
        print_js_matrix(jenson_list)
        avg_jsdiv += np.array(jenson_list)
    print_avg_js_matrix(avg_jsdiv.tolist(), 25)


if __name__ == '__main__':
    main()