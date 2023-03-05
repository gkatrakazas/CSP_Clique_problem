import constraint
import time
import random

def generate_random_adjacency_matrix(n):
    adjacency_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            adjacency_matrix[i][j] = random.randint(0, 1)
            adjacency_matrix[j][i] = adjacency_matrix[i][j]
    return adjacency_matrix

def find_maximum_clique_size(adjacency_matrix):
    def get_clique_size(solution):
        return sum(solution.values())

    problem = constraint.Problem()
    vertices = range(len(adjacency_matrix))
    problem.addVariables(vertices, [0, 1])

    for i in range(len(adjacency_matrix)):
        for j in range(i+1, len(adjacency_matrix)):
            if adjacency_matrix[i][j] == 0:
                problem.addConstraint(lambda x, y: x + y < 2 , (i, j))

    solutions = problem.getSolutions()

    max_clique_size = max([get_clique_size(solution) for solution in solutions])
    return max_clique_size

if __name__ == "__main__":
    n = 50
    adjacency_matrix = generate_random_adjacency_matrix(n)

    start_time = time.time()
    maximum_clique_size = find_maximum_clique_size(adjacency_matrix)
    end_time = time.time()

    print("Adjacency matrix:")
    for row in adjacency_matrix:
        print(row)
    print("Maximum clique size:", maximum_clique_size)
    print("Calculation time:", end_time - start_time, "seconds")
