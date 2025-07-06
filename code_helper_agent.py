from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class State(TypedDict):
    code: str
    language: str
    functionality: str
    documentation: str

llm = ChatOpenAI(model="gpt-4", temperature=0.0)

def detect_language(state: State):
    """Identify what programming language the code is written in"""
    prompt = PromptTemplate(
        input_variables=["code"],
        template="What programming language is the following code written in? Answer with just the language name.\n\nCode: {code}\n\nLanguage:"
    )

    message = HumanMessage(content=prompt.format(code=state["code"]))
    language = llm.invoke([message]).content.strip()

    return {"language": language}

def analyze_functionality(state: State):
    """Determine what the code does and how it works"""
    prompt = PromptTemplate(
        input_variables=["code", "language"],
        template="Analyze this {language} code and explain what it does in 2-3 sentences. Focus on the main purpose and functionality.\n\nCode: {code}\n\nFunctionality:"
    )

    message = HumanMessage(content=prompt.format(code=state["code"], language=state["language"]))
    functionality = llm.invoke([message]).content.strip()

    return {"functionality": functionality}

def generate_documentation(state: State):
    """Generate documentation for the code"""
    prompt = PromptTemplate(
        input_variables=["code", "language", "functionality"],
        template="""
        Based on this {language} code and its functionality, create documentation that includes:
        1. A brief description of what the code does
        2. Documentation for any functions (parameters, return values)
        3. Any potential improvements

        Code: {code}
        
        Functionality: {functionality}
        
        Documentation:
        """
    )

    chain = prompt | llm
    response = chain.invoke({
        "code": state["code"],
        "language": state["language"],
        "functionality": state["functionality"]
    })

    return {"documentation": response.content}

#Create the workflow graph
workflow = StateGraph(State)
workflow.add_node("detect_language", detect_language)
workflow.add_node("analyze_functionality", analyze_functionality)
workflow.add_node("generate_documentation", generate_documentation) 

workflow.set_entry_point("detect_language")
workflow.add_edge("detect_language", "analyze_functionality")
workflow.add_edge("analyze_functionality", "generate_documentation")
workflow.add_edge("generate_documentation", END)

code_helper = workflow.compile()