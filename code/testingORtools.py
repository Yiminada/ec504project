"""Capacited Vehicles Routing Problem (CVRP)."""

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from load_distance import getDistances, setupData
import plotly.graph_objects as go
from datetime import datetime
from visualize import showMap
import setupVRP
import csv_randomizer as randCsv
import csv


def load_data(filename="code/PR_Data.csv"):
    vehicle_list, client_list = setupData(filename)

    data = {}
    data['distance_matrix'] = getDistances(client_list)
    # print(data['distance_matrix'])
    data['demands'] = [client.demand for client in client_list]
    capacities = [vehicle.capacity for vehicle in vehicle_list]
    capacities.sort(reverse=True)
    data['vehicle_capacities'] = capacities
    data['num_vehicles'] = len(vehicle_list)
    data['depot'] = 0
    return data


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = [
        [
            0, 548, 776, 696, 582, 274, 502, 194, 308, 194, 536, 502, 388, 354,
            468, 776, 662
        ],
        [
            548, 0, 684, 308, 194, 502, 730, 354, 696, 742, 1084, 594, 480, 674,
            1016, 868, 1210
        ],
        [
            776, 684, 0, 992, 878, 502, 274, 810, 468, 742, 400, 1278, 1164,
            1130, 788, 1552, 754
        ],
        [
            696, 308, 992, 0, 114, 650, 878, 502, 844, 890, 1232, 514, 628, 822,
            1164, 560, 1358
        ],
        [
            582, 194, 878, 114, 0, 536, 764, 388, 730, 776, 1118, 400, 514, 708,
            1050, 674, 1244
        ],
        [
            274, 502, 502, 650, 536, 0, 228, 308, 194, 240, 582, 776, 662, 628,
            514, 1050, 708
        ],
        [
            502, 730, 274, 878, 764, 228, 0, 536, 194, 468, 354, 1004, 890, 856,
            514, 1278, 480
        ],
        [
            194, 354, 810, 502, 388, 308, 536, 0, 342, 388, 730, 468, 354, 320,
            662, 742, 856
        ],
        [
            308, 696, 468, 844, 730, 194, 194, 342, 0, 274, 388, 810, 696, 662,
            320, 1084, 514
        ],
        [
            194, 742, 742, 890, 776, 240, 468, 388, 274, 0, 342, 536, 422, 388,
            274, 810, 468
        ],
        [
            536, 1084, 400, 1232, 1118, 582, 354, 730, 388, 342, 0, 878, 764,
            730, 388, 1152, 354
        ],
        [
            502, 594, 1278, 514, 400, 776, 1004, 468, 810, 536, 878, 0, 114,
            308, 650, 274, 844
        ],
        [
            388, 480, 1164, 628, 514, 662, 890, 354, 696, 422, 764, 114, 0, 194,
            536, 388, 730
        ],
        [
            354, 674, 1130, 822, 708, 628, 856, 320, 662, 388, 730, 308, 194, 0,
            342, 422, 536
        ],
        [
            468, 1016, 788, 1164, 1050, 514, 514, 662, 320, 274, 388, 650, 536,
            342, 0, 764, 194
        ],
        [
            776, 868, 1552, 560, 674, 1050, 1278, 742, 1084, 810, 1152, 274,
            388, 422, 764, 0, 798
        ],
        [
            662, 1210, 754, 1358, 1244, 708, 480, 856, 514, 468, 354, 844, 730,
            536, 194, 798, 0
        ],
    ]
    data['demands'] = [0, 1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8]
    data['vehicle_capacities'] = [15, 15, 15, 15]
    data['num_vehicles'] = 4
    data['depot'] = 0
    return data


def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    print(f'Objective: {solution.ObjectiveValue()}')
    total_distance = 0
    total_load = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += data['demands'][node_index]
            plan_output += ' {0} Load({1}) -> '.format(node_index, route_load)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
            # print(route_distance)
        plan_output += ' {0} Load({1})\n'.format(manager.IndexToNode(index),
                                                 route_load)
        plan_output += 'Distance of the route: {}m\n'.format(route_distance)
        plan_output += 'Load of the route: {}\n'.format(route_load)
        print(plan_output)
        total_distance += route_distance
        total_load += route_load
    print('Total distance of all routes: {}m'.format(total_distance))
    print('Total load of all routes: {}'.format(total_load))

def ShowData(data, manager, routing, solution,filename="code/PR_Data.csv",imagename="ORTools.png"):
    vehicle_list, client_list = setupData(filename)
    fig = go.Figure()
    colors = ["gray","blue","red","orange","green","purple"]
    for vehicle_id in range(data['num_vehicles']):
        clients_in_route = []
        index = routing.Start(vehicle_id)
        while not routing.IsEnd(index):
            # Add all the clients to a list in order in this route
            node_index = manager.IndexToNode(index)
            clients_in_route += [client_list[node_index]]
            index = solution.Value(routing.NextVar(index))

        # create edges list
        edges = []
        for i in range(len(clients_in_route)-1):
            edges += [(clients_in_route[i],clients_in_route[i+1])]
        edges += [(clients_in_route[len(clients_in_route)-1],clients_in_route[0])]
        # print(colors[vehicle_id%len(colors)])
        fig = showMap(edges=edges,fig=fig,edgeColor=colors[vehicle_id%len(colors)])
    fig.write_image(imagename)





def main():
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    #data = create_data_model()
    data = load_data("code/PR_Data.csv")
    
    if sum(data['vehicle_capacities']) < sum(data['demands']):
        print("There is a greater demand than capacity, can not run code.")
        return
    
    
    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    
    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)


    # Add Capacity constraint.
    def demand_callback(from_index):
        """Returns the demand of the node."""
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(
        demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data['vehicle_capacities'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')
    
    
    start = datetime.now()
    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
    search_parameters.time_limit.FromSeconds(1)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    delta = datetime.now() - start
    if solution:
        print_solution(data, manager, routing, solution)
        print("Time to run in milliseconds: ", delta.total_seconds()*1000)
        ShowData(data,manager,routing,solution)
        

def testCsv(iters, num_clients, num_vehicles):
    avg_runtime = 0.0
    for i in range(0,iters):
        randCsv.create_csv("code/PR_Data.csv", num_clients, num_vehicles)
        # -----------------------------------------------------------------------------------------------------
        """Solve the CVRP problem."""
        # Instantiate the data problem.
        #data = create_data_model()
        data = load_data("code/PR_Data.csv")
        
        if sum(data['vehicle_capacities']) < sum(data['demands']):
            print("There is a greater demand than capacity, can not run code.")
            return
        
        
        # Create the routing index manager.
        manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                            data['num_vehicles'], data['depot'])

        # Create Routing Model.
        routing = pywrapcp.RoutingModel(manager)


        # Create and register a transit callback.
        def distance_callback(from_index, to_index):
            """Returns the distance between the two nodes."""
            # Convert from routing variable Index to distance matrix NodeIndex.
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return data['distance_matrix'][from_node][to_node]

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)

        
        # Define cost of each arc.
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)


        # Add Capacity constraint.
        def demand_callback(from_index):
            """Returns the demand of the node."""
            # Convert from routing variable Index to demands NodeIndex.
            from_node = manager.IndexToNode(from_index)
            return data['demands'][from_node]

        demand_callback_index = routing.RegisterUnaryTransitCallback(
            demand_callback)
        routing.AddDimensionWithVehicleCapacity(
            demand_callback_index,
            0,  # null capacity slack
            data['vehicle_capacities'],  # vehicle maximum capacities
            True,  # start cumul to zero
            'Capacity')
        
        
        start = datetime.now()
        # Setting first solution heuristic.
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
        search_parameters.local_search_metaheuristic = (
            routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
        search_parameters.time_limit.FromSeconds(1)

        # Solve the problem.
        solution = routing.SolveWithParameters(search_parameters)

        # -----------------------------------------------------------------------------------------------------


        delta = datetime.now()-start
        avg_runtime += delta.total_seconds() 
    return avg_runtime/iters


if __name__ == '__main__':
    # print("\nRunning multiple tests, this could take a while:")
    # print("-----------------------------------------------\n")
    # iters = [5 for _ in range(20)]
    # num_nodes = [50*(i+1) for i in range(20)]
    # num_vehicles = [i+1 for i in range(20)]
    # f = open("ORtoolsResults.csv",'w',newline='')
    # with f as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["Nodes", "Num_vehicles","Runtime"])
    #     for i in range(0, len(iters)):
    #         avg_runtime = testCsv(iters[i], num_nodes[i], num_vehicles[i])
    #         print("The average runtime is:", avg_runtime, "seconds for iters =", iters[i], ", num nodes =", num_nodes[i], ", and num vehicles =", num_vehicles[i])
    #         writer.writerow([num_nodes[i], num_vehicles[i], avg_runtime])
    # f.close()
    # #print(testCsv(1, 100000, 4))
    main()