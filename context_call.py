import google.generativeai as genai
import os

try:
#try - except block is good especially when using external APIs where alot of things can go wrong.
    # --- Reading Environment Variables / the .env file I created instead of system shell ---
    api_key = os.getenv("GOOGLE_API_KEY")
    # if not statement is a common Python pattern for checking if something is empty or None.
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")

    # --- Configuring the API ---
    # This tells the 'genai' library which API key to use.
    genai.configure(api_key=api_key)

    # --- Creating an AI Model Instance ---
    model = genai.GenerativeModel('gemini-2.0-flash')

    print("Chatbot initialized. Type 'quit', 'exit', or 'bye' to end the chat.")
    print("Optional: Type 'show history' to see the conversation log.")

    chat = model.start_chat()

    # --- Interactive Chat Loop ---
    # while true is a loop that will run until the user quits the program., as comapred to count=0 while count < 5, conditional while loop.
    while True:
        # Get input from the user
        user_prompt = input("You: ")

        # Check if the user wants to quit, and force lowercase input to program
        if user_prompt.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break # Exit the while loop

        # If user wants to see history
        if user_prompt.lower() == "show history":
            print("\n--- Conversation History ---")
            for message in chat.history:
                # The 'parts' attribute is a list, so we join its text elements
                # Older versions of the API might just have message.text
                print(f"{message.role.capitalize()}: {''.join(part.text for part in message.parts)}")
            print("--- End of History ---\n")
            continue

        # --- Sending a Prompt and Getting a Response ---
        if not user_prompt.strip(): # Check if the input is just whitespace
            print("Chatbot: Please say something.")
            continue # Skip to the next iteration of the loop

        print(f"Sending prompt: {user_prompt[:50]}...") # [:50] is a slice of the first 50 characters of the user's prompt.
        # also for example if i do [6:11] it will print the characters from index 6 to 10.
        # but not all types of variables, like for example strings / lists /tuples can be sliced.
        # for example dictionaries and integers cannot be sliced, so need to convert to slicable types first
        # number = 12345 / number_str = str(number) / print(number_str[:3])  # "123"

        # --- Sending a Prompt and Getting a Response ---
        # 'model.generate_content()' sends user text (the prompt) to Gemini.
        try:
            response = chat.send_message(user_prompt)
            # --- Accessing the Response ---
            print(f"Gemini: {response.text}")
        except Exception as e:
            print(f"Error generating response from API: {e}")
            # Depending on the error, you might want to break or just inform the user

except ValueError as value_error: # Specific error for API key
    print(f"Configuration error: {value_error}")
except Exception as error_message: # General errors
    print(f"An unexpected error occurred: {error_message}")

# end of program