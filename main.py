
import re

def evaluate_expression(expression):
    # Replace operators with spaces for safe splitting
    expression = expression.replace('*', ' * ').replace('/', ' / ').replace('+', ' + ').replace('-', ' - ')
   
    try:
        # Safe evaluation of the mathematical expression
        tokens = expression.split()
        if len(tokens) == 3:
            num1 = float(tokens[0])
            operator = tokens[1]
            num2 = float(tokens[2])
           
            if operator == '+':
                return f"The result is {num1 + num2}"
            elif operator == '-':
                return f"The result is {num1 - num2}"
            elif operator == '*':
                return f"The result is {num1 * num2}"
            elif operator == '/':
                if num2 != 0:
                    return f"The result is {num1 / num2}"
                else:
                    return "Error: Division by zero is not allowed."
            else:
                return "Invalid operator. Please use +, -, *, or /."
        else:
            return "Invalid expression format. Please use two numbers and an operator."
    except Exception:
        return "I'm sorry, I couldn't compute that. Please make sure your input is a valid mathematical expression."

def chatbot_response(user_input):
    # Convert the user input to lowercase for easier matching
    user_input = user_input.lower()
   
    # Check for mathematical expressions
    if re.search(r'\d+\s*[\+\-\*/]\s*\d+', user_input):
        # Extract and evaluate the mathematical expression
        expression = re.sub(r'[^\d+\-*/.]', '', user_input)
        return evaluate_expression(expression)
   
    # Define responses to different user inputs
    if "hello" in user_input or "hi" in user_input:
        return "Hello! I'm a mathematical chatbot. I can perform calculations for you. Just type a math problem like '10 + 5' and I'll solve it for you!"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing great! How can I assist you with calculations today?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "your name" in user_input:
        return "I'm a mathematical chatbot created to assist you with calculations."
    elif "perform" in user_input and "math" in user_input:
        return "Please provide a mathematical expression like '10 + 20' for me to calculate."
    else:
        return "I'm not sure how to respond to that. Can you ask me something else or try a math calculation?"

def main():
    print("Chatbot: Hello! I'm a mathematical chatbot. I can perform calculations for you. Just type a math problem like '10 + 5' and I'll solve it for you. Type 'bye' to end the conversation.")
    while True:
        # Take user input
        user_input = input("You: ")
       
        # Get the chatbot response
        response = chatbot_response(user_input)
       
        # Print the chatbot response
        print(f"Chatbot: {response}")
       
        # End the conversation if the user says goodbye
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            break

if __name__ == "__main__":
    main()
      
