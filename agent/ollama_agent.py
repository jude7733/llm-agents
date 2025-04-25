from ollama import ChatResponse, chat
import json
import os
from config.spec import model_id

from tools.sample_tool import add_two_numbers, subtract_two_numbers_tool

json_path = os.path.join(
    os.path.dirname(__file__), "..", "prompts", "system_prompt.json"
)

# Open and load the JSON file
with open(json_path, "r") as f:
    system_prompts = json.load(f)


available_functions = {
    "add_two_numbers": add_two_numbers,
    "subtract_two_numbers": subtract_two_numbers_tool,
}

messages = [
    system_prompts,
]

print("Prompt:", messages)


def execute_model():
    while True:
        user_input = input("Ask maths question > ")
        if user_input.lower() == "exit":
            break
        messages.append(
            {"role": "user", "content": user_input},
        )
        response: ChatResponse = chat(
            model_id,
            messages=messages,
            tools=[add_two_numbers, subtract_two_numbers_tool],
        )

        if response.message.tool_calls:
            for tool in response.message.tool_calls:
                if function_to_call := available_functions.get(tool.function.name):
                    print("Calling function:", tool.function.name)
                    print("Arguments:", tool.function.arguments)
                    output = function_to_call(**tool.function.arguments)
                    print("Function output:", output)
                else:
                    print("Function", tool.function.name, "not found")

                # Add the function response to messages for the model to use
                messages.append(
                    {"role": "tool", "content": str(output), "name": tool.function.name}
                )

            # Get final response from model with function outputs
            print("Final response:")
            for part in chat(model_id, messages=messages, stream=True):
                print(part["message"]["content"], end="", flush=True)

            print()

        else:
            print("No tool calls returned from model")
            # Ensure messages are updated even if no tools are called
            print("Final response:")
            for part in chat(model_id, messages=messages, stream=True):
                print(part["message"]["content"], end="", flush=True)

            messages.append({"role": "assistant", "content": response.message.content})
            print()
        print(messages)
