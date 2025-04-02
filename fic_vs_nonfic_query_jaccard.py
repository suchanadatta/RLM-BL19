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
    print(list[0], '\t', list[1], '\t', list[2], '\t', list[3], '\t', list[4], '\t', list[5], '\t', list[6], '\t', list[7])
    print(list[8], '\t', list[9], '\t', list[10], '\t', list[11], '\t', list[12], '\t', list[13], '\t', list[14], '\t', list[15])
    print(list[16], '\t', list[17], '\t', list[18], '\t', list[19], '\t', list[20], '\t', list[21], '\t', list[22], '\t', list[23])
    print(list[24], '\t', list[25], '\t', list[26], '\t', list[27], '\t', list[28], '\t', list[29], '\t', list[30], '\t', list[31])
    print(list[32], '\t', list[33], '\t', list[34], '\t', list[35], '\t', list[36], '\t', list[37], '\t', list[38], '\t', list[39])
    print(list[40], '\t', list[41], '\t', list[42], '\t', list[43], '\t', list[44], '\t', list[45], '\t', list[46], '\t', list[47])
    print(list[48], '\t', list[49], '\t', list[50], '\t', list[51], '\t', list[52], '\t', list[53], '\t', list[54], '\t', list[55])
    print(list[56], '\t', list[57], '\t', list[58], '\t', list[59], '\t', list[60], '\t', list[61], '\t', list[62], '\t', list[63])

def print_avg_jaccard_matrix(list, len):
    print(list[0]/len, '\t', list[1]/len, '\t', list[2]/len, '\t', list[3]/len, '\t', list[4]/len, '\t', list[5]/len, '\t', list[6]/len, '\t', list[7]/len)
    print(list[8]/len, '\t', list[9]/len, '\t', list[10]/len, '\t', list[11]/len, '\t', list[12]/len, '\t', list[13]/len, '\t', list[14]/len, '\t', list[15]/len)
    print(list[16]/len, '\t', list[17]/len, '\t', list[18]/len, '\t', list[19]/len, '\t', list[20]/len, '\t', list[21]/len, '\t', list[22]/len, '\t', list[23]/len)
    print(list[24]/len, '\t', list[25]/len, '\t', list[26]/len, '\t', list[27]/len, '\t', list[28]/len, '\t', list[29]/len, '\t', list[30]/len, '\t', list[31]/len)
    print(list[32]/len, '\t', list[33]/len, '\t', list[34]/len, '\t', list[35]/len, '\t', list[36]/len, '\t', list[37]/len, '\t', list[38]/len, '\t', list[39]/len)
    print(list[40]/len, '\t', list[41]/len, '\t', list[42]/len, '\t', list[43]/len, '\t', list[44]/len, '\t', list[45]/len, '\t', list[46]/len, '\t', list[47]/len)
    print(list[48]/len, '\t', list[49]/len, '\t', list[50]/len, '\t', list[51]/len, '\t', list[52]/len, '\t', list[53]/len, '\t', list[54]/len, '\t', list[55]/len)
    print(list[56]/len, '\t', list[57]/len, '\t', list[58]/len, '\t', list[59]/len, '\t', list[60]/len, '\t', list[61]/len, '\t', list[62]/len, '\t', list[63]/len)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fiction_expanded_query_path', default='/store/victeur/jcdl-24/')
    parser.add_argument('--nonfiction_expanded_query_path', default='/store/victeur/ecir-24/')
    args = parser.parse_args()

    fic_exp_query_dict = {}
    nonfic_exp_query_dict = {}

    # read fiction feedback query path
    for folder in os.listdir(args.fiction_expanded_query_path):
        if folder != 'wordvecs':
            decade = folder.split('_')[0]
            folder += '/'
            filePath = os.path.join(args.fiction_expanded_query_path, folder)
            filePath += 'expanded.query'
            print('\nReading from the file : ', filePath)

            fic_decade_dict = {}

            ficExpQueryReader = open(filePath, 'r')
            for line in ficExpQueryReader:
                qid, query = line.split('\t')
                fic_decade_dict[qid] = query
            fic_exp_query_dict[decade] = fic_decade_dict
    fic_exp_query_dict_sorted = collections.OrderedDict(sorted(fic_exp_query_dict.items()))
    print('Total entry for fiction dict : ', len(fic_exp_query_dict_sorted))
    # print(fic_exp_query_dict_sorted)

    # read non-fiction feedback query path
    for folder in os.listdir(args.nonfiction_expanded_query_path):
        decade = folder.split('_')[0]
        folder += '/'
        filePath = os.path.join(args.nonfiction_expanded_query_path, folder)
        filePath += 'expanded.query'
        print('\nReading from the file : ', filePath)

        nonfic_decade_dict = {}

        nonficExpQueryReader = open(filePath, 'r')
        for line in nonficExpQueryReader:
            qid, query = line.split('\t')
            nonfic_decade_dict[qid] = query
        nonfic_exp_query_dict[decade] = nonfic_decade_dict
    nonfic_exp_query_dict_sorted = collections.OrderedDict(sorted(nonfic_exp_query_dict.items()))
    print('Total entry for non-fiction dict : ', len(nonfic_exp_query_dict_sorted))
    # print(nonfic_exp_query_dict_sorted)

    avg_jaccard = np.zeros(64)
    for qid in range(1, 26):
        fic_decade_list = []
        nonfic_decade_list = []
        jaccard_list = []

        # for fiction
        for decade, value in fic_exp_query_dict_sorted.items():
            fic_decade_list.append(value[str(qid)])
        # print('\n****** Fiction decade list', fic_decade_list)
        # for non-fiction
        for decade, value in nonfic_exp_query_dict_sorted.items():
            nonfic_decade_list.append(value[str(qid)])
        # print('\n****** Nonfiction decade list', nonfic_decade_list)

        for query1 in fic_decade_list:
            for query2 in nonfic_decade_list:
                jaccard_list.append(round(jaccard_set(query1.split(), query2.split()), 4))
        print('============ ', qid, ' ============')
        # print(jaccard_list)
        print('length of the jaccard list : ', len(jaccard_list))
        print_jaccard_matrix(jaccard_list)

        avg_jaccard += np.array(jaccard_list)
    print_avg_jaccard_matrix(avg_jaccard.tolist(), 25)


if __name__ == '__main__':
    main()