from openai import OpenAI
client = OpenAI()

temp = 0.2
reps = 2
max_tokens = 64

def perform_analysis():
    # Perform analysis for each model in the list
    # Perform according to the number of reps
    models_list = open("files/models.txt").read().split("\n")
    for model in models_list:
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

            print(completion.choices[0].message)


perform_analysis()