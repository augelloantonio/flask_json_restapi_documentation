import os
import json
import http.client
from urllib.parse import urlparse
from flask import Blueprint, render_template, abort
import requests

test_api = Blueprint('test_api', __name__, template_folder='templates')

@test_api.route('/<string:section>/<string:api>')
def test_api_view(section, api):
    try:
        response_class = 'bg-success'

        # Load API data from JSON file
        filename = os.path.join('static/docs/rest_api.json')
        with open(filename) as api_file:
            data = json.load(api_file)
        
        index = 0
        for idx, val  in enumerate(data['rest_api'][section]):
            for i in val:
                if i == api:
                    index = idx
        
        selectedApi = data['rest_api'][section][index][api]
        method = selectedApi['Resource Information']['Method']
        endpoint = selectedApi['Resource Information']['Endpoint']
        headers = selectedApi['Resource Information']['Header']
        req_body = selectedApi.get('Request Body', {}).get('Body', {})

        # Make API Request
        response = requests.Response()        
        response_warning = ''
        response_json = {}
        try:
            session = requests.Session()
            
            try:
                session.headers.update(headers)
            except:
                response_warning = "Error in headers"

            if method == 'POST':
                response = session.post(endpoint, json=req_body)
            elif method == 'GET':
                response = session.get(endpoint)
            elif method == 'PUT':
                response = session.put(endpoint, json=req_body)
            elif method == 'DELETE':
                response = session.delete(endpoint)
                        
            # Check if the response contains JSON before calling .json()
            
            if response.status_code in range(200, 300): 
                response_class = 'bg-success'
            if response.status_code in range(300, 500): 
                response_class = 'bg-warning'
            if response.status_code in range(400, 500): 
                response_class = 'bg-danger'
            if response.status_code in range(500, 600): 
                response_class = 'bg-danger'
            try:
                # Verify response content type
                if 'application/json' in response.headers.get('Content-Type', ''):
                    response_json = response.json()        
                else:
                    response_warning =  "Response is not in JSON format"
            except requests.JSONDecodeError:
                response_warning =  "Invalid JSON"
                response.status_code = -1
        except requests.RequestException as e:
            response_warning = f"Error making API request: {e}"
            response.status_code = -1
                    
        return render_template(
            "test_api.html",
            section=section,
            api=api,
            method=method,
            endpoint=endpoint,
            header=headers,
            req_body=req_body,
            response_status=response.status_code,
            response_time=response.elapsed.total_seconds() if response else "N/A",
            response_json=response_json,  # Safe JSON data,
            response_warning=response_warning,
            response=response,
            response_class=response_class
        )

    except (KeyError, FileNotFoundError):
        abort(404)
        
@test_api.route('testAll/')
def test_all_apis_view():
    try:
        response_class = 'bg-success'
        
        request_response_list = []
        
        # Load API data from JSON file
        filename = os.path.join('static/docs/rest_api.json')
        
        with open(filename) as api_file:
            data = json.load(api_file)
                
        for section in data['rest_api']:
            for api in data['rest_api'][section]:
                for el in api:                
                    selectedApi = el
                    method = api[el]['Resource Information']['Method']
                    endpoint = api[el]['Resource Information']['Endpoint']
                    headers = api[el]['Resource Information']['Header']
                    req_body = api[el].get('Request Body', {}).get('Body', {})

                    request_response = makeRequest(endpoint, method, headers, req_body)
                    request_response_list.append(request_response)
        
        # Compute statistics
        success_count = sum(1 for r in request_response_list if 200 <= r['response_code'] < 300)
        failure_count = sum(1 for r in request_response_list if r['response_code'] >= 400)
        average_execution_time = round(sum(r['execution_time'].total_seconds() for r in request_response_list) / len(request_response_list), 3)

        # Pass data to template
        return render_template(
            "test_all_api.html",
            request_response_list=request_response_list,
            success_count=success_count,
            failure_count=failure_count,
            average_execution_time=average_execution_time
        )

            
    except (KeyError, FileNotFoundError):
        abort(404)
        

def makeRequest(endpoint, method, headers, req_body):
        
    session = requests.Session()
    response = requests.Response()  
    response_json = {}
    try:
        try:
            session.headers.update(headers)
        except:
            response_warning = "Error in headers"
            pass

        if method == 'POST':
            response = session.post(endpoint, json=req_body)
        elif method == 'GET':
            response = session.get(endpoint)
        elif method == 'PUT':
            response = session.put(endpoint, json=req_body)
        elif method == 'DELETE':
            response = session.delete(endpoint)
                        
        # Check if the response contains JSON before calling .json()
            
        if response.status_code in range(200, 300): 
            response_class = 'bg-success'
        if response.status_code in range(300, 500): 
            response_class = 'bg-warning'
        if response.status_code in range(400, 500): 
            response_class = 'bg-danger'
        if response.status_code in range(500, 600): 
            response_class = 'bg-danger'
        try:
            # Verify response content type
            if 'application/json' in response.headers.get('Content-Type', ''):
                response_json = response.json()        
            else:
                print("Warning: Response is not JSON.")
                response_warning =  "Response is not in JSON format"
        except requests.JSONDecodeError:
            print("Error: Response is not valid JSON.")
            response_warning =  "Invalid JSON"
            response.status_code = -1
            pass
    except requests.RequestException as e:
        print(f"Error making API request: {e}")
        response_warning = f"Error making API request: {e}"
        response.status_code = -1
        pass

    
    return {"method":method, "endpoint":endpoint, "response_code":response.status_code, "response_warning":response_warning, "execution_time": response.elapsed, "response_json":response_json }