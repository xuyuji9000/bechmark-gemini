# Terminal-Bench 2.0: Minimum Machine Specifications

While the creators of Terminal-Bench 2.0 (and its execution framework, **Harbor**) do not explicitly publish strict minimum hardware requirements, the underlying architecture dictates what you will need. The benchmark relies heavily on Docker containers to isolate and evaluate tasks. 

Here is a practical breakdown of the minimum specifications required to run Terminal-Bench 2.0 effectively.

---

## 1. Local Execution Requirements

When running the benchmark locally, your hardware needs will scale depending on how many tasks you evaluate concurrently (using the `--n-concurrent` flag).

### Minimum Hardware
* **CPU:** Modern multi-core processor (4 cores minimum). You need sufficient threads to manage Docker daemons and concurrent Python asynchronous tasks.
* **RAM:** 
  * **8 GB minimum** (bare minimum for single-thread/low concurrency execution).
  * **16 GB - 32 GB recommended** if you are running the default 4+ concurrent tasks.
* **Storage:** **20 GB - 30 GB of free disk space**. Harbor pulls various Docker images tailored for different tasks (compiling code, databases, servers), which can accumulate space quickly.
* **GPU:** **None required.** The benchmark uses API calls to frontier LLM models (e.g., Anthropic, OpenAI) so local inference hardware is not necessary unless you explicitly choose to run a local LLM backend.

### Software Prerequisites
* **Operating System:** Linux, macOS, or Windows (via WSL2).
* **Python:** Python 3.10+ (using `pip` or `uv`).
* **Docker:** Docker Desktop or Docker Engine installed and running.

---

## 2. Cloud Execution Alternative

If your local machine does not meet the requirements or you wish to scale massively (e.g., `--n-concurrent 100`), the **Harbor framework** natively supports cloud execution.

By utilizing cloud workspace providers, the heavy lifting of container execution is offloaded.
* **Providers supported:** Daytona, Modal, Blaxel, Novita Sandbox, etc.
* **Local requirement in this mode:** Any basic machine capable of running a lightweight Python script and making API calls to orchestrate the remote environments. 

*(Example: Adding `--env daytona` to your Harbor run command offloads execution to Daytona's infrastructure).*
