import csv
import json
import os
from dotenv import load_dotenv
from datetime import datetime

from openai import OpenAI
load_dotenv()
client = OpenAI()

temp = 0.5
reps = 10
max_tokens = 64
dir_path = "files/task_files"

def perform_all_tasks(header_y_n):
    if(header_y_n == True):
        with open("files/results/result.csv", 'a') as csv_file:
            header = ['date', 'model', 'temperature', 'cover_story', 'modus_ponens', 'modus_tollens', 'affirming_the_consequent', 'denying_the_antecedent']
            writer = csv.writer(csv_file)
            writer.writerow(header)
    perform_task_1()
    perform_task_2()
    perform_task_3()
    perform_task_4()
    perform_task_5()

def perform_task_1():
    file_name = "task_1.txt"
    with open(os.path.join(dir_path, file_name)) as file:
        task_file = file.read().replace('\n', '')
    models_list = open("files/models.txt").read().split("\n")
    for model in models_list:
        with open("files/results/result.csv", 'a') as csv_file:
            for x in range(reps):
                completion = client.chat.completions.create(
                    model=model,
                    response_format={"type": "json_object"},
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": task_file}
                    ],
                    temperature=temp,
                    max_tokens=max_tokens,
                )
                print(completion.choices[0].message.content)
                json_resp = json.loads(completion.choices[0].message.content)
                observation = [datetime.utcnow().strftime("%Y-%m-%d~%H:%M:%S"), model, temp, file_name, 0, 0, 0, 0]
                # Header format, date, model, temperature, cover_story, modus_ponens, modus_tollens, affirming_the_consequent, denying_the_antecedent
                if json_resp["param1"].lower() == "yes":
                    observation[4] = 1
                    # modus ponens
                if json_resp["param2"].lower() == "yes":
                    observation[7] = 1
                    # denying the antecedent
                if json_resp["param3"].lower() == "yes":
                    observation[6] = 1
                    # affirming the consequent
                if json_resp["param4"].lower() == "yes":
                    observation[5] = 1
                    # modus tollens
                writer = csv.writer(csv_file)
                writer.writerow(observation)
                print(observation)


def perform_task_2():
    file_name = "task_2.txt"
    with open(os.path.join(dir_path, file_name)) as file:
        task_file = file.read().replace('\n', '')
    models_list = open("files/models.txt").read().split("\n")
    for model in models_list:
        with open("files/results/result.csv", 'a') as csv_file:
            for x in range(reps):
                completion = client.chat.completions.create(
                    model=model,
                    response_format={"type": "json_object"},
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": task_file}
                    ],
                    temperature=temp,
                    max_tokens=max_tokens,
                )
                print(completion.choices[0].message.content)
                json_resp = json.loads(completion.choices[0].message.content)
                observation = [datetime.utcnow().strftime("%Y-%m-%d~%H:%M:%S"), model, temp, file_name, 0, 0, 0, 0]
                # Header format: date, model, temperature, cover_story, modus_ponens, modus_tollens, affirming_the_consequent, denying_the_antecedent
                if json_resp["param1"].lower() == "yes":
                    observation[4] = 1
                    # modus ponens
                if json_resp["param2"].lower() == "yes":
                    observation[7] = 1
                    # denying the antecedent
                if json_resp["param3"].lower() == "yes":
                    observation[6] = 1
                    # affirming the consequent
                if json_resp["param4"].lower() == "yes":
                    observation[5] = 1
                    # modus tollens
                writer = csv.writer(csv_file)
                writer.writerow(observation)
                print(observation)

def perform_task_3():
    file_name = "task_3.txt"
    with open(os.path.join(dir_path, file_name)) as file:
        task_file = file.read().replace('\n', '')
    models_list = open("files/models.txt").read().split("\n")
    for model in models_list:
        with open("files/results/result.csv", 'a') as csv_file:
            for x in range(reps):
                completion = client.chat.completions.create(
                    model=model,
                    response_format={"type": "json_object"},
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": task_file}
                    ],
                    temperature=temp,
                    max_tokens=max_tokens,
                )
                print(completion.choices[0].message.content)
                json_resp = json.loads(completion.choices[0].message.content)
                observation = [datetime.utcnow().strftime("%Y-%m-%d~%H:%M:%S"), model, temp, file_name, 0, 0, 0, 0]
                # Header format: date, model, temperature, cover_story, modus_ponens, modus_tollens, affirming_the_consequent, denying_the_antecedent
                if json_resp["param1"].lower() == "yes":
                    observation[4] = 1
                    # modus ponens
                if json_resp["param2"].lower() == "yes":
                    observation[5] = 1
                    # modus tollens
                if json_resp["param3"].lower() == "yes":
                    observation[6] = 1
                    # affirming the consequent
                if json_resp["param4"].lower() == "yes":
                    observation[7] = 1
                    # denying the antecedent
                writer = csv.writer(csv_file)
                writer.writerow(observation)
                print(observation)


def perform_task_4():
    file_name = "task_4.txt"
    with open(os.path.join(dir_path, file_name)) as file:
        task_file = file.read().replace('\n', '')
    models_list = open("files/models.txt").read().split("\n")
    for model in models_list:
        with open("files/results/result.csv", 'a') as csv_file:
            for x in range(reps):
                completion = client.chat.completions.create(
                    model=model,
                    response_format={"type": "json_object"},
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": task_file}
                    ],
                    temperature=temp,
                    max_tokens=max_tokens,
                )
                print(completion.choices[0].message.content)
                json_resp = json.loads(completion.choices[0].message.content)
                observation = [datetime.utcnow().strftime("%Y-%m-%d~%H:%M:%S"), model, temp, file_name, 0, 0, 0, 0]
                # Header format: date, model, temperature, cover_story, modus_ponens, modus_tollens, affirming_the_consequent, denying_the_antecedent
                if json_resp["param1"].lower() == "yes":
                    observation[7] = 1
                    # denying the antecedent
                if json_resp["param2"].lower() == "yes":
                    observation[4] = 1
                    # modus ponens
                if json_resp["param3"].lower() == "yes":
                    observation[6] = 1
                    # affirming the consequent
                if json_resp["param4"].lower() == "yes":
                    observation[5] = 1
                    # modus tollens
                writer = csv.writer(csv_file)
                writer.writerow(observation)
                print(observation)


def perform_task_5():
    file_name = "task_5.txt"
    with open(os.path.join(dir_path, file_name)) as file:
        task_file = file.read().replace('\n', '')
    models_list = open("files/models.txt").read().split("\n")
    for model in models_list:
        with open("files/results/result.csv", 'a') as csv_file:
            for x in range(reps):
                completion = client.chat.completions.create(
                    model=model,
                    response_format={"type": "json_object"},
                    messages=[
                        {"role": "system", "content": ""},
                        {"role": "user", "content": task_file}
                    ],
                    temperature=temp,
                    max_tokens=max_tokens,
                )
                print(completion.choices[0].message.content)
                json_resp = json.loads(completion.choices[0].message.content)
                observation = [datetime.utcnow().strftime("%Y-%m-%d~%H:%M:%S"), model, temp, file_name, 0, 0, 0, 0]
                # Header format: date, model, temperature, cover_story, modus_ponens, modus_tollens, affirming_the_consequent, denying_the_antecedent
                if json_resp["param1"].lower() == "yes":
                    observation[7] = 1
                    # denying the antecedent
                if json_resp["param2"].lower() == "yes":
                    observation[6] = 1
                    # affirming the consequent
                if json_resp["param3"].lower() == "yes":
                    observation[4] = 1
                    # modus ponens
                if json_resp["param4"].lower() == "yes":
                    observation[5] = 1
                    # modus tollens
                writer = csv.writer(csv_file)
                writer.writerow(observation)
                print(observation)

if __name__ == '__main__':
    perform_all_tasks(False)
