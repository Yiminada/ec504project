import setupVRP as vrp
import csv
import math
from setupVRP import client, vehicle, route


def setupData(filename):
    # opening the CSV file
    count = 0
    client_list = []
    vehicle_list = []
    with open(filename, mode='r') as file:
        # reading the CSV file
        csvFile = csv.reader(file)
        # displaying the contents of the CSV file
        for lines in csvFile:
            if (lines[0].isdigit()):
                client_list.append(vrp.client(
                    lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6]))
            if (lines[7].isdigit()):
                vehicle_list.append(vrp.vehicle(lines[7], lines[8]))
    return vehicle_list, client_list


def insertionHeuristic(N, V):
    """
    N is list of nodes, i.e. clients
    R is list of routes (one vehicle/route): each element in a route describes edge from [i-1,i]
    V is list of vehicles, w/ 1:1 correspondence b/w R and V
    """
    # initialize routes
    R = []
    origin = N[0]
    for v in V:
        R.append(route(origin, v))
    N.remove(origin)
    while N:
        print("in while loop")
        profit_temp = -float('inf')
        invalidRoute = True
        for j in N:
            for r in R:
                for i_prev, i in r.edges:
                    if feasibility(r.vehicle, r, j) and profit(i_prev, i, j) > profit_temp:
                        print("in if statement")
                        invalidRoute = False
                        r_candidate = r
                        j_candidate = j
                        i_candidate = i
                        profit_temp = profit(i_prev, i, j)
        if invalidRoute:
            break
        print(j_candidate.id)
        N.remove(j_candidate)
        r_candidate.Insert(j_candidate, i_candidate)
        # Update(r_candidate)
    for r in R:
        # print(f"\nOrigin: ({r.orig.xcoords}, {r.orig.ycoords})")
        print(f"\nOrigin: {r.orig.id}")
        print(f"Capacity: {r.demand} vs {r.vehicle.capacity}")
        for client in r.clientList:
            # print(f"({client.xcoords}, {client.ycoords})", end=',')
            print(client.id, end=', ')
    return R


def feasibility(vehicle, route, client):
    if (route.demand + client.demand < vehicle.capacity):
        return True
    else:
        return False


def profit(i_prev, i, j):
    i_prev_to_j = math.sqrt((i_prev.xcoords-j.xcoords)
                            ** 2 + (i_prev.ycoords-j.ycoords)**2)
    j_to_i = math.sqrt((j.xcoords-i.xcoords)**2 + (j.ycoords-i.ycoords)**2)
    i_prev_to_i = math.sqrt((i_prev.xcoords-i.xcoords)
                            ** 2 + (i_prev.ycoords-i.ycoords)**2)
    return -1 * (i_prev_to_j + j_to_i - i_prev_to_i)


def Update(r):
    return None


def main():
    vehicle_list, client_list = setupData("VRP_Data_1.csv")
    print("Vehicles: ", end='')
    for v in vehicle_list:
        print(v.id, end=', ')
    print("\nClients: ", end='')
    for client in client_list:
        print(f"({client.xcoords}, {client.ycoords})", end=', ')
    insertionHeuristic(client_list, vehicle_list)


if __name__ == '__main__':
    main()
