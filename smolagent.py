from smolagents import (
    CodeAgent,
    DuckDuckGoSearchTool,
    FinalAnswerTool,
    LiteLLMModel,
)
import gradio as gr

model = LiteLLMModel(
    model_id="ollama_chat/llama-3b-npu",
    api_key="ollama",
    api_base="http://localhost:11434",
)

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool(), FinalAnswerTool()],
    model=model,
    add_base_tools=True,
    planning_interval=3,
    additional_authorized_imports=["numpy", "pandas", "sys", "wikipedia", "requests"],
)


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
