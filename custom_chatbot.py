import google.generativeai as genai

# Configure the Gemini API key
genai.configure(api_key="your_api_key")  # Replace with your actual API key

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")

print("Type 'exit' to quit the program.\n")  # Inform the user about the exit option

# Infinite loop for user interaction
while True:
    # Get user input
    domain = "fun facts about every professional soccer player"
    user_input = input("Enter your prompt: ")

    # Break the loop if the user types "exit"
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if domain == "your field/domain here":
      context = "the full description for your chatbot"

    prompt = context + user_input

    # Generate and print the response
    try:
        response = model.generate_content(prompt)
        print("\nResponse from Gemini:")
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")
