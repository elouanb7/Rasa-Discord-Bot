# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class ActionModifyComment(Action):
    def name(self):
        return "action_modify_comment"

    def run(self, dispatcher, tracker, domain):
        comment = next(tracker.get_latest_entity_values("commentaire"), None)
        if comment:
            dispatcher.utter_message(text="Votre commentaire a été modifié.")
            return [SlotSet("table_reservation_comment", comment)]
        else:
            dispatcher.utter_message(text="Je n'ai pas compris votre commentaire. Pouvez-vous répéter ?")
            return []


class ActionShowReservationInfo(Action):
    def name(self):
        return "action_show_reservation_info"

    def run(self, dispatcher, tracker, domain):
        first_name = tracker.get_slot("reservation_name")
        comment = tracker.get_slot("table_reservation_comment")
        heure = tracker.get_slot("heure_reservation")
        place = tracker.get_slot("nbr_place_reservation")
        dispatcher.utter_message(text=f"Voici les informations de votre réservation :"
                                      f"\nPrénom : {first_name}"
                                      f"\nPlace: {place}"
                                      f"\nHeure de réservation : {heure}"
                                      f"\n Commentaire : {comment}")
        return []
