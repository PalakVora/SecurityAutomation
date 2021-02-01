import re

def find_vulnerable_parameters(result):
    parameter = {}
    try:
        Method = str(result['HTTPMethod'])
        parameter['HTTPMethod'] = Method
        print("HTTP Method: " + parameter['HTTPMethod'])

        Protocol = str(result['Protocol'])
        parameter['Protocol'] = Protocol
        print("Protocol: " + parameter['Protocol'])

        parameter['URL'] = str(result['URL'])
        print("URL: " + str(parameter['URL']))

        parameter['Body']=result['Body']
        print("Body: " + str(parameter['Body']))

        parameter['Header']=result['Header']
        print("Header: " + str(parameter['Header']))

        parameter['Cookie']=result['Cookie']
        print("Cookie: " + str(parameter['Cookie']))

    except:

        print("Error in Reading API Contents")

    try:
        parameter['URL_Parameter'] = re.findall(r'\$(.*?)\$', parameter['URL'])
        if(parameter['URL_Parameter']):
            print("Parameter found in URL")
            print(parameter['URL_Parameter'])
        else:
            print("No Parameter found in URL")
           # parameter['URL_Parameter'] = parameter['URL']

        parameter['Body_Parameter'] = re.findall(r'\$(.*?)\$', str(parameter['Body']))
        if(parameter['Body_Parameter']):
            print("Parameter found in Body")
            print(parameter['Body_Parameter'])
        else:
            print("No Parameter found in Body")
            parameter['Body_Parameter'] = parameter['Body']

        parameter['Header_Parameter'] = re.findall(r'\$(.*?)\$', str(parameter['Header']))
        if (parameter['Header_Parameter']):
            print("Parameter found in Header")
            print(parameter['Header_Parameter'])
        else:
            print("No Parameter found in Header")
            #parameter['Header_Parameter'] = parameter['Header']

        parameter['Cookie_Parameter'] = re.findall(r'\$(.*?)\$', str(parameter['Cookie']))
        if (parameter['Cookie_Parameter']):
            print("Parameter found in Cookie")
            print(parameter['Cookie_Parameter'])
        else:
            print("No Parameter found in Cookie")
            #parameter['Cookie_Parameter'] = parameter['Cookie']
    except:
        print("Error in fetching Parameters")

    return parameter

