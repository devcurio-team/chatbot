# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START aiplatform_sdk_chat]
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
import argparse
from dotenv import load_dotenv
import os

load_dotenv()

def science_tutoring(args, temperature: float = 0.2) -> None:
    chat_model = ChatModel.from_pretrained("chat-bison@001")

    # TODO developer - override these parameters as needed:
    parameters = {
        # Temperature controls the degree of randomness in token selection.
        "temperature": temperature,
        # Token limit determines the maximum amount of text output.
        "max_output_tokens": 256,
        # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_p": 0.95,
        # A top_k of 1 means the selected token is the most probable among all tokens.
        "top_k": 40,
    }

    chat = chat_model.start_chat(
        context="My name is Miles. You are an astronomer, knowledgeable about the solar system.",
        examples=[
            InputOutputTextPair(
                input_text="How many moons does Mars have?",
                output_text="The planet Mars has two moons, Phobos and Deimos.",
            ),
        ],
    )
    # chat = chat_model.start_chat()
    response = chat.send_message(
        "How many planets are there in the solar system?", **parameters
    )
    # response = chat.send_message(
    #     args.query, **parameters
    # )
    print(f"Response from Model: {response.text}")
    # [END aiplatform_sdk_chat]

    return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Cadet Agents')
    parser.add_argument('--query', metavar='query', type=str,
                        help='Write your question to me!')
    args = parser.parse_args()
    science_tutoring(args)
