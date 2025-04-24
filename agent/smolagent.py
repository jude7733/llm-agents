from smolagents import (
    CodeAgent,
    DuckDuckGoSearchTool,
    FinalAnswerTool,
    LiteLLMModel,
    load_tool,
)
import gradio as gr

model = LiteLLMModel(
    model_id="ollama_chat/llama-3b-npu",
    api_key="ollama",
    api_base="http://localhost:11434",
)

image_generation_tool = load_tool("m-ric/text-to-image", trust_remote_code=True)
agent = CodeAgent(
    tools=[],
    model=model,
    add_base_tools=True,
    planning_interval=3,
    additional_authorized_imports=["numpy", "pandas", "sys", "requests"],
)

agent.run("Make a 3 line poem about the world")


def agent_response(prompt):
    result = agent.run(prompt)
    return result


iface = gr.Interface(
    fn=agent_response,
    inputs=gr.Textbox(label="Enter your prompt"),
    outputs=gr.Textbox(label="Agent Response"),
    title="Llama 3B NPU",
    description="Interact with the SmolAgent using a Gradio interface.",
)

iface.launch()
