import numpy as np

class client:
    def __init__(self, id, xcoords, ycoords, demand, start_time, due_date, service_time):
        self.id = float(id)
        self.xcoords = float(xcoords)
        self.ycoords = float(ycoords)
        self.demand = int(float(demand)+0.5)
        self.start_time = float(start_time)
        self.due_date = float(due_date)
        self.service_time = float(service_time)

    def equals(self, check):
        if self.id == check.id:
            return True


class vehicle:
    def __init__(self, id, capacity):
        self.id = float(id)
        self.capacity = int(float(capacity)+0.5)


class route:
    def __init__(self, orig: client, vehicle: vehicle):
        """Expects an origin node to be given of type client"""
        self.orig = orig
        self.clientList = [orig]
        self.edges = [(orig, orig)]
        self.demand = orig.demand
        self.vehicle = vehicle

    def Insert(self, client, goesTo):
        """Expects goesTo to be existing node already"""
        for count, c in enumerate(self.edges):
            if c[1].equals(goesTo):
                self.edges[count] = (c[0],client)
                (self.edges).insert(count+1,(client,goesTo))
                (self.clientList).insert(count,client)
                self.demand += client.demand
                return
                
        print("Could not insert, goesTo not found")
    
    def getTotDistance(self):
        runtot = 0
        for edge in self.edges:
            runtot += findDist(edge[0],edge[1])
        return runtot

def findDist(c1, c2):
    """Expects two clients, returns distance between them"""
    return np.sqrt((c1.xcoords - c2.xcoords)**2 + (c1.ycoords - c2.ycoords)**2)

def testRoute():
    client1 = client(0, 1, 1, 20, 504, 207, 90)
    client2 = client(1, 2, 1, 3, 504, 207, 90)
    r = route(client1)
    print(r.demand)
    r.Insert(client2, client1)
    print(r.demand)


def main():
    # make client to test client
    client1 = client(0, 1, 1, 20, 504, 207, 90)
    print("Client1:")
    print(client1.id, client1.xcoords, client1.ycoords, client1.demand,
          client1.start_time, client1.due_date, client1.service_time)

    # make vehicle to test vehicle class
    vehicle1 = vehicle(0, 100)
    print("\nvehicle: ")
    print(vehicle1.id, vehicle1.capacity)


if __name__ == '__main__':
    testRoute()
