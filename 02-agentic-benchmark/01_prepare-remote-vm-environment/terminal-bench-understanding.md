# Terminal-Bench Overview

**Terminal-Bench** is an evaluation benchmark designed to test AI agents and Large Language Models (LLMs) on complex, real-world tasks within a terminal environment. 

Developed primarily by the Laude Institute and distributed via the `harbor-framework` organization on GitHub, it evaluates how autonomously agents can handle system-level reasoning tasks, such as compiling code, training machine learning models, and setting up servers. 

The benchmark consists of two main components:
1. **A Dataset of Tasks:** Real-world, end-to-end challenges.
2. **An Execution Harness:** A system that connects a language model directly to a terminal sandbox for execution and grading.

---

## Versions and Variants

### 1. Terminal-Bench (v1)
* **Status:** Beta
* **Description:** The original framework featuring a dataset of approximately 100 tasks designed to test agent capabilities in text-based environments.
* **Distribution:** Available as a Python package via PyPI (`pip install terminal-bench`).
* **Latest PyPI Release:** `0.2.18` (Includes versions from `0.1.0` through `0.2.17`).
* **Repository:** [harbor-framework/terminal-bench](https://github.com/harbor-framework/terminal-bench)

### 2. Terminal-Bench 2.0
* **Description:** The next generation of the benchmark. The maintainers have directed new users toward version 2.0.
* **Execution Framework:** Designed to be run using their newly released **Harbor** framework, standardizing how agents interact with the evaluation environment.
* **Repository:** [harbor-framework/terminal-bench-2](https://github.com/harbor-framework/terminal-bench-2)

### 3. Terminal-Bench Science
* **Description:** A specialized, domain-specific variant of the benchmark.
* **Focus:** It strictly evaluates AI agents on complex, real-world scientific workflows and bioinformatics pipelines directly within the terminal.
* **Repository:** [harbor-framework/terminal-bench-science](https://github.com/harbor-framework/terminal-bench-science)

---

## Key Links
* **Harbor Framework:** [harbor-framework/harbor](https://github.com/harbor-framework/harbor)
* **Official Docs:** [tbench.ai/docs](https://www.tbench.ai/docs)
