with open("input1.txt") as input_file, open("output1.txt","w") as output_file:
    def adjMat(input_file):
        n, m = input_file.readline().split()
        n, m = int(n), int(m)
        given = []
        for i in range(m):
            given.append([int(i) for i in input_file.readline().split()])
        adjMat = [[0 for i in range(n+1)] for j in range(n+1)]
        for j in range(len(given)):
            u,v,w = given[j]
            adjMat[u][v] = w

        return adjMat

    matrice = adjMat(input_file)
    for k in matrice:
        output_file.writelines(" ".join(map(str,k)))
        output_file.writelines('\n')


''' First we read the number of edges and vertices, then we create a (n+1)*(n+1) matrice to store the graph. For the upcoming
lines we just put the weight in the matrice, where u is the start node and v is the destination.
'''