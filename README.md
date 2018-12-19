# CS-498-Computational-Advertising-

This class surveys the emerging landscape of computational advertising. It provides students with a thorough understanding of the technologies including web-search, auctions, behavioral targeting, mechanisms for viral marketing, that underpin the display of advertisements on a variety of locations. These locations include web pages (banner ads), on prominent search engines (text ads), on social media platforms, as well as cell phones. The students shall also learn about emerging areas in computational advertising including electronic billboards, moving objects (banners atop taxi cabs) and algorithmic synthesis of personalized advertisements. Discussion around privacy is a significant focus of the class. 

# Mp1 Implement the HITS algorithm

Input Format

The input consits of User-Movie links, where users denote the hubs and movies denote the authorities in the HITS algorithm. 

The first line specifies the total number of links N, followed by N lines each containing 2 comma separated non-negative integer values - U, M where 0 <= U <= 1,000,000 and 0 <= M <= 1,000,000 
A sample input looks like 

N
U1, M1
U2, M2
...
UN, MN

Note U1 is a user-id, while M1 is the movie-id for a movie reviewed positively by U. Note that a given user can review more than one movie, meaning multiple lines could have the same user-id, but no two lines are identical.

You are required to build the bipartitle Hub-Authority graph (with users as hubs, and movies as authorities) using the above links, initialize the algorithm with equal weights assigned to all hubs and authorities, and perform K=10 iterations of Authority and Hub-Score updates.

Constraints

No constraints.

Output Format

Your output must contain 2 lines, 
The first line contains the comma separated IDs of the top 3 hubs (by their hub-score) in decreasing order meaning that the first ID corresponds to the highest score. Note that the top hubs are the most profilic movie reviewers. 

In case there is a tie, print the smaller ID value first (i.e. if ID's 1 and 2 are both tied for first place, then the first place will be assigned to ID 1 and second place to ID 2). 

The second line contains the comma separated IDs of the top 3 authorities (by authority-score), which in this case refers to critically acclaimed movies. Follow the same instructions as above for the order of IDs and tie-breaking. 

A sample output looks like this-
U1,U2,U3
M1,M2,M3



Sample Input 0

4
1,1
2,2
3,3
4,4
Sample Output 0

1,2,3
1,2,3
Explanation 0

Each user receives the same hub-score after K=10 iterations, thus they are sorted to place the smaller ID first. Same for the movies.

Sample Input 1

6
2100,10897
2100,21443
12,10897
12,21443
12,38976
387,41005
Sample Output 1

12,2100,387
10897,21443,38976

# Mp2 Implement SimRank and SimRank with evidence
**In this question, you are required to implement the SimRank algorithm and SimRank with 2 forms of evidence weights with a supported programming language of your choice. In each case, your iterations must begin with user updates, alternating with ad similarity updates. We will use this reference for the algorithm details. You can use the sample test case to debug your code, however the final test case is significantly larger and hence may require an efficient implementation. You should use partial sum sharing to speed up your implementation.**

Input Format

The input consits of weighted User-Ad links. 

The first line specifies the total number of links N, followed by N lines each containing 3 comma separated entries - U, A, S where U and A are integers representing User and Ad Ids, 0 <= U <= 1,000,000 and 0 <= A <= 1,000,000, and score S is a float score value for that link, 0.0 <= S <= 1,000.0. The score is based on how fast the user responded to the Ad (a higher score denotes a greater proclivity).

This is then followed by a single line with 2 ids, Q_U and Q_A. You need to output the 3 most similar users to Q_U and the 3 most similar ads to Q_A with each of the variations of simrank. In case 2 of the 3 entries have the same similarity score in any case, use the same tiebreak criterion as in the previous assignment.

A sample input looks like 

N
U1, A1, S1
U2, A2, S2
...
UN, AN, SN
Q_U,Q_A


Note U1 is a user-id, while A1 is the advertisement-id for a specific display-ad clicked by U and S1 is the link weight. Note that a given user can click more than one ad, meaning multiple lines could have the same user-id, but no two lines are identical. You are required to build the bipartitle weighted User-Ad graph using the above links.

Task One - Simple SimRank iterations
Implement conventional SimRank and compute the similarities of users to each other and ads to other ads. You need to use the partial sums trick described in the links provided with the assignment description in your implementation. Initialize the algorithm with the usual procedure (similarity of a node to itself is 1 and 0 to all others), and perform K=10 iterations of User and Ad-similarity updates (start with user similarity updates). The constants C1 and C2 are both set to 0.8. Let us call the similarity scores obtained after K=10 iterations simple_simrank_scores.

Task Two - Incorporate evidence
In section 7 of the reference, two forms are introduced for evidence scores (geometric in eq 7.3 and exponential in eq 7.4). You will apply each of these forms to the results obtained after 10 iterations of Simple SimRank and obtain the new similarity scores for users and ads. Let us call these 2 new sets of scores evidence_geometric_scores and evidence_exponential_scores.


You output should contain 6 lines - 

Line 1 - 3 most similar users to Q_U with simple_simrank_scores
Line 2 - 3 most similar ads to Q_A with simple_simrank_scores
Line 3 - 3 most similar users to Q_U with evidence_geometric_scores
Line 4 - 3 most similar ads to Q_A with evidence_geometric_scores
Line 5 - 3 most similar users to Q_U with evidence_exponential_scores
Line 6 - 3 most similar ads to Q_A with evidence_exponential_scores

Constraints

-No constraints.

Output Format

Your output must contain 6 lines as described above, follow the same instructions as the last assignment for tie-breaks.

A sample output looks like this-
U_1,U_2,U_3
A_1,A_2,A_3
U_4,U_5,U_6
A_4,A_5,A_6
U_7,U_8,U_9
A_7,A_8,A_9



Sample Input 0

8
1,20,1.0
2,20,2.0
2,38,2.5
3,20,1.2
3,38,1.7
4,38,2.5
5,1235,0.9
5,8271,3.8
1,20
Sample Output 0

2,3,4
38,1235,8271
2,3,4
38,1235,8271
2,3,4
38,1235,8271

# Mp3 Recommender Systems
**The objective of this programming assignment is to design a movie recommender system. The main goal of such a system is to recommend relevant movies to an user based on available data. Data includes information about the movies and ratings provided by a user to a subset of movies. We will have some metadata information about each movie like title, a brief overview , tagline of the movie etc. We also have the ratings that a user has provided to some of the movies. Now based on movie metadata and ratings information, we need to
recommend new movies to an user.**

Input Format

The input contains the (user,movie) rating information, movie metadata and the (user,movie) pair for which you need to estimate the rating.

The first line of the input contains 2 space seperated integers R M. R is the number of lines of rating information. M is the number of movies.

Next R lines contain the rating information. Each line will contain 3 space seperated values (user id, movie id, rating).

Next M lines contain the metadata information. The first word/value of each line is the movie id. The rest of the words are the metadata information about that movie.

The last line with contain 2 space seperated integers (target user id, target movie id) for which you need to estimate the rating.

Please refer to the sample input 0 below.

There are 5 rating information lines and 5 movie metadata lines. You need to find the rating that user 1 would have given to movie 4.

Constraints

NA

Output Format

Your ouput should be a single floating point value for the estimated rating. Round the output to 1 decimal point.

Sample Input 0

5 5
1 1 3.0
1 2 4.0
1 3 3.0
2 4 2.0
2 5 5.0
1 batman robin superhero
2 batman dark knight
3 dark knight returns
4 batman joker gotham
5 batman superhero
1 4
Sample Output 0

2.0
Sample Input 1

6 5
1 1 3.0
1 2 4.0
1 3 3.0
2 1 2.8
2 4 2.0
2 5 5.0
1 batman robin superhero
2 batman dark knight
3 dark knight returns
4 batman joker gotham
5 batman superhero
1 5
Sample Output 1

5.1
