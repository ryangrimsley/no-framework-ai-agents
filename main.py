from tools.file_saver import save_to_file
from agents.agents import BaseAgent
from models.ollama_model import OllamaModel
from prompts.prompts import agent_system_prompt_template, file_saving_agent_prompt

if __name__ == "__main__":
    #list with all tools
    tools = [save_to_file]
    #model service, Ollama for local, and model to use
    model_service = OllamaModel
    model_name = 'llama3'
    #create agent and start main loop
    agent = BaseAgent(tools=tools, model_service=model_service, model_name=model_name, system_prompt=file_saving_agent_prompt)
    print("Ask me a question, and I'll output the answer to a file!")
    while True:
        prompt = input("What would you like to ask?(Enter 'exit' to quit): ")
        if prompt.lower() == "exit":
            break

        agent.work(prompt)