import setupVRP as vrp
import csv
import numpy

def setupData(filename):
    # opening the CSV file
    count = 0
    client_list = []
    vehicle_list = []
    with open(filename, mode ='r') as file:
        # reading the CSV file
        csvFile = csv.reader(file)
        # displaying the contents of the CSV file
        for lines in csvFile:
            if(lines[0].isdigit()):
                client_list.append(vrp.client(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6]))
            if(lines[7].isdigit()):
                vehicle_list.append(vrp.vehicle(lines[7], lines[8]))
    return vehicle_list, client_list

def profit(i, j):
    return ((i.xcoords-j.xcoords)**2 + (i.ycoords-j.ycoords)**2)**0.5 #sqrt((x2-x1)^2 + (y2-y1)^2)
def feasibility():

def main():
    vehicle_list, client_list = setupData("VRP_Data.csv")
    print(profit(client_list[0], client_list[1]))
    
if __name__ == '__main__':
    main()