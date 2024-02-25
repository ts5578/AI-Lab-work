#cryptarthimatic problem.
#you can change the puzzle according to the question.

from itertools import permutations

def solve_cryptarithmetic(puzzle):
    # Extract unique letters from the puzzle
    letters = set([char for char in puzzle if char.isalpha()])
    if len(letters) > 10:
        return "Too many letters for a valid solution"

    # Generate all permutations of digits for the letters in the puzzle
    for perm in permutations('0123456789', len(letters)):
        sol = dict(zip(letters, perm))
        # Check for leading zero in any of the numbers
        if any(sol[word[0]] == '0' for word in puzzle.replace('=', '==').split() if word.isalpha()):
            continue
        # Replace letters with digits and evaluate the puzzle
        try:
            # Construct the equation by replacing letters with corresponding digits
            equation = puzzle.translate(str.maketrans(sol))
            # Check if the current permutation solves the puzzle
            if eval(equation):
                return sol
        except ArithmeticError:
            pass

    return "No solution found"

# Define the puzzle
puzzle = "EAT + THAT == APPLE"

# Solve the puzzle
solution = solve_cryptarithmetic(puzzle)

# Print the solution
if isinstance(solution, dict):
    print("Solution:")
    for letter, digit in solution.items():
        print(f"{letter} = {digit}")
else:
    print(solution)