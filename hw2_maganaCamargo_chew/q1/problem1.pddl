(define (problem waymo-problem)
 (:domain waymo-domain)
 (:objects
   waymo_01 - waymo
   stop_0 stop_1 - location
   passenger_01 - passenger
 )
 (:init
              (waymo_at waymo_01 stop_0)
              (passenger_at passenger_01 stop_0)
              (connected stop_0 stop_1)
              (connected stop_1 stop_0)
 )
 (:goal (and 
           (passenger_at passenger_01 stop_1)
        )
 )
)
