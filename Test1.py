seats = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]


def solutionFlight(N, S):
    # Implement your solution here
    FS = 4
    for c, i in enumerate(seats[N - 1]):
        if i == 'E':
            i.replace('E', 'F',4)
            break
    print(seats)
    pass


solutionFlight(1, 0)


def solution(A, B):
    # Implement your solution here
    sumA = 0
    sumB = 0
    index = 0
    indexCount = 0
    for i, j in zip(A, B):
        sumA = sumA + i
        sumB = sumB + j

        if sumA == sumB and index > 2:
            indexCount += 1
        index += 1
    print(indexCount)


A = [0, 4, -1, 0, 3]
B = [0, -2, 5, 0, 3]
solution(A, B)
