# EC504 Project: Comparing Algorithms to Solve the Vehicle Routing Problem
> Yang Lu, Antonio Alonso, Christopher Gough, Yimin Xu

## How to Run the Code
### Using Make
The Makefile is designed to run on a Linux distribution and was tested on the SCC. Once you've cloned the repository, run:
```
make all
```
This will set up a virtual environment, install the necessary dependencies, and run the two programs. The visualized output graphs will be available as `.png` files in the root directory.

### Requirements
We've configured the codebase to set up all necessary requirements and run the code with a Makefile. The below instructions are for replicating the automated process on your own, and are by no means required.

Ensure you have a recent version (3.6 or higher) of Python installed. We have provided sample data to use for testing the algorithms; if you wish to test on your own, ensure it's properly formatted as a CSV and change the file name on line 104 of `VRP_alg.py` and line 168 of `testingORtools.py`. You'll also need to set up a virtual environment to install the necessary dependencies.
> You don't _need_ to, but for the sake of keeping your PC clean and organized, you really should.

It's very simple. Run the following (for Mac/Linux distros):
```
python -m venv .venv
source .venv/bin/activate
pip install -r code/requirements.txt
```
If you're on a Windows machine, activate the virtual environment with `source .venv/Scripts/activate`.  To deactivate (on any OS) run `deactivate`.

### Running the Code
We've configured each algorithm to run and print their output from a single entrypoint. To test the insertion heuristic, simply run `python code/VRP_alg.py` from the root directory. To test the benchmark OR tools, run `python code/testingORtools.py`. The visualized output graphs will be available as `.png` files in the root directory.

### Presentation link
https://docs.google.com/presentation/d/1zqL0-hHf6ZOdBUKRWEU3CPR2AtTBuGb6sFXqF_0Zv9U/edit?usp=sharing

### Report link
https://docs.google.com/document/d/1yelBcl4w9N3EWt_TEjPo1Go7PxMaTxEcPPINmKHokS0/edit#
Note, a pdf of the report is also saved above.
