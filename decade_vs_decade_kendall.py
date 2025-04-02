import argparse, csv
import ir_datasets
from scipy import stats


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--decade_res_list', default='/store/victeur/ecir-24/1831_index/BL_topics.xml-BM25k1=0.7,b=0.3-D100-T100-queryMix-0.5.res')
    parser.add_argument('--full_res_list', default='/store/victeur/ecir-24/full_index/BL_topics.xml-BM25k1=0.7,b=0.3-D100-T100-queryMix-0.5.res')
    args = parser.parse_args()

    # make decade ranklist dict
    decade_file = open(args.decade_res_list, 'r')
    decade_read = csv.reader(decade_file, delimiter='\t')
    decade_ranklist_dict = {}
    qid = ""
    ranklist = []
    for line in decade_read:
        if qid == "" or line[0] == qid:
            qid = line[0]
            ranklist.append(line[3])
        elif line[0] != qid:
            decade_ranklist_dict[int(qid)] = ranklist
            # print(qid, ':::::::::::::', ranklist)
            ranklist = []
            qid = line[0]
            ranklist.append(line[3])
        decade_ranklist_dict[int(qid)] = ranklist
    # print(qid, ':::::::::::::', ranklist)

    # make full coll ranklist dict
    fullcoll_file = open(args.full_res_list, 'r')
    fullcoll_read = csv.reader(fullcoll_file, delimiter='\t')
    full_ranklist_dict = {}
    qid = ""
    ranklist = []
    for line in fullcoll_read:
        if qid == "" or line[0] == qid:
            qid = line[0]
            ranklist.append(line[3])
        elif line[0] != qid:
            full_ranklist_dict[int(qid)] = ranklist
            # print(qid, ':::::::::::::', ranklist)
            ranklist = []
            qid = line[0]
            ranklist.append(line[3])
        full_ranklist_dict[int(qid)] = ranklist
    # print(qid, ':::::::::::::', ranklist)

    for qid in range(1, 26):
        list1 = decade_ranklist_dict[qid]
        # print(list1)
        list2 = full_ranklist_dict[qid]
        # print(list2)
        correlation = stats.kendalltau(list1, list2)
        print('\n',qid, '>>>>>>>>>>>>>>>', correlation)


if __name__ == '__main__':
    main()