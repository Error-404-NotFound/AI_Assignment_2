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
  Grid world used to test search algorithms like DFBnB and IDA*. [Frozen Lake](https://gymnasium.farama.org/environments/toy_text/frozen_lake/) environment is used for these algorithms.

- **Traveling Salesman Problem (TSP)**  
  Custom TSP environment from [VRP-GYM](https://github.com/kevin-schumann/VRP-GYM) is used for optimization algorithms like Hill Climbing and Simulated Annealing.
 
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

## Visualizations

All results and plots are stored in the `results/` directory:
- `*_costs.png`: Cost progression plots for TSP solutions.
- `*_tour.gif`: Animation of tour progression.
- `*_frozenlake.gif`: Search exploration animations on Frozen Lake.
- `*_simulation_across_different_iterations.gif`: Comparative visualizations over iterations.
- `search_times_plot.png`, `average_search_times.png`, `times_for_hc_and_sa.png`: Time analysis of different algorithms.

## search_algo/ – Core Algorithm Implementations

This directory contains the core logic for all the search and optimization algorithms implemented in the project. Each file corresponds to a specific algorithm or shared functionality.

### File Descriptions

- **`dfbnb.py`**  
  Implements the **Depth-First Branch and Bound (DFBnB)** algorithm, a tree-based search technique that prunes paths exceeding the current best-known solution. Used primarily for solving navigation problems like Frozen Lake.

- **`ida_star.py`**  
  Implements the **Iterative Deepening A*** (**IDA\***), which combines the space efficiency of depth-first search with the optimality and heuristics of A*. Suited for large search spaces where A* is memory-intensive.

- **`hill_climb.py`**  
  Contains the **Hill Climbing** algorithm, a local search method that iteratively improves a solution by exploring its neighbors. Applied to the Traveling Salesman Problem (TSP) to minimize tour cost.

- **`simulated_annealing.py`**  
  Implements **Simulated Annealing**, a probabilistic algorithm inspired by the annealing process in metallurgy. It allows worse moves occasionally to escape local minima, making it well-suited for TSP and other complex optimization problems.

- **`helpers.py`**  
  Provides utility functions and shared logic used across multiple algorithms such as heuristic calculations, path cost computations, and neighbor generation.

- **`__init__.py`**  
  Makes the directory a Python package, allowing easy imports from `search_algo` in other parts of the codebase (e.g., `from search_algo import dfbnb`).

These implementations are modular and designed to work with various environments defined in `environment.py`, supporting experiments in grid-based navigation and TSP optimization.

## Conclusion

This project demonstrates the application of both classical search algorithms and modern optimization techniques across different environments. Through experiments and visualizations, it highlights the strengths, limitations, and performance trade-offs of each approach.

Whether you're navigating a frozen grid or optimizing a TSP route, this repo serves as a comprehensive educational resource for understanding and comparing:

- Informed vs uninformed search strategies
- Greedy local search vs probabilistic exploration
- Time and cost efficiency of different algorithms

Feel free to explore, modify, and extend the implementations for your own experiments or learning purposes.

---

**Questions or Suggestions?**  
Open an issue or reach out via discussions!


