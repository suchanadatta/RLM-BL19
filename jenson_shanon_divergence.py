import argparse
import os
import collections
import itertools
import numpy as np
from scipy.spatial import distance

def jenson_shanon(list1, list2):
    return distance.jensenshannon(list1, list2)


def print_js_matrix(list):
    print('1\t', list[0], '\t', list[1], '\t', list[2], '\t', list[3], '\t', list[4], '\t', list[5], '\t', list[6])
    print('0\t1\t', list[7], '\t', list[8], '\t', list[9], '\t', list[10], '\t', list[11], '\t', list[12])
    print('0\t0\t1\t', list[13], '\t', list[14], '\t', list[15], '\t', list[16], '\t', list[17])
    print('0\t0\t0\t1\t', list[18], '\t', list[19], '\t', list[20], '\t', list[21])
    print('0\t0\t0\t0\t1\t', list[22], '\t', list[23], '\t', list[24])
    print('0\t0\t0\t0\t0\t1\t', list[25], '\t', list[26])
    print('0\t0\t0\t0\t0\t0\t1\t', list[27])
    print('0\t0\t0\t0\t0\t0\t0\t1')


def print_avg_js_matrix(list, len):
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

    global_dict = {}
    for qid in range(1, 26):
        decade_dict = {}
        for folder in os.listdir(args.expanded_query_path):
            decade = folder.split('_')[0]
            folder += '/'
            filePath = os.path.join(args.expanded_query_path, folder)
            filePath += 'q' + str(qid) + '.expand.query.sorted'
            print('\nReading from the file : ', filePath)
            if os.path.isfile(filePath):
                exp_query_dist = open(filePath, 'r')
                lines = exp_query_dist.readlines()
                prob_dist_list = []
                for x in lines:
                    prob_dist_list.append(x.split('\t')[1])
                # from list to an array of floats
                for i in range(0, len(prob_dist_list), 1):
                    prob_dist_list[i] = prob_dist_list[i].replace(',','')
                    prob_dist_list[i] = float(prob_dist_list[i])
                exp_query_dist.close()
                decade_dict[decade] = prob_dist_list
            else:
                prob_dist_list = [0.0] * 100
                decade_dict[decade] = prob_dist_list
        decade_dict_sorted = collections.OrderedDict(sorted(decade_dict.items()))
        global_dict[qid] = decade_dict_sorted
        print('======= ', global_dict)

    avg_jsdiv = np.zeros(28)
    for qid, value in global_dict.items():
        list_of_dist = []
        jenson_list = []
        for decade, list in value.items():
            list_of_dist.append(list)
        for list1, list2 in itertools.combinations(list_of_dist, 2):
            jenson_list.append(round(jenson_shanon(list1, list2), 4))
        print('============== :', qid, '============== :', jenson_list)
        print_js_matrix(jenson_list)

        jenson_list = [0.0 if math.isnan(val) else val for val in jenson_list]
        print(jenson_list)
        avg_jsdiv += np.array(jenson_list)
    print_avg_js_matrix(avg_jsdiv.tolist(), 25)


if __name__ == '__main__':
    main()