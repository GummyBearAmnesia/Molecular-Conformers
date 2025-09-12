# Population Matrix Simulation

This project simulates the movement of a population between two locations, **A** and **B**, over time using **matrix multiplication**. The code demonstrates concepts from linear algebra such as **matrix multiplication**, **transpose**, **symmetry**, and **stability analysis**.

---

## 🔹 Project Overview

The population is represented as a vector, and their movements between two locations are determined by a **transition probability matrix** `p`. Each iteration simulates the passing of one hour.

* **Task 1:**

  * Computes the population distribution after 1 hour.
  * Checks if the transition matrix is symmetrical (i.e., equal to its transpose).

* **Task 2:**

  * Simulates population distribution over 72 hours (3 days).
  * Checks if the total population is conserved (remains 300).
  * Determines whether the population stabilizes.
  * Extends simulation for 24 more hours to verify long-term stability.

---

## 🔹 Code Explanation

### Transition Matrix

```python
p = np.array([[0.8, 0.1],
              [0.2, 0.9]])
```

* 80% of population in A stays in A, 20% moves to B.
* 90% of population in B stays in B, 10% moves to A.

### Initial Population

```python
pop = np.array([150, 150])
```

* Starting with **150 in A** and **150 in B**.

### Key Steps

1. **Population after 1 hour:**

   ```python
   pPop = np.dot(p, pop)
   ```

   Uses matrix multiplication to compute the new distribution.

2. **Transpose and Symmetry:**

   ```python
   pT = np.transpose(p)
   np.allclose(p, pT)
   ```

   Checks if the transition matrix is symmetrical.

3. **Long-term Simulation (72 hours):**

   ```python
   while n < 73:
       temp = np.dot(p, temp)
   ```

   Iteratively applies the transition matrix to simulate 72 hours.

4. **Conservation of Total Population:**
   Ensures the total remains **300** when rounded.

5. **Stability Check:**
   Extends simulation by 24 more hours to verify if population numbers stop changing significantly.

---

## 🔹 Example Output

```
The population in A after 1 hour is 135
The population in B after 1 hour is 165
The matrix for the population after one hour is [135. 165.]
The transposed matrix of p is [[0.8 0.2]
 [0.1 0.9]]
The matrices are not symmetrical

The population in A after 72 hours is 125
The population in B after 72 hours is 175
The population number of A and B are stable after around 65 hours
The total is always 300 when rounded to the nearest integer
The population number of A and B remains stable even if an extra 24 hours (a full day) is simulated
```

---

## 🔹 Requirements

* Python 3.x
* NumPy

Install NumPy if not already installed:

```bash
pip install numpy
```

---

## 🔹 How to Run

Save the script (e.g., `population_simulation.py`) and run:

```bash
python population_simulation.py
```

---

## 🔹 Key Concepts Covered

* Matrix multiplication
* Transition matrices
* Symmetry of matrices
* Population conservation
* Stability of dynamic systems

