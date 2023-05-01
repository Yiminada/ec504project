class client:
    def __init__(self, id, xcoords, ycoords, demand, start_time, due_date, service_time):
        self.id = id
        self.xcoords = xcoords
        self.ycoords = ycoords
        self.demand = demand
        self.start_time = start_time
        self.due_date = due_date
        self.service_time = service_time
class vehicle:
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity

def main():
    #make client to test client
    client1 = client(0, 1, 1, 20, 504, 207, 90)
    print("Client1:")
    print(client1.id, client1.xcoords, client1.ycoords, client1.demand, 
          client1.start_time, client1.due_date, client1.service_time)
    
    #make vehicle to test vehicle class
    vehicle1 = vehicle(0, 100)
    print("\nvehicle: ")
    print(vehicle1.id, vehicle1.capacity)
if __name__ == '__main__':
    main()