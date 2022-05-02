RODOLFO DIAZ
==============================

This program can compute basic statistics for a collection of numbers 0<x<1000, where x is an integer.

Getting Started
------------


No external libraries needed.
Python >= 3.8.10

1. Clone this repository:
   ```sh
   git clone https://github.com/AbelardoDV/rdiaz_challenge.git
   ```
2. cd to the project:
   ```sh
   cd rdiaz_challenge/
   ```
3. Run production
   ```sh
   python run.py
   ```
4. Run tests
   ```sh
   python -m unittest
   ```

Project Structure
------------

    ├── README.md
    |
    ├── run.py                            <- Executable script to perform example inputs from challenge instructions
    |
    ├── app
    │   │
    │   ├── statistics.py                 <- Holds 2 Models: DataCapture and StatsEngine
    │   │
    │   └── validators                    
    |       |
    │       └── inputvalidator.py         <- Decorator: valid_input(), makes sure that inputs are  0<x<1000 and int
    │
    │
    └── test       
        │
        ├── test_statistics.py
        |
        └── test_validators
              |
              └── test_inputvalidator.py       
