import csv
import random

def create_csv(name, num_clients, num_vehicles):
    f = open(name, 'w', newline='')
    with f as file:
        writer = csv.writer(file)
        
        writer.writerow(["Customer ID", "X-Coordinate", "Y-Coordinate", "Demand", "Ready Time", 
                         "Due Date", "Service Time", "Vehicle Number", "Vehicle Capacity"])
        
        demand = 0
        for node in range(0, num_clients - num_vehicles):
            demand_node = random.randint(10,100)
            demand += demand_node
            writer.writerow([node, random.randint(-180,180), random.randint(-90,90), demand_node, 0, 0, 0, '-', '-'])
    f.close()

    f1 = open(name, 'a', newline='')
    with f1 as file:
        capacity = 0
        tot_demand = demand
        writer = csv.writer(file)
        for node in range(num_clients - num_vehicles, num_clients):
            demand_node = random.randint(10,100)
            tot_demand += demand_node
            temp = int(demand/num_vehicles+demand_node+random.randint(1, 20))
            capacity += temp
            writer.writerow([node, random.randint(-180,180), random.randint(-90,90), demand_node, 0, 0, 0, node - num_clients + num_vehicles, temp])
        # writer.writerow([""])
        # writer.writerow([""])
        # writer.writerow([""])
        # writer.writerow(["Demand = ", tot_demand])
        # writer.writerow(["Capcity = ", capacity])
    f1.close()


def main():
    name = "test.csv"
    num_clients = 100
    num_vehicles = 2
    create_csv(name, num_clients, num_vehicles)
    print(name, "has been created and set")
if __name__ == '__main__':
    main()