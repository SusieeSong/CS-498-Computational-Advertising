import numpy as np
import scipy.sparse as sp
from scipy.sparse import lil_matrix
from scipy.sparse import csc_matrix
from sys import stdin
from collections import OrderedDict
import math


def print2largest_user(arr, userid):
    # There should be at least two
    # elements
    nnz = arr.count_nonzero()
    third = first = second = -1
    third_idx = first_idx = second_idx = -1
    r, c = arr.nonzero()
    c.sort()

    if (nnz == 1):
        userid.pop(c[0], None)
        idx = 1
        for key in userid:
            if idx == 1:
                first_idx = key
            else:
                second_idx = key
                break
            idx += 1
        print("{},{},{}".format(c[0], first_idx, second_idx))
        return

    if (nnz == 2):
        if arr[0, c[1]] > arr[0, c[0]]:
            first_idx = c[1]
            second_idx = c[0]
            userid.pop(c[1])
            userid.pop(c[0])
        else:
            first_idx = c[0]
            second_idx = c[1]
            userid.pop(c[1])
            userid.pop(c[0])

        idx = 1
        for key in userid:
            if idx == 1:
                third_idx = key
                break

        print("{},{},{}".format(first_idx, second_idx, third_idx))
        return


    for i in c:
        if (arr[0, i] > first):
            third = second
            third_idx = second_idx
            second = first
            second_idx = first_idx
            first = arr[0, i]
            first_idx = i

        elif (arr[0, i] > second):
            third = second
            third_idx = second_idx
            second = arr[0, i]
            second_idx = i

        elif (arr[0, i] > third):
            third = arr[0, i]
            third_idx = i
    print("{},{},{}".format(first_idx, second_idx, third_idx))
    return

def print2largest_ad(arr, adid, rowN):
    # There should be atleast two
    # elements
    nnz = arr.count_nonzero()
    third = first = second = -1
    third_idx = first_idx = second_idx = -1
    r, c = arr.nonzero()
    c.sort()

    if (nnz == 1):
        adid.pop(c[0]-1-rowN, "None")
        idx = 1
        for key in adid:
            if idx == 1:
                first_idx = key
            else:
                second_idx = key
                break
            idx += 1
        print("{},{},{}".format(c[0]-rowN-1, first_idx, second_idx))
        return

    if (nnz == 2):
        if arr[0, c[1]] > arr[0, c[0]]:
            first_idx = c[1]
            second_idx = c[0]
            adid.pop(c[1]-1-rowN)
            adid.pop(c[0]-1-rowN)
        else:
            first_idx = c[0]
            second_idx = c[1]
            adid.pop(c[1] - 1 - rowN)
            adid.pop(c[0] - 1 - rowN)

        idx = 1
        for key in adid:
            if idx == 1:
                third_idx = key
                break

        print("{},{},{}".format(first_idx-rowN-1, second_idx-rowN-1, third_idx))
        return


    for i in c:
        if (arr[0, i] > first):
            third = second
            third_idx = second_idx
            second = first
            second_idx = first_idx
            first = arr[0, i]
            first_idx = i

        elif (arr[0, i] > second):
            third = second
            third_idx = second_idx
            second = arr[0, i]
            second_idx = i

        elif (arr[0, i] > third):
            third = arr[0, i]
            third_idx = i
    print("{},{},{}".format(first_idx-rowN-1, second_idx-rowN-1, third_idx-rowN-1))
    return

def main():
    idx = -1
    # file = open("large_sample.txt")
    userid = OrderedDict()
    adid = OrderedDict()
    for line in stdin:
        if idx == -1:
            line_num = int(line[:])
            row = np.zeros(line_num, dtype=np.int32)
            col = np.zeros(line_num, dtype=np.int32)
            val = np.zeros(line_num)
            idx = 0
            continue

        if line_num == idx:
            temp = line.split(',')
            to_user = int(temp[0])
            to_ad = int(temp[1])
            break

        temp = line.split(',')
        row[idx] = int(temp[0])
        userid[int(temp[0])] = 1
        col[idx] = int(temp[1])
        adid[int(temp[1])] = 1
        val[idx] = float(temp[2])
        idx = idx + 1


    rowN = np.amax(row)
    colN = np.amax(col)
    matrix = lil_matrix((rowN + colN + 2, rowN + colN + 2))
    colsum = {}

    for i in range(0, line_num):
        matrix[row[i], rowN + 1 + col[i]] = 1
        matrix[rowN + 1 + col[i], row[i]] = 1
        if rowN + 1 + col[i] not in colsum:
            colsum[rowN + 1 + col[i]] = 1
        else:
            colsum[rowN + 1 + col[i]] += 1
        if row[i] not in colsum:
            colsum[row[i]] = 1
        else:
            colsum[row[i]] += 1

    for i in range(0, line_num):
        matrix[row[i], rowN + 1 + col[i]] = matrix[row[i], rowN + 1 + col[i]] / colsum[rowN + 1 + col[i]]
        matrix[rowN + 1 + col[i], row[i]] = matrix[rowN + 1 + col[i], row[i]] / colsum[row[i]]

    triu = sp.triu(matrix)
    tril = sp.tril(matrix)

    S0 = lil_matrix((rowN + colN + 2, rowN + colN + 2))
    for idx in userid:
        S0[idx, idx] = 1
    for idx in adid:
        S0[idx + rowN + 1, idx + rowN + 1] = 1

    S = S0
    for k in range(0, 11):
        user = 0.8 * tril.transpose() * S * tril
        for idx in userid:
            user[idx, idx] = 1
        ad = 0.8 * triu.transpose() * user * triu
        for idx in adid:
            ad[idx+rowN+1, idx+rowN+1] = 1
        S = ad + user

    S = S - S0
    r, c = S.nonzero()
    evidence1 = lil_matrix((rowN + colN + 2, rowN + colN + 2))
    evidence2 = lil_matrix((rowN + colN + 2, rowN + colN + 2))
    for idx in range(len(r)):
        evidence1[r[idx], c[idx]] = 1 - math.pow(0.5, colsum[r[idx]]+colsum[c[idx]])
        evidence2[r[idx], c[idx]] = 1 - math.exp(-colsum[r[idx]]-colsum[c[idx]])

    userid.pop(to_user, None)
    adid.pop(to_ad, None)

    print2largest_user(S[to_user, :], userid)
    print2largest_ad(S[to_ad+rowN+1, :], adid, rowN)

    old = S.copy()
    S = old.multiply(evidence1)
    print2largest_user(S[to_user, :], userid)
    print2largest_ad(S[to_ad+rowN+1, :], adid, rowN)

    S = old.multiply(evidence2)
    print2largest_user(S[to_user, :], userid)
    print2largest_ad(S[to_ad+rowN+1, :], adid, rowN)

if __name__ == "__main__":
    main()