# 📘 FLASK EASY API - Monitor & Document

![FLASK EASY API DOCUMENTATION](https://github.com/augelloantonio/flask_json_restapi_documentation/blob/main/media/preview.png)
![FLASK EASY API DOCUMENTATION](https://github.com/augelloantonio/flask_json_restapi_documentation/blob/main/media/monitor_preview.png)

**Flask JSON REST API Documentation** is a lightweight project that allows you to quickly build a visual documentation and control room for your APIs using a simple JSON configuration.


---

## Features

* Auto-generate API documentation from a JSON file
* Test all your endpoint with one click
* Test a single endpoint
* Fast setup — no database or heavy configuration needed
* Group APIs by service or organization
* Easy integration with existing Flask apps
* Easy integration with existing Flask apps

---

## How to Run

1. **Clone the repository or download the ZIP:**

   ```bash
   git clone https://github.com/augelloantonio/flask_json_restapi_documentation.git
   cd flask_json_restapi_documentation
   ```

2. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   python3 application.py
   ```

4. **Visit the documentation in your browser:**

   ```
   http://localhost:8000/
   ```

---

## How It Works

The app reads a single file: `static/docs/rest_api.json`.

* The `rest_api` key contains all services.
* Each service has a list of endpoint definitions.
* Each endpoint contains: method, description, headers, body, success & error responses.

To get started quickly, replace the value of `"rest_api"` with this template:

```json
"rest_api": {
  "YourServiceName": [
    {
      "YourEndpointName": {
        "Resource Information": {
          "Method": "GET",
          "Description": "Short explanation of the endpoint",
          "Endpoint": "https://api.yourdomain.com/endpoint",
          "Header": {
            "Content-Type": "application/json"
          },
          "Requires Authentication?": "Yes"
        },
        "Request Body": {
          "Body": {
            "field1": "value",
            "field2": "value"
          }
        },
        "Success Response": {
          "200": {
            "Response": "Successful response message"
          }
        },
        "Error Response": {
          "403": {
            "Response": "Unauthorized access",
            "Explanaition": "Authentication failed"
          },
          "400": {
            "Response": "Bad request",
            "Explanaition": "Missing or invalid parameters"
          }
        }
      }
    }
  ]
}
```

---

## Next Steps

* [ ] Add auth test mode for endpoints
* [ ] Improve test mode for endpoints
* [ ] Add Swagger implementation

---

## 🧑‍💻 Author

**Antonio Augello**
[augellotech.com](https://www.augellotech.com/) | [LinkedIn](https://www.linkedin.com/in/antonio-augello-aba83911a/)

---