# Spring_2025_AI_Assignment_2

This repository contains implementations of classical search and optimization algorithms applied to various environments including Frozen Lake and the Traveling Salesman Problem (TSP). Visualizations and performance metrics are also provided to analyze and compare the efficiency of each method.

## Contributors:
- CS22B028 Johri Aniket Manish
- CS22B024 Harshit Garg

## How to Run

1. Clone the repository
```bash
git clone https://github.com/Error-404-NotFound/AI_Assignment_2.git
```
2. Go to the cloned repository
```bash
cd AI_Assignment_2
```
3. Ensure Python is installed
```bash
python --version # Output: Python 3.12.4
```
4. Create a virtual environment and activate it
```bash
python -m venv AI
```
> [!TIP]
> For Linux:
>```bash
>source AI/bin/activate
>```
>For Windows:
>```bash
>AI\Scripts\activate.bat
>```
5. Install dependencies
```bash
pip install -r requirements.txt
```
6. Run main.py
```bash
python main.py
```
## Implemented Algorithms

- **DFBnB (Depth-First Branch and Bound)**  
  Efficient tree-based search for pathfinding in environments like Frozen Lake.

- **IDA\*** (Iterative Deepening A*)  
  Combines depth-first and heuristic search to balance memory and performance.

- **Hill Climbing**  
  Greedy optimization approach for improving tour cost in TSP.

- **Simulated Annealing**  
  Probabilistic optimization technique for escaping local minima in TSP.

## Environments

- **Frozen Lake**  
  Grid world used to test search algorithms like DFBnB and IDA*.

- **Traveling Salesman Problem (TSP)**  
  Custom TSP environment from:
  - [VRP-GYM](https://github.com/kevin-schumann/VRP-GYM)
 
## Project Structure

```bash
.
├── results/
│   ├── average_search_times.png
│   ├── dfbnb_frozenlake.gif
│   ├── hc_tour.gif
│   ├── hill_climb_costs.png
│   ├── hill_climb_simulation_across_different_iterations.gif
│   ├── ida_star_frozenlake.gif
│   ├── sa_tour.gif
│   ├── search_times_plot.png
│   ├── simulated_annealing_costs.png
│   ├── simulated_annealing_simulation_across_different_iterations.gif
│   └── times_for_hc_and_sa.png
├── search_algo/
│   ├── __init__.py
│   ├── dfbnb.py
│   ├── helpers.py
│   ├── hill_climb.py
│   ├── ida_star.py
│   └── simulated_annealing.py
├── .gitignore
├── README.md
├── environment.py
├── main.py
├── requirements.txt
└── utils.py
```
