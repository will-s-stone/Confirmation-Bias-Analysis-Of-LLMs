import format_helper as formatter
import os
import dotenv
import google.generativeai as genai
import anthropic

dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
#https://ai.google.dev/api/python/google/generativeai
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)

def get_gemini_response(cover_story, repetitions):
    for x in range(repetitions):
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(cover_story)
        print(response.text)


def get_claude_response(cover_story, repetitions):
    for x in range(repetitions):
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": formatter.get_cover_story(1)}
            ]
        )
        print(message.content)

def get_gpt_3_5_response(cover_story, repetitions):
    for x in range(repetitions):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": task_file}
            ],
            temperature=temp,
            max_tokens=max_tokens,
        )
        print(completion.choices[0].message.content)

def get_gpt_4_response(cover_story, repetitions):
    for x in range(repetitions):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": cover_story}
            ],
            temperature=temp,
            max_tokens=max_tokens,
        )
        print(completion.choices[0].message.content)






