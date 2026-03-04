#!/bin/bash

SUMMARY_FILE="result.txt"
> "$SUMMARY_FILE"

python3 generate_q1.py
python3 generate_q2.py
python3 generate_q3.py
python3 generate_q4.py

do_thingy() {
    local q_num=$1
    local heuristic=$2
    
    echo "Working on q${q_num}..."
    mkdir -p "q${q_num}_results"

    for i in {1..5}; do
        output_file="q${q_num}_results/${i}.txt"
        
        ./fast-downward.sif "q${q_num}/domain.pddl" "q${q_num}/problem${i}.pddl" --search "eager_greedy([${heuristic}()])" > "$output_file"
        
        echo "--- q${q_num} problem ${i} ---" >> "$SUMMARY_FILE"
        grep -E "Plan cost:|Initial heuristic value" "$output_file" >> "$SUMMARY_FILE"
        echo "" >> "$SUMMARY_FILE"
    done
    
    echo "q${q_num} results done!"
}

do_thingy 1 "ff"
do_thingy 2 "ff"
do_thingy 3 "cg"
do_thingy 4 "cg"

echo "ALL DONE!!! look at $SUMMARY_FILE"