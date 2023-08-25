from prompt import prompt

messages = [
    {"role": "system", "content": prompt},
]
for x in range(0,2):
    user_input = input()
    messages.append({"role": "user", "content": user_input})
    if True:
        addData = {"role": "user", "content": "This is a useless text. You do not need to reply to this text. You should wait for the next text"}
        messages[-1].clear()
        messages[-1].update(addData)
        print(messages[-1])