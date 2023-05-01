class client:
    def __init__(self, id, xcoords, ycoords, demand, start_time, due_date, service_time):
        self.id = float(id)
        self.xcoords = float(xcoords)
        self.ycoords = float(ycoords)
        self.demand = float(demand)
        self.start_time = float(start_time)
        self.due_date = float(due_date)
        self.service_time = float(service_time)

    def equals(self,check):
        if self.id == check.id:
            return True

class vehicle:
    def __init__(self, id, capacity):
        self.id = float(id)
        self.capacity = float(capacity)

class route:
    def __init__(self, orig: client):
        """Expects an origin node to be given of type client"""
        self.orig = orig
        self.clientList = [orig]
        self.edges = [(orig,orig)]
        self.demand = orig.demand

    def Insert(self, client, goesTo):
        """Expects both comesFrom and goesTo to be existing nodes already"""
        for count, c in enumerate(self.edges):
            if c[1].equals(goesTo):
                self.edges[count] = (c[0],client)
                (self.edges).insert(count+1,(client,goesTo))
                (self.clientList).insert(count,client)
                break

        self.demand += client.demand

def testRoute():
    client1 = client(0, 1, 1, 20, 504, 207, 90)
    client2 = client(1, 2, 1, 3, 504, 207, 90)
    r = route(client1)
    print(r.demand)
    r.Insert(client2,client1)
    print(r.demand)

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
    testRoute()