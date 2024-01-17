# ProblemGraderMatchTool
A tool for matching names of graders to problem numbers

## Requirements
Python 3 or greater


## How to use
Within the json config file, we have the following: 
```
{
  "graders": ["Bob",
              "Tim",
              "Joe"],
  "problems": ["0",
               "1",
               "1a",
               "1b"]
}
```
In the list of graders, enter the names of the graders for the assigment. In the list of problems, enter 
the problem numbers. Then run the main.py file. The output of the script is the following:
```
Provided config file info: 
Grader names: ['Bob', 'Tim', 'Joe']
Problems: ['0', '1', '1a', '1b']

Results: 
{'Bob': ['0'], 'Joe': ['1a'], 'Tim': ['1', '1b']}
```