### CS 378: Automated Planning for Robots
# HW 2: Understanding the Limits of Classical Heuristics
### Spring 2026
### Lecturer: Erez Karpas
### TA: Talal Ayman

In this homework assignment you will explore the limits of classical planning heuristics

You will use the [Fast Downward](https://www.fast-downward.org/) planner, a state-of-the-art planner, which will allow us to solve planning problems with many different heuristics. 

To run the planner, see the [quick start](https://www.fast-downward.org/latest/documentation/quick-start/). You can pick your favorite method to install and run the planner.

For example, using the **Apptainer** method, you can pull the Fast Downward image with:
```
apptainer pull fast-downward.sif docker://aibasel/downward:latest
```
Then run the planner with:
```
./fast-downward.sif <domain.pddl> <problem.pddl> --search <search_method>
```

Alternatively, if you build from **source code**, you can run the planner with:
```
fast-downward.py <domain.pddl> <problem.pddl> --search <search_method>
```

### General Instructions

In this homework exercise, you will create several _families_ of planning problems. A _family_ is a set of planning problems that share the same domain and different instances of increasing size. 

For the purposes of this homework exercise, each family will contain 5 planning problems of increasing size. You will need to submit the PDDL files for each family, as well as a report in PDF, which will be described below. Remember that you can use the Unified Planning Framework to generate PDDL files, by using the [PDDL Writer](https://unified-planning.readthedocs.io/en/latest/interoperability.html#id3).

**You are required to solve 2 out of the 4 questions below (your choice). Solving a 3rd question is optional and worth 15% extra credit.**

Your objective is to create families of planning problems for which some heuristics are either accurate or very inaccurate. For the purposes of this exercise, we will measure the accuracy of a heuristic on a given problem by the ratio between its estimate of the heuristic state and the actual cost of an optimal solution to the problem. 

* A heuristic is considered *accurate* if this ratio is 1. 
* A heuristic is considered *very inaccurate* if this ratio decreases as the size of the problem increases.

To measure this using Fast Downward, call Fast Downward on your PDDL files as follows (using Apptainer as an example):
```
./fast-downward.sif <domain.pddl> <problem.pddl> --search <search_method>
```

You will then see output that looks like
```
...
[t=0.003024s, 10276 KB] Initial heuristic value for cea: 16
...
[t=0.004530s, 10276 KB] Plan cost: 34
...
```

The initial heuristic value can be found in the line:
```
Initial heuristic value for cea: 16
```

The plan cost can be found in the line:
```
Plan cost: 34
```

So in this case the ratio is 16/34 = 0.47

#### Q1

In this question, you will create a family of planning problems for which the relaxed plan heuristic is accurate.

To call fast downward with GBFS and the relaxed plan heuristic, use the following command:
```
fast-downward.py <domain.pddl> <problem.pddl> --search "eager_greedy([ff()])"
```

#### Q2

In this question, you will create a family of planning problems for which the relaxed plan heuristic is inaccurate.

Use the same search algorithm and heuristc as in Q1.

#### Q3

In this question, you will create a family of planning problems for which the causal graph heuristic is accurate.

To call fast downward with GBFS and the relaxed plan heuristic, use the following command:
```
fast-downward.py <domain.pddl> <problem.pddl> --search "eager_greedy([cg()])"
```

#### Q4

In this question, you will create a family of planning problems for which the causal graph heuristic is inaccurate.

Use the same search algorithm and heuristc as in Q3.

### Report

In your report, you should (a) describe the family of planning problems you created for each questions, and (b) include a table showing the initial heuristic value, the plan cost, and their ratio for each planning problem in each question. You should also include a plot showing the ratio for each question.

### Submission

Submit a zip file named `hw2_lastname1_lastname2.zip` which unzips to the following structure:

```
hw2_lastname1_lastname2/
├── report.pdf
├── q_/
│   ├── domain.pddl
│   ├── problem1.pddl
│   ├── problem2.pddl
│   ├── problem3.pddl
│   ├── problem4.pddl
│   └── problem5.pddl
├── q_/
│   ├── domain.pddl
│   ├── problem1.pddl
│   ├── ...
└── q_/  (optional, extra credit)
    ├── ...
```

Replace `q_` with the question numbers you chose (e.g., `q1`, `q3`, `q4`).
