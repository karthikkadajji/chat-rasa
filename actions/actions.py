from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from slack_sdk import WebClient


class ActionHelloWorld(Action):
    #
    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #
        client = WebClient(token="ADD SLACK TOKEN")
        response = client.reactions_add(
            channel=tracker.latest_message["metadata"]["out_channel"],
            name="thumbsup",
            timestamp=tracker.latest_message["metadata"]["thread_id"]
        )
        if response['ok']:
            print("successfully gave a thumbsup")
        else:
            print("failed to give thumbsup " + response["error"])

        return []
