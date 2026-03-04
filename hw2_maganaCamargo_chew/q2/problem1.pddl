(define (problem waymo_2_electric_boogaloo-problem)
 (:domain waymo_2_electric_boogaloo-domain)
 (:objects
   waymo - waymo_0
   stop_0 stop_n_1 stop_n_2 stop_s_1 stop_s_2 stop_e_1 stop_e_2 stop_w_1 stop_w_2 - location
   passenger - passenger_0
 )
 (:init
              (connected stop_0 stop_n_1)
              (connected stop_n_1 stop_0)
              (connected stop_n_1 stop_n_2)
              (connected stop_n_2 stop_n_1)
              (connected stop_0 stop_s_1)
              (connected stop_s_1 stop_0)
              (connected stop_s_1 stop_s_2)
              (connected stop_s_2 stop_s_1)
              (connected stop_0 stop_e_1)
              (connected stop_e_1 stop_0)
              (connected stop_e_1 stop_e_2)
              (connected stop_e_2 stop_e_1)
              (connected stop_0 stop_w_1)
              (connected stop_w_1 stop_0)
              (connected stop_w_1 stop_w_2)
              (connected stop_w_2 stop_w_1)
              (waymo_at waymo stop_0)
              (passenger_at passenger stop_n_2)
 )
 (:goal (and 
           (passenger_at passenger stop_s_2)
        )
 )
)
