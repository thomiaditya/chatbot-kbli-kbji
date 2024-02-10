from chatbot.Application import Application
from chatbot.TelegramBot import TelegramBot
from dotenv import load_dotenv
from fastapi import FastAPI
import os

load_dotenv()
print(".env file loaded!")

server = FastAPI()
app = Application(server)

HOST = os.environ.get("SERVER_HOST", "0.0.0.0")
PORT = int(os.environ.get("SERVER_PORT", 8000))

# Run the FastAPI server
if __name__ == "__main__":
    import uvicorn
    print("Starting application...")
    uvicorn.run("main:server", host=HOST, port=PORT, reload=True)
