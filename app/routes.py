from quart import Blueprint, jsonify, request
import logging

routes = Blueprint('routes', __name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# define routes
@routes.route('/hello-world', methods=['POST'])
async def hello_world():
    try:
        data = await request.json
        logger.info(f"Received data: {data}")

        response = [
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

        return jsonify(response), 200
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({"error": "Server error"}), 500

@routes.route('/call-status', methods=['POST'])
async def call_status():
    try:
        data = await request.json
        logger.info(f"Call status: {data}")
        return '', 200
    except Exception as e:
        logger.error(f"Error in call status: {str(e)}")
        return '', 500

@routes.websocket('/ws')
async def ws_handler():
    logger.info("New WebSocket connection established.")

    while True:
        try:
            message = await websocket.receive()
            data = json.loads(message)
            logger.info(f"Received message: {data}")

            if data.get('type') == 'session:new':
                call_sid = data['call_sid']
                logger.info(f"New incoming call: {call_sid}")
                
                response = {
                    "msgid": data.get("msgid"),
                    "command": {
                        "verb": "say",
                        "text": "Hi, welcome to the jambonz WebSocket app!"
                    }
                }

                await websocket.send(json.dumps(response))
                logger.info(f"Sent response to call: {call_sid}")

        except Exception as e:
            logger.error(f"WebSocket error: {e}")
            break