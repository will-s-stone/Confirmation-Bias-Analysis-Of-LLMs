import os
import re
import json
import csv
from datetime import datetime


def get_cover_story(n):
    cover_story = ""
    if n > 5:
        raise ValueError("Cover Story Undefined")
    match n:
        case 1:
            print("task file one")
            cover_story = "task_1.txt"
        case 2:
            print("task file two")
            cover_story = "task_2.txt"
        case 3:
            print("task file three")
            cover_story = "task_3.txt"
        case 4:
            print("task file four")
            cover_story = "task_4.txt"
        case 5:
            print("task file five")
            cover_story = "task_5.txt"
    file_path = os.path.abspath(
        os.path.join(os.path.join(os.pardir, os.path.join("files", "task_files")), cover_story))
    with open(file_path, 'r') as file:
        formatted_cover_story = file.read().replace('\n', '')
    return formatted_cover_story


def _get_json_substring(input_string):
    input_string = str(input_string)
    new_input_string = input_string.replace('\\n', "")
    match = re.search(r"\{([^}]*)\}", new_input_string)
    if match:
        result = str(match.group(0))
        print("json sub output: " + result)
        return result
    return None


def _process_response(cover_story_number, input_string, model, temp):
    file_name = "task_" + str(cover_story_number)
    response = _get_json_substring(input_string)
    json_resp = json.loads(response)
    observation = [datetime.utcnow().strftime("%Y-%m-%d~%H:%M:%S"), model, temp, file_name, 0, 0, 0, 0]
    if cover_story_number == 1:
        if json_resp["card1"].lower() == "yes":
            observation[4] = 1
            # modus ponens
        if json_resp["card2"].lower() == "yes":
            observation[7] = 1
            # denying the antecedent
        if json_resp["card3"].lower() == "yes":
            observation[6] = 1
            # affirming the consequent
        if json_resp["card4"].lower() == "yes":
            observation[5] = 1
            # modus tollens
    elif cover_story_number == 2:
        if json_resp["room1"].lower() == "yes":
            observation[4] = 1
            # modus ponens
        if json_resp["room2"].lower() == "yes":
            observation[7] = 1
            # denying the antecedent
        if json_resp["room3"].lower() == "yes":
            observation[6] = 1
            # affirming the consequent
        if json_resp["room4"].lower() == "yes":
            observation[5] = 1
            # modus tollens
    elif cover_story_number == 3:
        if json_resp["user1"].lower() == "yes":
            observation[4] = 1
            # modus ponens
        if json_resp["user2"].lower() == "yes":
            observation[5] = 1
            # modus tollens
        if json_resp["user3"].lower() == "yes":
            observation[6] = 1
            # affirming the consequent
        if json_resp["user4"].lower() == "yes":
            observation[7] = 1
            # denying the antecedent
    elif cover_story_number == 4:
        if json_resp["fabric1"].lower() == "yes":
            observation[7] = 1
            # denying the antecedent
        if json_resp["fabric2"].lower() == "yes":
            observation[4] = 1
            # modus ponens
        if json_resp["fabric3"].lower() == "yes":
            observation[6] = 1
            # affirming the consequent
        if json_resp["fabric4"].lower() == "yes":
            observation[5] = 1
            # modus tollens
    elif cover_story_number == 5:
        if json_resp["person1"].lower() == "yes":
            observation[7] = 1
            # denying the antecedent
        if json_resp["person2"].lower() == "yes":
            observation[6] = 1
            # affirming the consequent
        if json_resp["person3"].lower() == "yes":
            observation[4] = 1
            # modus ponens
        if json_resp["person4"].lower() == "yes":
            observation[5] = 1
            # modus tollens
    else:
        raise ValueError("Cover Story Number Error")
    return observation


def log_observation(cover_story_number, response, model, temp):
    observation = _process_response(cover_story_number, response, model, temp)
    file_path = os.path.abspath(os.path.join(os.path.join(os.pardir, os.path.join("files", "results")), "results.csv"))
    with open(file_path, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(observation)


