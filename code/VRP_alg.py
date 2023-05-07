import setupVRP as vrp
import csv_randomizer as randCsv
import csv
import math
from datetime import datetime

import plotly.graph_objects as go
from setupVRP import client, vehicle, route
from visualize import showMap


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
            if (lines[0].isdigit()):  # VRP_Data
                client_list.append(vrp.client(
                    lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6]))
                if (lines[7].isdigit()):
                    vehicle_list.append(vrp.vehicle(lines[7], lines[8]))
            elif (lines[1].isdigit()):  # PR_Data
                client_list.append(vrp.client(
                    lines[1], lines[2], lines[3], lines[5], lines[6], lines[7], lines[8]))
                if (lines[9].isdigit()):
                    vehicle_list.append(vrp.vehicle(lines[9], lines[10]))

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
        profit_temp = -float('inf')
        invalidRoute = True
        for j in N:
            for r in R:
                for i_prev, i in r.edges:
                    if feasibility(r.vehicle, r, j) and profit(i_prev, i, j) > profit_temp:
                        invalidRoute = False
                        r_candidate = r
                        j_candidate = j
                        i_candidate = i
                        profit_temp = profit(i_prev, i, j)
        if invalidRoute:
            break
        N.remove(j_candidate)
        r_candidate.Insert(j_candidate, i_candidate)
        # Update(r_candidate)
    # for r in R:
    #     print(f"\nOrigin: ({r.orig.xcoords}, {r.orig.ycoords})")
    #     print(f"\nOrigin: {r.orig.id}")
    #     print(f"Capacity: {r.demand} vs {r.vehicle.capacity}")
    #     for client in r.clientList:
    #         print(f"({client.xcoords}, {client.ycoords})", end=',')
    #         print(client.id, end=', ')
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

def testCsv(iters, num_clients, num_vehicles):
    avg_runtime = 0.0
    for i in range(0,iters):
        randCsv.create_csv("test.csv", num_clients, num_vehicles)
        vehicle_list, client_list = setupData("test.csv")
        start = datetime.now()
        insertionHeuristic(client_list, vehicle_list)
        delta = datetime.now()-start
        avg_runtime += delta.total_seconds() 
    return avg_runtime/iters
        
def main():
    # vehicle_list, client_list = setupData("PR_Data.csv")
    # print("Vehicles: ", end='')
    # for v in vehicle_list:
    #     print(v.id, end=', ')
    # print("\nClients: ", end='')
    # for client in client_list:
    #     print(f"({client.xcoords}, {client.ycoords})", end=', ')
    # R = insertionHeuristic(client_list, vehicle_list)
    # fig = go.Figure()
    # colors = ["gray","blue","red","orange","green","purple"]
    # for count,r in enumerate(R):
    #     fig = showMap(r.edges, fig=fig,edgeColor=colors[count%len(colors)])
    # fig.show()
    
    
    print("\nRunning multiple tests, this could take a while:")
    print("-----------------------------------------------\n")
    iters = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    num_nodes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    num_vehicles = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    for i in range(0, len(iters) ):
        avg_runtime = testCsv(iters[i], num_nodes[i], num_vehicles[i])
        print("The average runtime is:", avg_runtime, "seconds for iters =", iters[i], ", num nodes =", num_nodes[i], ", and num vehicles =", num_vehicles[i])

if __name__ == '__main__':
    main()