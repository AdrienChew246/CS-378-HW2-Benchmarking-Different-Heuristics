import unified_planning as up
from unified_planning.shortcuts import *
from unified_planning.io import PDDLWriter
import os

def generate_q2_waymo(directory="q2"):
    if not os.path.exists(directory):
        os.makedirs(directory)

    DOMAIN_NAME = "waymo_2_electric_boogaloo"

    # Size
    for i in range(1, 6):
        leg_length = 2**i 
        problem = Problem(DOMAIN_NAME)
        
        # Types
        Location = UserType("Location")
        Waymo = UserType("Waymo")
        Passenger = UserType("Passenger")
        
        # Fluents
        waymo_at = Fluent("waymo_at", BoolType(), v=Waymo, l=Location)
        passenger_at = Fluent("passenger_at", BoolType(), p=Passenger, l=Location)
        boarding = Fluent("boarding", BoolType(), p=Passenger, v=Waymo)
        connected = Fluent("connected", BoolType(), l1=Location, l2=Location)

        problem.add_fluents([waymo_at, passenger_at, boarding, connected])
        
        # Actions
        # Drive
        drive = InstantaneousAction("drive", v=Waymo, l_from=Location, l_to=Location)
        v, f, t = drive.parameter("v"), drive.parameter("l_from"), drive.parameter("l_to")
        drive.add_precondition(waymo_at(v, f))
        drive.add_precondition(connected(f, t))
        drive.add_effect(waymo_at(v, t), True)
        drive.add_effect(waymo_at(v, f), False)
        problem.add_action(drive)
        
        # Pickup Passenger
        pickup = InstantaneousAction("pickup", v=Waymo, p=Passenger, l=Location)
        v, p, l = pickup.parameter("v"), pickup.parameter("p"), pickup.parameter("l")
        pickup.add_precondition(waymo_at(v, l))
        pickup.add_precondition(passenger_at(p, l))
        pickup.add_effect(boarding(p, v), True)
        pickup.add_effect(passenger_at(p, l), False)
        problem.add_action(pickup)
        
        # Dropoff Passenger
        dropoff = InstantaneousAction("dropoff", v=Waymo, p=Passenger, l=Location)
        v, p, l = dropoff.parameter("v"), dropoff.parameter("p"), dropoff.parameter("l")
        dropoff.add_precondition(waymo_at(v, l))
        dropoff.add_precondition(boarding(p, v))
        dropoff.add_effect(passenger_at(p, l), True)
        dropoff.add_effect(boarding(p, v), False)
        problem.add_action(dropoff)

        # Graph
        hub = Object("stop_0", Location)
        problem.add_object(hub)
        
        # Create 4 legs (North, South, East, West)
        legs = []
        for direction in ["n", "s", "e"]:
            leg_nodes = [Object(f"stop_{direction}_{j}", Location) for j in range(1, leg_length + 1)]
            problem.add_objects(leg_nodes)
            legs.append(leg_nodes)
            
            # Connect first node of leg to the central node
            problem.set_initial_value(connected(hub, leg_nodes[0]), True)
            problem.set_initial_value(connected(leg_nodes[0], hub), True)
            
            # Connect rest of leg nodes in a chain
            for j in range(len(leg_nodes) - 1):
                problem.set_initial_value(connected(leg_nodes[j], leg_nodes[j+1]), True)
                problem.set_initial_value(connected(leg_nodes[j+1], leg_nodes[j]), True)

        # Objects
        car = Object("waymo", Waymo)
        problem.add_object(car)
        problem.set_initial_value(waymo_at(car, hub), True)

        # Passengers
        for p_idx in range(i):
            p_obj = Object(f"passenger_{p_idx}", Passenger)
            problem.add_object(p_obj)

            # Start pos
            start_leg = legs[p_idx % 3]
            end_leg = legs[(p_idx + 1) % 3]
            
            problem.set_initial_value(passenger_at(p_obj, start_leg[-1]), True)
            problem.add_goal(passenger_at(p_obj, end_leg[-1]))

        # Export
        writer = PDDLWriter(problem)
        if i == 1:
            writer.write_domain(os.path.join(directory, "domain.pddl"))
        writer.write_problem(os.path.join(directory, f"problem{i}.pddl"))

    print(f"DONE DONE YAY YAY :D slapped thingies in {directory}/")

if __name__ == "__main__":
    generate_q2_waymo()