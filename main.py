import csv
import json
import os
from dotenv import load_dotenv

from openai import OpenAI
load_dotenv()
client = OpenAI()

temp = 0.7
reps = 30
max_tokens = 64

def perform_tasks():
    dir_path = "files/task_files"
    for task_file in os.listdir(dir_path):
        with open(os.path.join(dir_path, task_file)) as file:
            task_file_name = task_file
            task_file = file.read().replace('\n', '')

        models_list = open("files/models.txt").read().split("\n")
        for model in models_list:
            with open("files/responses/" + task_file_name.replace(".txt", "_") + model.replace("-", "_") + "_" + str(temp) + ".json", 'w') as response_file:
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
                    response_file.write(completion.choices[0].message.content)

def write_results():
    dir_path = "files/responses"
    for file in os.listdir(dir_path):
        response_json = json.load(open(os.path.join(dir_path, file)))
        model_substring = '_'.join((file.split('_'))[2:-1])
        task_substring = '_'.join((file.split('_'))[:2])
        print(model_substring)
        with open("files/results/" + model_substring + ".txt", 'a') as results_file:
            log_path = "files/logical_conclusions"
            correct_logic = json.load(open(os.path.join(log_path, "correct_logic/" + task_substring + ".json")))
            affirming_consequent_logic = json.load(open(os.path.join(log_path, "affirming_consequent/" + task_substring + ".json")))
            denying_antecedent_logic = json.load(open(os.path.join(log_path, "denying_antecedent/" + task_substring + ".json")))
            if response_json == correct_logic:
                results_file.write("On " + task_substring + " it did the correct logic\n")
            elif response_json == affirming_consequent_logic:
                results_file.write("On " + task_substring + " it affirmed the consequent\n")
            elif response_json == denying_antecedent_logic:
                results_file.write("On " + task_substring + " it denied the antecedent\n")
            else:
                results_file.write("On " + task_substring + " it was unpredictable\n")


def perform_analysis():
    dir_path = "files/responses"
    for file in os.listdir(dir_path):
        response_json = json.load(open(os.path.join(dir_path, file)))
        model_substring = '_'.join((file.split('_'))[2:-1])
        task_substring = '_'.join((file.split('_'))[:2])
        print(model_substring)
        with open("files/results/" + model_substring + ".txt", 'a') as results_file:
            log_path = "files/logical_conclusions"
            correct_logic = json.load(open(os.path.join(log_path, "correct_logic/" + task_substring + ".json")))
            affirming_consequent_logic = json.load(open(os.path.join(log_path, "affirming_consequent/" + task_substring + ".json")))
            denying_antecedent_logic = json.load(open(os.path.join(log_path, "denying_antecedent/" + task_substring + ".json")))
            if response_json == correct_logic:
                results_file.write("On " + task_substring + " it did the correct logic\n")
            elif response_json == affirming_consequent_logic:
                results_file.write("On " + task_substring + " it affirmed the consequent\n")
            elif response_json == denying_antecedent_logic:
                results_file.write("On " + task_substring + " it denied the antecedent\n")
            else:
                results_file.write("On " + task_substring + " it was unpredictable\n")


if __name__ == '__main__':
    perform_tasks()
