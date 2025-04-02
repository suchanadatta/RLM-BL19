import argparse
import os
import collections
import itertools
import numpy as np

def jaccard_set(list1, list2):
    """Define Jaccard Similarity function for two sets"""
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

def print_jaccard_matrix(list):
    print('1\t', list[0], '\t', list[1], '\t', list[2], '\t', list[3], '\t', list[4], '\t', list[5], '\t', list[6])
    print('0\t1\t', list[7], '\t', list[8], '\t', list[9], '\t', list[10], '\t', list[11], '\t', list[12])
    print('0\t0\t1\t', list[13], '\t', list[14], '\t', list[15], '\t', list[16], '\t', list[17])
    print('0\t0\t0\t1\t', list[18], '\t', list[19], '\t', list[20], '\t', list[21])
    print('0\t0\t0\t0\t1\t', list[22], '\t', list[23], '\t', list[24])
    print('0\t0\t0\t0\t0\t1\t', list[25], '\t', list[26])
    print('0\t0\t0\t0\t0\t0\t1\t', list[27])
    print('0\t0\t0\t0\t0\t0\t0\t1')


def print_avg_jaccard_matrix(list, len):
    print('1\t', list[0]/len, '\t', list[1]/len, '\t', list[2]/len, '\t', list[3]/len, '\t', list[4]/len, '\t', list[5]/len, '\t', list[6]/len)
    print('0\t1\t', list[7]/len, '\t', list[8]/len, '\t', list[9]/len, '\t', list[10]/len, '\t', list[11]/len, '\t', list[12]/len)
    print('0\t0\t1\t', list[13]/len, '\t', list[14]/len, '\t', list[15]/len, '\t', list[16]/len, '\t', list[17]/len)
    print('0\t0\t0\t1\t', list[18]/len, '\t', list[19]/len, '\t', list[20]/len, '\t', list[21]/len)
    print('0\t0\t0\t0\t1\t', list[22]/len, '\t', list[23]/len, '\t', list[24]/len)
    print('0\t0\t0\t0\t0\t1\t', list[25]/len, '\t', list[26]/len)
    print('0\t0\t0\t0\t0\t0\t1\t', list[27]/len)
    print('0\t0\t0\t0\t0\t0\t0\t1')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--expanded_query_path', default='/store/victeur/ecir-24/')
    args = parser.parse_args()

    exp_query_dict = {}

    for folder in os.listdir(args.expanded_query_path):
        decade = folder.split('_')[0]
        folder += '/'
        filePath = os.path.join(args.expanded_query_path, folder)
        filePath += 'expanded.query'
        # print('\nReading from the file : ', filePath)

        decade_dict = {}

        expQueryReader = open(filePath, 'r')
        for line in expQueryReader:
            qid, query = line.split('\t')
            decade_dict[qid] = query
        exp_query_dict[decade] = decade_dict
    exp_query_dict_sorted = collections.OrderedDict(sorted(exp_query_dict.items()))
    # print(exp_query_dict_sorted)

    avg_jaccard = np.zeros(28)
    for qid in range(1, 26):
        decade_list = []
        jaccard_list = []
        for decade, value in exp_query_dict_sorted.items():
            decade_list.append(value[str(qid)])
        print('\n****** Decade list', decade_list)
        for query1, query2 in itertools.combinations(decade_list, 2):
            jaccard_list.append(round(jaccard_set(query1.split(), query2.split()), 4))
        print(jaccard_list)
        print_jaccard_matrix(jaccard_list)

        avg_jaccard += np.array(jaccard_list)
    print_avg_jaccard_matrix(avg_jaccard.tolist(), 25)


if __name__ == '__main__':
    main()