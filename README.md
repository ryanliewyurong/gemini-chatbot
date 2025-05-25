# Gemini Chatbot

A Python-based chatbot implementation using Google's Gemini AI model. This chatbot provides an interactive command-line interface for engaging in conversations with the Gemini AI model.

## Features

- Interactive chat interface with Gemini AI
- Conversation history tracking
- Error handling for API interactions
- Environment variable support for API key management
- Command-based controls for chat management

## Prerequisites

- Python 3.x
- Google API key for Gemini AI
- Required Python packages:
  - google-generativeai
  - python-dotenv (for .env file support)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/gemini-chatbot.git
cd gemini-chatbot
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Google API key:


## Usage

1. Run the chatbot:
```bash
python chatbot.py
```

2. Available Commands:
   - Type your message to chat with the AI
   - Type `show history` to view conversation history
   - Type `quit`, `exit`, or `bye` to end the chat

## Features in Detail

### Chat Interface
- Real-time interaction with Gemini AI
- Automatic response generation
- Input validation and error handling

### Conversation Management
- View complete chat history using the `show history` command
- Track both user inputs and AI responses
- Maintain conversation context throughout the session

### Error Handling
- Robust error handling for API interactions
- Environment variable validation
- Graceful error messages for user feedback

## Security

- API key management through environment variables
- No hardcoded sensitive information
- Secure API key storage using `.env` file

## Contributing

Feel free to submit issues and enhancement requests!

## License

[Your chosen license]

## Acknowledgments

- Google Gemini AI for providing the API
- Python community for the excellent libraries