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

def getDistances(client_list):
    dist_mat = []
    for row in range(0, len(client_list)-1 ):
        node = []
        for col in range(0, len(client_list)-1 ):
            eqn = ((client_list[row].xcoords - client_list[col].xcoords)**2 + (client_list[row].ycoords - client_list[col].ycoords)**2)**0.5
            node.append(eqn)
        dist_mat.append(node)
    return dist_mat

def main():
    vehicle_list, client_list = setupData("VRP_Data.csv")
    dist = getDistances(client_list)
    print(dist[1])

if __name__ == '__main__':
    main()