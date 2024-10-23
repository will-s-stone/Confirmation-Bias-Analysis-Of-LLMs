from openai import OpenAI

import format_helper as formatter
import os
import time

lm_studio_client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")


def _get_local_model_response(cover_story_number, repetitions, temp, max_tokens, model_name):
    for x in range(repetitions):
        completion = lm_studio_client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user", "content": formatter.get_cover_story(cover_story_number)}
            ],
            temperature=temp,
            max_tokens=max_tokens
        )
        print(completion.choices[0].message)
        formatter.log_observation(cover_story_number, completion.choices[0].message.content, model_name, temp)


def _get_qwen_1_5_response(cover_story_number, repetitions, temp, max_tokens):
    _get_local_model_response(cover_story_number, repetitions, temp, max_tokens, "qwen-1.5-7B-Chat")


def _get_wizard_coder_response(cover_story_number, repetitions, temp, max_tokens):
    _get_local_model_response(cover_story_number, repetitions, temp, max_tokens, "WizardCoder-Python-13B-V1.0")


def _get_code_llama_response(cover_story_number, repetitions, temp, max_tokens):
    _get_local_model_response(cover_story_number, repetitions, temp, max_tokens, "CodeLlama-7B-Instruct")


def _get_mistral_response(cover_story_number, repetitions, temp, max_tokens):
    _get_local_model_response(cover_story_number, repetitions, temp, max_tokens, "Mistral-7B-Instruct-v0.1")


def _get_phi_2_response(cover_story_number, repetitions, temp, max_tokens):
    _get_local_model_response(cover_story_number, repetitions, temp, max_tokens, "phi-2")


def _get_gemma_2_response(cover_story_number, repetitions, temp, max_tokens):
    _get_local_model_response(cover_story_number, repetitions, temp, max_tokens, "gemma-2-9b-it")


def _get_stable_code_response(cover_story_number, repetitions, temp, max_tokens):
    _get_local_model_response(cover_story_number, repetitions, temp, max_tokens, "stable-code-instruct-3b")


def _get_phi_3_1_response(cover_story_number, repetitions, temp, max_tokens):
    _get_local_model_response(cover_story_number, repetitions, temp, max_tokens, "phi-3.1-mini-128k-instruct")


def _get_llama_3_2_response(cover_story_number, repetitions, temp, max_tokens):
    _get_local_model_response(cover_story_number, repetitions, temp, max_tokens, "llama-3.2-1b-instruct")


def _get_internlm_response(cover_story_number, repetitions, temp, max_tokens):
    _get_local_model_response(cover_story_number, repetitions, temp, max_tokens, "internlm2_5-20b-chat")

def _get_qwen2_1_5_response(cover_story_number, repetitions, temp, max_tokens):
    _get_local_model_response(cover_story_number, repetitions, temp, max_tokens, "qwen2-0.5b-instruct")


def get_non_local_responses(repetitions, temp, max_tokens_per_response):
    for x in range(5):
        x = x + 1
        # _get_gemini_response(x, repetitions, temp, max_tokens_per_response)
        # _get_claude_response(x, repetitions, temp, max_tokens_per_response)
        # _get_gpt_3_5_response(x, repetitions, temp, max_tokens_per_response)
        #_get_gpt_4_response(x, repetitions, temp, max_tokens_per_response)


def get_local_responses(repetitions, temp, max_tokens_per_response):
    #for x in range(5):
        #x = x + 1
        # _get_qwen_1_5_response(x, repetitions, temp, max_tokens_per_response)
        # _get_wizard_coder_response(x, repetitions, temp, max_tokens_per_response)
        # _get_code_llama_response(x, repetitions, temp, max_tokens_per_response)
        # _get_mistral_response(x, repetitions, temp, max_tokens_per_response)
        # _get_phi_2_response(x, repetitions, temp, max_tokens_per_response)
        #_get_gemma_2_response(x, repetitions, temp, max_tokens_per_response)
        #_get_stable_code_response(x, repetitions, temp, max_tokens_per_response)
        #_get_phi_3_1_response(x, repetitions, temp, max_tokens_per_response)
        #_get_llama_3_2_response(x, repetitions, temp, max_tokens_per_response)
        #_get_internlm_response(x, repetitions, temp, max_tokens_per_response)
        _get_qwen2_1_5_response(5, repetitions, temp, max_tokens_per_response)


get_local_responses(30, 0.5, 1024)
