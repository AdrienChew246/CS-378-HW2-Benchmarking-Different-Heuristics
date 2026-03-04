(define (problem waymo-problem)
 (:domain waymo-domain)
 (:objects
   waymo_01 - waymo
   stop_0 stop_1 stop_2 stop_3 - location
   passenger_01 - passenger
 )
 (:init
              (waymo_at waymo_01 stop_0)
              (passenger_at passenger_01 stop_0)
              (connected stop_0 stop_1)
              (connected stop_1 stop_0)
              (connected stop_1 stop_2)
              (connected stop_2 stop_1)
              (connected stop_2 stop_3)
              (connected stop_3 stop_2)
 )
 (:goal (and 
           (passenger_at passenger_01 stop_3)
        )
 )
)
