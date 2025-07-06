from code_helper_agent import code_helper
import gradio as gr

def run_agent(input_text):
    return code_helper.invoke({"code": input_text})

demo = gr.Interface(fn=run_agent, inputs=gr.Textbox(label="Input", placeholder="Type your input here..."),
                     outputs=gr.Textbox(label="Output", placeholder="Your output will appear here..."),
                     title="Code Helper Agent",
                     description="An AI-powered tool to analyze and document code.",
                     theme="default",
                     allow_flagging="never")

demo.launch(share=True)