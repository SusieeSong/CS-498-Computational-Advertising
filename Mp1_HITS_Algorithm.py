import numpy as np
from scipy.sparse import csr_matrix
from sys import stdin

def sort_idx(idx, value):
    d = dict(zip(idx, value))
    result = sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))
    return result

def main():
    data = ""
    idx = -1
    for line in stdin:
        if idx == -1:
            line_num = int(line[:])
            row = np.zeros(line_num)
            col = np.zeros(line_num)
            val = np.zeros(line_num)
            idx = 0
            continue
            
        temp = line.split(',')
        row[idx] = int(temp[0])
        col[idx] = int(temp[1])
        val[idx] = 1
        idx = idx + 1
    
    matrix = csr_matrix((val, (row, col)))
    user_num  = matrix.shape[0]
    movie_num = matrix.shape[1]
    user_score = np.ones(user_num)
    
    for i in range(0, 9):
        movie_score = user_score * matrix
        movie_score = movie_score / sum(movie_score)
        user_score = movie_score * matrix.transpose()
    
    user_idx = np.argsort(-user_score)[:3]
    result1 = sort_idx(user_idx, user_score[user_idx])

    string = ""
    for pair in result1:
        string = string + str(pair[0]) + ','
    print(string[:-1])
    
    movie_idx = np.argsort(-movie_score)[:3]
    result2 = sort_idx(movie_idx, movie_score[movie_idx])
    string = ""
    for pair in result2:
        string = string + str(pair[0]) + ','
    print(string[:-1])

if __name__=="__main__":
    main()