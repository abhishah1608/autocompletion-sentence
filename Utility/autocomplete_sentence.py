import os

import openai

class AutcompleteSentence:
    sentence, context = None, None

    # here is the API key for OpenAI.
    openai.api_key = os.getenv("key_chatgpt")

    def __init__(self, sentence, context):
        self.sentence, self.context = sentence, context

    def get_autcompleteSentence(self):
        prompt = self.sentence

        context = self.context

        p_c = None

        if context is None:
            p_c = prompt
        else:
            p_c = context + '\n' + prompt

        stop_token = ". "

        response = openai.Completion.create(
            engine="davinci",
            prompt=p_c,
            max_tokens=50,  # Adjust the number of tokens as needed
            stop=stop_token,
            temperature=0.9
        )

        translated_text = response.choices[0].text.strip()
        return translated_text





