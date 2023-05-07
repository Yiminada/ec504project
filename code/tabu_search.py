# Paper with original algo: https://www.sciencedirect.com/science/article/pii/S2405896318314022
import random

class TabuList:
    def __init__(self, max_size):
        self.max_size = max_size
        self.tabu_list = []

    def add_tabu(self, item):
        self.tabu_list.append(item)
        if len(self.tabu_list) > self.max_size:
            self.tabu_list.pop(0)

    def is_tabu(self, item):
        return item in self.tabu_list


# Define parameters
maxgen = 1000  # maximum number of iterations
tabulen1 = 20  # tabu list length for TS I
tabulen2 = 10  # tabu list length for TS II

# Define functions to generate initial solutions and neighborhoods
def generate_initial_solution():
    # Code to generate an initial solution
    pass

def get_neighborhood(solution):
    # Code to generate the neighborhood of a given solution
    pass

# Define the intensification operator
def do_intensification(solution):
    # Code to intensify a given solution
    pass

# Define the objective function
def objective_function(solution):
    # Code to evaluate the objective function for a given solution
    pass

# Define condition for intensification
def solution_needs_intensification(neighbor):
    # Code to determine if intensification is required
    pass

# Define the Tabu Search I algorithm
def tabu_search1(current_solution, best_solution, tabu_list1):
    # Generate the neighborhood of the current solution
    neighborhood = get_neighborhood(current_solution)
    best_neighbor = None
    for neighbor in neighborhood:
        # Check if the solution needs intensification
        if solution_needs_intensification(neighbor):
            neighbor = do_intensification(neighbor)
        # Check if the neighbor is not in the Tabu List 1
        if not tabu_list1.is_tabu(neighbor):
            # Check if the neighbor is better than the best neighbor found so far
            if best_neighbor is None or objective_function(neighbor) < objective_function(best_neighbor):
                best_neighbor = neighbor
    # Check if the best neighbor found is better than the best solution found so far
    if best_neighbor is not None and objective_function(best_neighbor) < objective_function(best_solution):
        best_solution = best_neighbor
    # Update the Tabu List 1
    tabu_list1.add_tabu(current_solution)
    # Return the current solution and the best solution found so far
    return current_solution, best_solution

# Define the Tabu Search II algorithm
def tabu_search2(current_solution, best_solution, tabu_list2):
    # Generate the neighborhood of the current solution
    neighborhood = get_neighborhood(current_solution)
    best_neighbor = None
    for neighbor in neighborhood:
        # Check if the solution needs intensification
        if solution_needs_intensification(neighbor):
            neighbor = do_intensification(neighbor)
        # Check if the neighbor is not in the Tabu List 2
        if not tabu_list2.is_tabu(neighbor):
            # Check if the neighbor is better than the current solution
            if objective_function(neighbor) < objective_function(current_solution):
                current_solution = neighbor
                # Check if the neighbor is better than the best solution found so far
                if objective_function(neighbor) < objective_function(best_solution):
                    best_solution = neighbor
                # Update the Tabu List 2
                tabu_list2.add_tabu(neighbor)
                break
    # Return the current solution and the best solution found so far
    return current_solution, best_solution

# Main function to run the algorithm
def run_algorithm(maxgen, max_size1, max_size2):
    # Generate initial solution s0 by PFIH.
    s0 = generate_initial_solution()
    # Initialize current solution and best solution to s0.
    scurrent, s_best = s0, s0
    # Initialize tabu lists.
    tl1, tl2 = TabuList(max_size1), TabuList(max_size2)

    # Loop for a given number of iterations.
    for iteration in range(maxgen):
        # Perform Tabu Search I.
        scurrent, s_best = tabu_search1(scurrent, s_best, tl1)
        # Perform Tabu Search II.
        scurrent, s_best = tabu_search2(scurrent, s_best, tl2)

    # Return the best solution found.
    return s_best
