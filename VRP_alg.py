import setupVRP as vrp
import csv


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


def insertionHeuristic(N):
    # set of routes: each element in a route describes edge from [i-1,i]
    R = [[[0, 0]]]
    while N:
        profit_temp = -float('inf')
        invalidRoute = True
        for j in N:
            for r in R:
                for i_prev, i in r:
                    if isFeasible(i_prev, i) and getProfit(i_prev, i) > profit_temp:
                        invalidRoute = False
                        r_candidate = r
                        i_prev_candidate = i_prev
                        j_candidate = j
                        profit_temp = getProfit(i_prev, i)
        if invalidRoute:
            break
        del N[j_candidate]
        Insert(i_prev_candidate, j_candidate)
        Update(r_candidate)
    return R


def isFeasible(i, j):   # REPLACE THIS FUNCTION WITH FEASIBILITY
    return True


def feasibility(vehicle, route, client):
    if (route.demand + client.demand < vehicle.capacity):
        return True
    else:
        return False


def getProfit(i, j):  # REPLACE THIS FUNCTION WITH PROFIT
    return 5


def profit(i, j):
    # sqrt((x2-x1)^2 + (y2-y1)^2)
    return ((i.xcoords-j.xcoords)**2 + (i.ycoords-j.ycoords)**2)**0.5


def Insert(i, j):
    return None


def Update(r):
    return None


def main():
    vehicle_list, client_list = setupData("VRP_Data.csv")
    insertionHeuristic({0: [0, 0]})
    print(profit(client_list[0], client_list[1]))


if __name__ == '__main__':
    main()
