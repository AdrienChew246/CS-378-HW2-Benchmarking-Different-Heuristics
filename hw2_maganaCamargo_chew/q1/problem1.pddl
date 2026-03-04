(define (problem waymo-problem)
 (:domain waymo-domain)
 (:objects
   waymo - waymo_0
   stop_0 stop_1 stop_2 - location
   passenger - passenger_0
 )
 (:init
              (waymo_at waymo stop_0)
              (passenger_at passenger stop_0)
              (connected stop_0 stop_1)
              (connected stop_1 stop_0)
              (connected stop_1 stop_2)
              (connected stop_2 stop_1)
 )
 (:goal (and 
           (passenger_at passenger stop_2)
        )
 )
)
