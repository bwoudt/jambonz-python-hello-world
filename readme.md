# Jambonz Python Hello World (Quart)

This repository contains a simple Python implementation of a Jambonz webhook application using the `Quart` framework. The app includes a basic "Hello World" example that uses Jambonz's Text-to-Speech (TTS) functionality.

## Features

- Basic TTS example using Jambonz
- Async API using `Quart` (Flask-compatible async framework)
- Logging for incoming requests and responses
- Configurable via environment variables for easy deployment

## Repository URL

Clone the repository from GitHub:

```bash
git clone https://github.com/bwoudt/jambonz-python-hello-world.git
```
Installation
1. Prerequisites
Ensure you have Python 3.8+ installed.

2. Install dependencies
From the root directory of the project, run the following command to install the required packages:

```bash
pip install -r requirements.txt
```
3. Environment variables
Create a ```.env``` file in the root directory of the project with your Jambonz configuration. You can use the following template:

```ini
NODE_ENV=production
LOGLEVEL=info
HTTP_PORT=3000
JAMBONZ_ACCOUNT_SID=<YOUR_JAMBONZ_ACCOUNT_SID>
JAMBONZ_API_KEY=<YOUR_JAMBONZ_API_KEY>
JAMBONZ_REST_API_BASE_URL=<YOUR_JAMBONZ_API_URL>
WEBHOOK_SECRET="" # This is a secret key that you can use to secure your webhook endpoint
HTTP_PASSWORD="" # This is the password that you can use to secure your webhook endpoint
HTTP_USERNAME="" # This is the username that you can use to secure your webhook endpoint
```
Replace the placeholders with your actual Jambonz API credentials and other necessary values.

Project Structure
The project is structured as follows:

```bash
jambonz-python-hello-world/
├── app/
│   ├── __init__.py         # Initializes the Quart app
│   ├── routes.py           # Defines the HTTP routes (e.g., /hello-world)
│   └── config.py           # Loads configuration from .env
├── .env                    # Environment variables for Jambonz API
├── main.py                 # Starts the Quart application
└── README.md               # Project documentation (this file)
```
4. Running the application
Start the Quart server using:

```bash
python main.py
```
The server will start on http://0.0.0.0:3000 by default. Jambonz will trigger your webhook when an incoming call is received.

5. Jambonz Webhook Configuration
In the Jambonz portal, set up your application to use the webhook. You should point to the /hello-world route on the server where this application is hosted.

For example:

```arduino
http://<your-server-ip>:3000/hello-world
```
This will trigger the TTS response defined in the routes.py file when Jambonz processes an incoming call.

Example Webhook Response
The /hello-world route sends back a JSON payload to Jambonz with the text to be spoken during a call. The response looks like this:

```json
[
  {
    "verb": "say",
    "text": "<speak><prosody volume='loud'>Hi there,</prosody> and welcome to jambonz! This is an example of simple text-to-speech. Try us out!</speak>"
  },
  {
    "verb": "pause",
    "length": 1.5
  },
  {
    "verb": "hangup"
  }
]
```
**Contributing**
Feel free to fork this repository and submit pull requests. Any improvements or new features are welcome!

**License**
This project is licensed under the MIT License - see the LICENSE file for details.