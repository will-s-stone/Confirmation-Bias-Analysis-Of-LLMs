import format_helper as formatter
import os
import dotenv
import google.generativeai as genai
import anthropic
import openai
from openai import OpenAI

dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# https://ai.google.dev/api/python/google/generativeai
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)
openai_client = OpenAI(api_key=OPENAI_API_KEY)
anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


def get_gemini_response(cover_story, repetitions, temp, max_tokens):
    model = genai.GenerativeModel('gemini-pro')
    generation_config = genai.GenerationConfig(temperature=temp, max_output_tokens= max_tokens)
    for x in range(repetitions):
        response = model.generate_content(cover_story, generation_config=generation_config)
        print(response.text)


def get_claude_response(cover_story, repetitions, temp, max_tokens):
    for x in range(repetitions):
        #client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        message = anthropic_client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=max_tokens,
            temperature=temp,
            messages=[
                {"role": "user", "content": cover_story}
            ]
        )
        print(message.content)


def get_gpt_3_5_response(cover_story, repetitions, temp, max_tokens):
    for x in range(repetitions):
        completion = openai_client.chat.completions.create(
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


def get_gpt_4_response(cover_story, repetitions, temp, max_tokens):
    for x in range(repetitions):
        completion = openai_client.chat.completions.create(
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



#get_claude_response(formatter.get_cover_story(1), 2, 1, 1024)
