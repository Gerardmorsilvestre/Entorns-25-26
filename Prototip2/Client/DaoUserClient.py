import requests
from User import User


class DaoUserClient:

    base_url = "http://localhost:5000"

    def login(self, user):

        url_peticion = self.base_url + "/login"

        params_post = {
            "username": user.username,
            "password": user.password
        }

        response = requests.post(url_peticion, json=params_post)

        if response.status_code == 200:

            user_data_raw = response.json()

            print("Respuesta servidor:", user_data_raw)

            code_response = user_data_raw.get("coderesponse")
            if code_response == "0":
                return None

            user = User(
                user_data_raw.get("id"),
                user_data_raw.get("username"),
                "",
                user_data_raw.get("email"),
                user_data_raw.get("idrole"),
                user_data_raw.get("token")
            )

            return user

        else:
            print("Error HTTP:", response.status_code)
            return None