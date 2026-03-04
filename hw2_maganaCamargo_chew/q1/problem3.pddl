(define (problem waymo-problem)
 (:domain waymo-domain)
 (:objects
   waymo_01 - waymo
   stop_0 stop_1 stop_2 stop_3 stop_4 stop_5 stop_6 stop_7 - location
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
              (connected stop_3 stop_4)
              (connected stop_4 stop_3)
              (connected stop_4 stop_5)
              (connected stop_5 stop_4)
              (connected stop_5 stop_6)
              (connected stop_6 stop_5)
              (connected stop_6 stop_7)
              (connected stop_7 stop_6)
 )
 (:goal (and 
           (passenger_at passenger_01 stop_7)
        )
 )
)
