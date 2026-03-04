(define (domain waymo-domain)
 (:requirements :strips :typing)
 (:types waymo_0 location passenger_0)
 (:predicates 
             (waymo_at ?v - waymo_0 ?l - location)
             (passenger_at ?p - passenger_0 ?l - location)
             (boarding ?p - passenger_0 ?v - waymo_0)
             (connected ?l1 - location ?l2 - location)
 )
 (:action drive
  :parameters ( ?v - waymo_0 ?l_from - location ?l_to - location)
  :precondition (and (waymo_at ?v ?l_from) (connected ?l_from ?l_to))
  :effect (and (waymo_at ?v ?l_to) (not (waymo_at ?v ?l_from))))
 (:action pickup
  :parameters ( ?v - waymo_0 ?p - passenger_0 ?l - location)
  :precondition (and (waymo_at ?v ?l) (passenger_at ?p ?l))
  :effect (and (boarding ?p ?v) (not (passenger_at ?p ?l))))
 (:action dropoff
  :parameters ( ?v - waymo_0 ?p - passenger_0 ?l - location)
  :precondition (and (waymo_at ?v ?l) (boarding ?p ?v))
  :effect (and (passenger_at ?p ?l) (not (boarding ?p ?v))))
)
