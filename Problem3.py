class solution:

    def __init__(self, numbers, n_sum):
        self.numbers = numbers
        self.n_sum = n_sum

    def getNumbers(self):
        return self.numbers

    def getSum(self):
        return self.n_sum

class solutions:

    def __init__(self, numbers, target, tolerance):
        self.numbers = numbers
        self.target = target

        self.solution_list = [solution([num], num) for num in numbers]
        self.best_sol = solution([None], target + tolerance)

        for sol in self.solution_list:
            if abs(sol.n_sum - target) < abs(self.best_sol.n_sum - target):
                self.best_sol = sol

        self.sums = set(numbers)

    def iterate(self):
        sums_len = len(self.sums)
        add_sols = []
        for sol in self.solution_list:
            # if all get added to current sol then current sol will be obsolete
            # if none get added to current sol then current sol is a dead end
            # if either of these cases are true at the end we can remove this path
            # (leaving it as best solution if it is)
            added_all = True
            added_none = True
            for num in self.numbers:
                new_sum = sol.getSum() + num
                # if new sum is better that sol sum and not in all sums
                # it is a new solution
                if new_sum not in self.sums and abs(self.target - new_sum) < abs(self.target - sol.getSum()):
                    added_none = False
                    new_sol = solution(sol.getNumbers() + [num], new_sum)
                    # update the best solution if new sol is better
                    if abs(self.target - new_sum) < abs(self.target - self.best_sol.n_sum):
                        self.best_sol = new_sol
                    # update sums
                    self.sums.add(new_sum)
                    # add the new solution to a list to add at the end
                    add_sols.append(new_sol)
                else:
                    added_all = False
            # prune redundant branches
            if added_all or added_none:
                self.solution_list.remove(sol)
        # add the solutions
        self.solution_list += add_sols
        # return true when finished
        if len(self.sums) == sums_len:
            return False
        return True

target = 13.42
numbers = [0.01, 0.05, 0.10, 0.20, 0.50, 1, 2, 5, 10, 20, 50, 100, 200, 500]
solutions = solutions(numbers, target, 1)

i = 0
while(solutions.iterate()):
    i+=1

print('Target ammount           ',target)
print('Possible combinations:   ',i)
best_combination = sorted(solutions.best_sol.numbers)
print('Best combination:        ','+'.join(map(str, best_combination)))