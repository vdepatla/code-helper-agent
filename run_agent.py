from code_helper_agent import code_helper

#Sample code to run the analyze
python_code = """
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
"""

# Initialize the code helper agent with the provided Python code
initial_state = { "code": python_code }

result = code_helper.invoke(initial_state)

# Print the results of the analysis
print("Language Detected:", result["language"])
print("Functionality Analyzed:", result["functionality"])
print("Documentation Generated:", result["documentation"])
