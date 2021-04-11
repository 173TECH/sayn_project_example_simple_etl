# list of free apis
# https://apipheny.io/free-api/
import requests
import json
import time

from sayn import PythonTask

class ExtractJokesTranslated(PythonTask):
    def setup(self):
        self.dst_table = self.parameters["user_prefix"] + "logs_jokes_translated"
        self.n_jokes = self.parameters["n_jokes"]
        self.translation_type = self.parameters["translation_type"]
        self.table_full_refresh = self.run_arguments["full_load"]

        self.url_joke = "https://official-joke-api.appspot.com/random_joke"
        self.url_translation = f"https://api.funtranslations.com/translate/{self.translation_type}.json"

        return self.success()

    def run(self):
        jokes = []

        # get jokes
        self.debug(f"Extracting {str(self.n_jokes)} jokes.")
        for i in range(self.n_jokes):
            r = requests.get(self.url_joke)

            if r.status_code != 200:
                self.debug("Request not successful!")
                continue

            content = json.loads(r.content.decode("utf-8"))
            # self.debug(content)

            joke = {
                "id": content["id"],
                "type": content["type"],
                "text": content["setup"] + " | " + content["punchline"]
            }

            jokes.append(joke)

        # get joke translations
        # ATTENTION: the translation API has very low levels of free requests (~5 per hour)
        # re-running the task multiple times might not return the translations and load those as null
        self.debug(f"Translating {len(jokes)} jokes.")
        for j in jokes:
            r = requests.post(self.url_translation, data={"text": j["text"]})

            if r.status_code != 200:
                self.debug("Request not successful!")
                continue

            content = json.loads(r.content.decode("utf-8"))
            # self.debug(content)

            j.update({
                "text_translated": content["contents"]["translated"],
                "translation_type": self.translation_type
            })

        # load data to database
        self.debug(f"Loading {len(jokes)} jokes translated to DB.")
        db = self.default_db
        db.load_data(self.dst_table, jokes, replace=self.table_full_refresh)

        return self.success()
