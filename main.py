import json
import os

from openai import OpenAI
client = OpenAI()

temp = 0.2
reps = 1
max_tokens = 64

def perform_tasks():
    # Perform analysis for each model in the list
    # Perform according to the number of reps
    dir_path = "files/task_files"
    for task_file in os.listdir(dir_path):
        with open(os.path.join(dir_path, task_file)) as file:
            task_file_name = task_file
            task_file = file.read().replace('\n', '')

        models_list = open("files/models.txt").read().split("\n")
        for model in models_list:
            with open("files/responses/" + model.replace("-", "_") + "_" + str(temp) + "_" + task_file_name.replace(".txt", ".json"), 'a') as response_file:
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

def perform_analysis():
    dir_path = "files/responses"
    for file in os.listdir(dir_path):
        response_json = json.load(open(os.path.join(dir_path, file)))
        model_substring = file[:file.find('_') + 1]
        with open("files/results" + model_substring + ".txt", 'w') as results_file:
            log_path = "files/logical_conclusions"
            correct_logic = open(os.path.join(dir_path, ""))









perform_analysis()