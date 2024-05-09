#water jug in dfs
from collections import deque

def DFS(a, b, target):
    m = {}
    isSolvable = False
    path = []

    stack = deque()

    stack.append((0, 0))

    while stack:
        u = stack.pop()  # If this state is already visited
        if (u[0], u[1]) in m:
            continue
        if u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0:
            continue

        # Filling the vector for constructing the solution path
        path.append([u[0], u[1]])

        # Marking current state as visited
        m[(u[0], u[1])] = 1

        # If we reach the solution state, set isSolvable to True
        if u[0] == target or u[1] == target:
            isSolvable = True

            if u[0] == target:
                if u[1] != 0:
                    # Fill final state
                    path.append([u[0], 0])
            else:
                if u[0] != 0:
                    # Fill final state
                    path.append([0, u[1]])

            # Print the solution path
            sz = len(path)
            for i in range(sz):
                print("(", path[i][0], ",", path[i][1], ")")
            break

        # If we have not reached the final state
        # then, start developing intermediate states to reach the solution state
        stack.append([u[0], b])  # Fill Jug2
        stack.append([a, u[1]])  # Fill Jug1

        for ap in range(max(a, b) + 1):
            # Pour amount ap from Jug2 to Jug1
            c = u[0] + ap
            d = u[1] - ap

            # Check if this state is possible or not
            if c == a or (d == 0 and d >= 0):
                stack.append([c, d])

            # Pour amount ap from Jug1 to Jug2
            c = u[0] - ap
            d = u[1] + ap

            # Check if this state is possible or not
            if (c == 0 and c >= 0) or d == b:
                stack.append([c, d])

        # Empty Jug2
        stack.append([a, 0])

        # Empty Jug1
        stack.append([0, b])

    # No solution exists if isSolvable is still False
    if not isSolvable:
        print("No solution")

# Driver code
if __name__ == '__main__':
    Jug1, Jug2, target = 4, 3, 2
    print("Path from initial state to solution state ::")
    DFS(Jug1, Jug2, target)
