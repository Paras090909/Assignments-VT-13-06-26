# PROJECT SIMULATION REPORT

Generated dynamically from simulation outputs.

## Executive Summary

This document compiles the problem statements, mathematical approaches, and actual results for the three simulation assignments: Smart Epidemic Spread Simulator, AI Population Growth Analyzer, and Smart Investment Predictor.

## Assignment 1: Smart Epidemic Spread Simulator

### Problem Statement
- Initial infected people: 10
- Everyday, each infected person infects 2 new people.
- Daily recovery rate: 15% of infected people recover.
- Recovered people cannot be infected again.
- Tasks: Simulate 60 days, find total infected, total recovered, and the day active infections exceed 1 million.

### Solution Approach
- **Active infected** \(I_t\) grows exponentially:
  \[I_t = I_{t-1} + 2 I_{t-1} - 0.15 I_{t-1} = 2.85 I_{t-1}\]
- **Recovered people** \(R_t\) accumulates recoveries:
  \[R_t = R_{t-1} + 0.15 I_{t-1}\]
- **Cumulative infections** \(C_t\) logs the total contracted cases:
  \[C_t = I_t + R_t = C_{t-1} + 2 I_{t-1}\]

### Results
- **Final Day 60 Active Infected**: 19,529,521,405,632,804,706,819,506,176.00 (~19,529,521,405,632,804,706,819,506,176)
- **Final Day 60 Total Recovered**: 1,583,474,708,564,821,735,806,861,312.00 (~1,583,474,708,564,821,735,806,861,312)
- **Final Day 60 Cumulative Cases**: 21,112,996,114,197,623,144,091,484,160.00 (~21,112,996,114,197,623,144,091,484,160)
- **Day Active Infections Exceeded 1 Million**: Day 11.0
- **Day Cumulative Infections Exceeded 1 Million**: Day 11.0

## Assignment 2: AI Population Growth Analyzer

### Problem Statement
- Initial population: 50,000 residents.
- Population increases by 7% annually.
- Migration decreases population by 2% annually.
- Tasks: Simulate 50 years, find ending population and the first year population exceeds 1 million.

### Solution Approach
- Net annual compounding growth rate = \(7\% - 2\% = 5\%\).
- Population \(P_t\) in year \(t\) is simulated as:
  \[P_t = P_{t-1} \times (1 + 0.07 - 0.02) = P_{t-1} \times 1.05\]

### Results
- **Year 50 Population**: 573,369.99 (~573,370)
- **Year Population Exceeds 1 Million**: Year 62 (Population: 1,029,690)

## Assignment 3: Smart Investment Predictor

### Problem Statement
- Initial investment: ₹1,00,000.
- Annual return: Between 8% and 15% randomly.
- Tasks: Simulate for 30 years, run 1,000 simulations, and find the best, worst, and average outcomes.

### Solution Approach
- **Monte Carlo Simulation**: Execute 1,000 independent simulation paths.
- For each path, capital grows annually for 30 years:
  \[V_y = V_{y-1} \times (1 + r_y)\]
  where \(r_y \sim U(0.08, 0.15)\) (uniformly distributed random rate of return).
- Statistically analyze ending balances to determine minimum, maximum, mean, and median outcomes.

### Results
- **Best Outcome (Max)**: Rs. 3,596,130.28
- **Worst Outcome (Min)**: Rs. 1,912,181.25
- **Average Outcome (Mean)**: Rs. 2,618,507.40
- **Median Outcome**: Rs. 2,609,575.85
