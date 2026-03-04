import unified_planning as up
from unified_planning.shortcuts import *
from unified_planning.io import PDDLWriter
import os

def generate_q1_waymo(directory="q3"):
    if not os.path.exists(directory):
        os.makedirs(directory)

    DOMAIN_NAME = "waymo"

    # Size
    for i in range(1, 6):
        n_locations = 2**i 
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

        # Objects
        car = Object("waymo", Waymo)
        person = Object("passenger", Passenger)
        locs = [Object(f"stop_{j}", Location) for j in range(n_locations)]
        problem.add_objects([car, person] + locs)

        # Initial State
        problem.set_initial_value(waymo_at(car, locs[0]), True)
        problem.set_initial_value(passenger_at(person, locs[0]), True)
        
        for j in range(n_locations - 1):
            problem.set_initial_value(connected(locs[j], locs[j+1]), True)
            problem.set_initial_value(connected(locs[j+1], locs[j]), True)
        
        # Goal
        problem.add_goal(passenger_at(person, locs[-1]))

        # Export
        writer = PDDLWriter(problem)
        if i == 1:
            writer.write_domain(os.path.join(directory, "domain.pddl"))
        writer.write_problem(os.path.join(directory, f"problem{i}.pddl"))

    print(f"DONE DONE YAY YAY :D slapped thingies in {directory}/")

if __name__ == "__main__":
    generate_q1_waymo()