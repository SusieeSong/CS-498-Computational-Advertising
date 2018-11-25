import numpy as np
from scipy.sparse import lil_matrix
from sys import stdin
import math
from sklearn.metrics.pairwise import cosine_similarity

def main():
    idx = -1
    # file = open("h4test.txt")
    for line in stdin:
        line = line.split()
        if idx == -1:
            line_num = int(line[0])
            movie_num = int(line[1])
            ru = {}
            rm = {}
            rum = {}
            rating = np.zeros((line_num))
            metadata = {}
            datastring = []
            idx = 0
            continue

        if idx < line_num:
            user_id = int(line[0])
            movie_id = int(line[1])
            if user_id not in ru:
                ru[user_id] = []
                ru[user_id].append(int(line[1]))
            else:
                ru[user_id].append(int(line[1]))

            if movie_id not in rm:
                rm[movie_id] = []
                rm[movie_id].append(int(line[0]))
            else:
                rm[movie_id].append(int(line[0]))
            rating[idx] = float(line[2])
            rum[(user_id, movie_id)] = rating[idx]
        elif idx < line_num + movie_num:
            datastring += (line[1:])
            metadata[int(line[0])] = line[1:]
        else:
            tar_user = int(line[0])
            tar_movie = int(line[1])
        idx += 1

    miu = rating.mean()
    # print(rm)
    bm = {}
    for m in rm:
        sum = 0.0
        for u in rm[m]:
            sum += rum[(u, m)] - miu
        bm[m] = sum / len(rm[m])

    bu = {}
    for u in ru:
        sum = 0.0
        for m in ru[u]:
            sum += rum[(u, m)] - miu - bm[m]
        bu[u] = sum / len(ru[u])

    bum = {}
    for u in ru:
         for m in rm:
             bum[(u, m)] = miu + bu[u] + bm[m]

    #print(rm)

    unique_item = {}
    pos = 0
    for e in datastring:
        if e not in unique_item:
            unique_item[e] = pos
            pos += 1

    d = {}
    d[tar_movie] = lil_matrix((1, len(unique_item)))
    for term in metadata[tar_movie]:
        if d[tar_movie][0, unique_item[term]] == 0:
            d[tar_movie][0, unique_item[term]] = metadata[tar_movie].count(term)*math.log(movie_num/inverse_df(term, metadata)) / len(metadata[tar_movie])

    # print(metadata[tar_movie])
    # print(d[tar_movie])

    sum1 = 0.0
    sum2 = 0.0
    for j in ru[tar_user]:
        d[j] = lil_matrix((1, len(unique_item)))
        for term in metadata[j]:
            if d[j][0, unique_item[term]] == 0:
                d[j][0, unique_item[term]] = metadata[j].count(term)*math.log(movie_num/inverse_df(term, metadata)) / len(metadata[j])

        smj = cosine_similarity(d[tar_movie], d[j])
        # print(rum[tar_user, j], bum[tar_user, j])
        # print(bum[(tar_user, j)])
        sum1 += smj*float(rum[(tar_user, j)] - bum[(tar_user, j)])
        sum2 += smj

    print(round(sum1[0][0]/sum2[0][0] + bum[(tar_user, tar_movie)], 1))

def inverse_df(term, dataset):
    num = 0
    for key in dataset:
        if term in dataset[key]:
            num += 1

    return num

if __name__=="__main__":
    main()