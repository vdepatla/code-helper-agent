from code_helper_agent import code_helper
import gradio as gr

def run_agent(input_text):
    response = code_helper.invoke({"code": input_text})
    documentation = response.get("documentation", "")
    language = response.get("language", "")
    return f"Language: {language}\n\nDocumentation:\n{documentation}"

demo = gr.Interface(fn=run_agent, inputs=gr.Textbox(label="Input", placeholder="Enter code for which you want to generate code..."),
                     outputs=gr.Textbox(label="Output", placeholder="Your output will appear here..."),
                     title="Code Helper Agent",
                     description="An AI-powered tool to analyze and document code.",
                     theme="default",
                     allow_flagging="never")

demo.launch()