import json

'''
This module provides the functions to manage the belief base of the agent. 
Main functions:
1. Load Beliefs: load all the beliefs from the json to python dict.
2. Save Beliefs: save all the beliefs from python dict to json.
3. Add Belief: add a new belief to the belief set.
4. Remove Belief: remove a belief from the belief set.
'''

def load_beliefs(file_path):
    try:
        with open(file_path, 'r') as f:
            beliefs = json.load(f)
        return beliefs
    except FileNotFoundError:
        print(f"Belief file '{file_path}' not found. Starting with an empty belief set.")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{file_path}'. Starting with an empty belief set.")
        return {}

def save_beliefs(beliefs, file_path):
    with open(file_path, 'w') as f:
        json.dump(beliefs, f, indent=4)

def add_belief(beliefs, belief):
    if belief not in beliefs:
        beliefs.append(belief)
        print(f"Added belief: '{belief}'")
    else:
        print(f"Belief '{belief}' already exists.")

def remove_belief(beliefs, belief):
    if belief in beliefs:
        beliefs.remove(belief)
        print(f"Removed belief: '{belief}'")
    else:
        print(f"Belief '{belief}' not found.")