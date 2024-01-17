"""
main.py
Created Jan. 16 2024
Purpose: match names from a json file to problem numbers
"""

####################

# Import packages
import pprint
import json
import random
from typing import List

####################

# Global/Config variables
CONFIG_JSON_PATH: str = "config.json"

####################

def match_names_to_problems(list_names: List[str], list_problems: List[str]):
    results = {name: [] for name in list_names}

    # Shuffle names
    temp_list_names = list(list_names)
    random.shuffle(temp_list_names)

    for problem in list_problems:
        grader_name = temp_list_names.pop()
        results[grader_name].append(problem)
        # Reshuffle names if more problems than graders
        if not temp_list_names:
            temp_list_names = list(list_names)
            random.shuffle(temp_list_names)
    return results

####################
def main():
    # Load config file
    with open(CONFIG_JSON_PATH, 'r') as j:
        config_json = json.loads(j.read())
    list_names = config_json["graders"]
    list_problems = config_json["problems"]
    print("Provided config file info: ")
    print("Grader names: {}".format(list_names))
    print("Problems: {}".format(list_problems))

    # Match problems to graders
    results = match_names_to_problems(list_names, list_problems)
    print("\n"+"Results: ")
    pprint.pprint(results)

####################

if __name__ == "__main__":
    main()