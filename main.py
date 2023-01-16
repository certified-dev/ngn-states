from fastapi import FastAPI

app = FastAPI()

db = [  
        {"state": "Abia", "capital": "Umahia"},
        {"state": "Adamawa", "capital": "yola"},
        {"state": "Akwa ibom", "capital": "Uyo"},
        {"state": "Anambra", "capital": "Oka"},
        {"state": "Bauchi", "capital": "Bauchi"},
        {"state": "Benue", "capital": "Makurdi"},
        {"state": "Borno", "capital": "Maduguri"},
        {"state": "Cross River", "capital": "Calabar"},
        {"state": "Delta", "capital": "Asaba"},
        {"state": "Ebonyi", "capital": "Abakaliki"},
        {"state": "Edo", "capital": "Benin"},
        {"state": "Enugu", "capital": "Enugu"},
        {"state": "Imo", "capital": "Owerri"},
        {"state": "Jigawa", "capital": "Duste"},
        {"state": "Kano", "capital": "Kano"},
        {"state": "Kaduna", "capital": "Kaduna"},
        {"state": "Plateau", "capital": "Jos"},
        {"state": "Rivers", "capital": "Port harcourt"},
        {"state": "Lagos", "capital": "Ikeja"},
        {"state": "Taraba", "capital": "Jalingo"},
        {"state": "Abuja", "capital": "FCT"},
        {"state": "Sokoto", "capital": "Sokoto"}
     ]


@app.get('/api/states')
def get_states():
    return db



