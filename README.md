# flask_json_restapi_documentation

![FLASK EASY API DOCUMENTATION](https://github.com/augelloantonio/flask_json_restapi_documentation/blob/main/media/preview.png)

## How to run
1. Clone repo or download zip from Github. 
2. Install dependencies with comand:

```
pip install -r requirements.txt
```

3. Execute main script:

```
python3 application.py
```

## How does it work?
As easy as possible, just edit the file "rest_api.json".
Every key under "rest_api" will be converted to a new api documentation element.

Faster approach? Copy and paste this into the key "rest_api":

```
"title": [
            {
                "method": {
                    "Resource Information": {
                        "Method": "method",
                        "Description": "descritption",
                        "Endpoint": "URL",
                        "Header": "Content-Type",
                        "Requires Authentication?": "description"
                    },
                    "Request Body": {
                        "Body": "{json_body }"
                    },
                    "Success Response": {
                        "200": {
                            "Response": "response."
                        }
                    },
                    "Error Response": {
                        "403": {
                            "Response": "response",
                            "Explanaition": "description"
                        },
                        "400": {
                            "Response": "response",
                            "Explanaition": "description"
                        }
                    }
                }
            }
        ],
```