from google import genai
from google.genai.types import (
    Content,
    LiveConnectConfig,
    Modality,
    Part,
)
from dotenv import load_dotenv
import os

# create a .env file with your google api key
load_dotenv()

async def get_sentiment(text):
    client = genai.Client(
        api_key=os.getenv("GOOGLE_API_KEY"),
        http_options={"api_version": "v1alpha"},
    )

    model_id = "gemini-2.0-flash-exp"
    config = LiveConnectConfig(response_modalities=[Modality.TEXT])
    async with client.aio.live.connect(model=model_id, config=config) as session:
        text_input = f"{text}\nPerform sentiment analysis on the above text. Return 3 values: the probability of the message having a positive sentiment, the probability of the message having a neutral sentiment, and the probability of the message having a negative sentiment. Form your response in the following format: 'positive probability,neutral probability,negative probability'. Return nothing other than this."
        await session.send_client_content(
            turns=Content(role="user", parts=[Part(text=text_input)])
        )

        response = []
    
        async for message in session.receive():
            if message.text:
                response.append(message.text)

        return "".join(response)

async def get_response(text, sentiment):
    client = genai.Client(
        api_key=os.getenv("GOOGLE_API_KEY"),
        http_options={"api_version": "v1alpha"},
    )

    model_id = "gemini-2.0-flash-exp"
    config = LiveConnectConfig(response_modalities=[Modality.TEXT])
    async with client.aio.live.connect(model=model_id, config=config) as session:
        text_input = f"{text}\nAssume you are a human who recieved the above email. Return a {sentiment}, yet polite reply. Keep it within a few sentences in length. Return only the email reply."
        await session.send_client_content(
            turns=Content(role="user", parts=[Part(text=text_input)])
        )

        response = []
    
        async for message in session.receive():
            if message.text:
                response.append(message.text)

        return "".join(response)