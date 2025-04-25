from llama_index.llms.ollama import Ollama
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.core.tools import FunctionTool
from llama_index.core.workflow import Context
import asyncio


# define sample Tool -- type annotations, function names, and docstrings, are all included in parsed schemas!
def multiply(a: int, b: int) -> int:
    """Multiplies two integers and returns the resulting integer"""
    return a * b


def add(a: int, b: int) -> int:
    """Adds two integers and returns the resulting integer"""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtracts two integers and returns the resulting integer"""
    return a - b


def divide(a: int, b: int) -> int:
    """Divides two integers and returns the resulting integer"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b


# initialize llm
llm = Ollama(model="llama-3b-npu", request_timeout=100)

agent = AgentWorkflow.from_tools_or_functions(
    [
        FunctionTool.from_defaults(multiply),
        FunctionTool.from_defaults(add),
        FunctionTool.from_defaults(subtract),
        FunctionTool.from_defaults(divide),
    ],
    llm=llm,
)


async def main():
    ctx = Context(agent)
    # stateless
    response = await agent.run("What is 2 times 2?", ctx=ctx)
    print(response)

    response = await agent.run("what is 2 divided by 2", ctx=ctx)
    print(response)

    response = await agent.run("What is 2 plus 2", ctx=ctx)
    print(response)
    response = await agent.run("What is 2 minus 2", ctx=ctx)
    print(response)


# Run the main function

asyncio.run(main())
