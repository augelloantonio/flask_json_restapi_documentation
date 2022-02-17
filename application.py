import os
from flask import Flask, render_template
import pandas as pd
import json

application = app = Flask(__name__)

##########
# Main Route with the documentation explained
##########

@application.route('/')
def api_guide():
    filename = os.path.join('static/rest_api.json')
    with open(filename) as api_file:
        data = json.load(api_file)
    
    api_version = data['api_version']
    name = data['name']

    section_list = []
    endpoint_list = []
    meta_info_list = []
    services = {}
    endpoints_meta = {}
    info_list=[]
    meta_info = {}
    info_text = []
    meta_info_text = {}
    info_services = {}
    
    df = pd.json_normalize(data, max_level=0)

    i = 0
    count =0
    count_i = 0
    method = ""
    description = ""
    count_text_index = 0
    meta_count = 0
    for section in df['rest_api'][0]:
        section_list.append(section)
        for endpoints in df['rest_api'][0][section]:
            for service in endpoints:
                endpoint_list.append(service)   
                
                for d in df['rest_api'][0][section][count][service]:
                    meta_info_list.append(d)
                    for meta in df['rest_api'][0][section][count][service][d]:
                        info_list.append(meta)
                        
                        meta_info_text[count_text_index] = {"service":service, "info_text":df['rest_api'][0][section][count][service][d][meta], "meta":meta }
                        
                        if meta== "Method":
                            method = df['rest_api'][0][section][count][service][d][meta]
                        if meta == "Description":
                            description = df['rest_api'][0][section][count][service][d][meta]
                        meta_info[count_text_index] = {"meta_info":meta, "service":service, "section":d, "info_text":df['rest_api'][0][section][count][service][d][meta], "meta":meta}
                        count_text_index+=1 
                    count_i+=1                    
                    
                    info_list = []
                info_services[count_i] = {'service':service, 'description':description, 'method':method}
                services[i] = {'available_functions':endpoint_list, 'section':section}
                endpoints_meta[count_i] = {"meta":meta_info_list, "service":service}
                
                count += 1
                meta_info_list = []
        count = 0
        meta_count = 0
        endpoint_list = []
        i+=1

    return render_template("index.html", name=name, api_version=api_version, section_list=section_list, services=services, endpoints_meta=endpoints_meta, meta_info=meta_info, meta_info_text=meta_info_text, info_services=info_services)


if __name__ == "__main__":
    application.debug = True
    application.run(port=5050)
