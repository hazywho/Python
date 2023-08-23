import openai
import gradio as gr
import json
from List import  Finder, gpt_functions
from Prompt import prompt

openai.api_key = "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"


messages = [
    {"role": "system", "content": prompt},
]

switch_dict = {
    "find_webstie_name_by_ranking": Finder.find_website_name_by_ranking
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