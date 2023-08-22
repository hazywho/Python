import openai
import gradio as gr
import json
from List import  BookFinder
from Prompt import prompt
from functions import gpt_functions

openai.api_key = "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"


messages = [
    {"role": "system", "content": prompt},
]

switch_dict = {
    "find_book_location_by_name": BookFinder.get_book_location_by_name,
    "list_book_by_genre": BookFinder.list_book_by_genre,
    "list_book_by_rating": BookFinder.list_book_by_rating,
    "find_rating_by_name": BookFinder.find_rating_by_name,
    "find_genre_by_name": BookFinder.find_genre_by_name
}

def case_default(json_input):
    print("API not implemented")

def chat_completion(messages):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        temperature=0.7,
        messages=messages,
        functions=gpt_functions
    )

def chatbot(user_input):
    if user_input:
        messages.append({"role": "user", "content": user_input})
        for index, msg in enumerate(messages):
            print(msg)

        # User Input : Where is the "Frankenstein" book located?
        chat = chat_completion(messages)
        reply = chat.choices[0].message.content

        if chat.choices[0].finish_reason == "function_call":
            name = chat.choices[0].message.function_call.name
            arguments = json.loads(chat.choices[0].message.function_call.arguments)
            print(name, arguments)
            result = switch_dict.get(name, case_default)(arguments)
            messages.append({"role": "function", "name": name, "content": json.dumps(result)})
            chat = chat_completion(messages)
            reply = chat.choices[0].message.content

        messages.append({"role": "assistant", "content": reply})
        print(reply)
        return reply


inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)