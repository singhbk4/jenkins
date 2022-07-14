import requests
import json
header = {}

def acilogin():
    username = "admin" #input("Enter username:")
    password = "!v3G@!4@Y" #input("Enter password:")

    url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"
    payload = {"aaaUser":{"attributes":{"name": username,"pwd":password}}}

    try:
        apiclogin = requests.request("POST", url=url, json=payload, verify=False)
        json_data = apiclogin.text
        python_data = json.loads(json_data)
        # print(python_data)
        if apiclogin.ok:
          print("APIC Login is successful")
          token = python_data["imdata"][0]["aaaLogin"]["attributes"]["token"]
          token2 = "APIC-cookie="+ token
          header = {"APIC-Cookie": token, "Cookie": token2}
          # print(header)
          return header
        else:
            print(python_data["imdata"][0]["error"]["attributes"]["text"])
            print("Please Provide correct username and password")
            header = acilogin()
            return header
    except Exception as e:
        print("Not possible, something worng")
        print(e)

def acirefresh(header):
    # print("Refereshing cookie")
    url = "https://sandboxapicdc.cisco.com/api/aaaRefresh.json"
    try:
        apicreferesh = requests.request("GET", url, headers=header, verify=False)
        json_data = apicreferesh.text
        python_data = json.loads(json_data)
        if apicreferesh.ok:
            # print("ACI relogin successfull")
            token = python_data["imdata"][0]["aaaLogin"]["attributes"]["token"]
            token2 = "APIC-cookie=" + token
            header = {"APIC-Cookie": token, "Cookie": token2}
            return header
        else:
            print(python_data['imdata'][0]['error']['attributes']['text'])
            print("relogin attempt")
            header = acilogin()
            return header
    except Exception as e:
        print("Cannot connect to APIC while referesh")
        print(e)
        return {}

def ACItenantConfig(tenant, header):
    print ("Creating New Tenant: {}".format(tenant))
    #logger.info ("Changing VRF of bd {}".format(bd))
    url = "https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-{}.json".format(tenant)
    payload = {"fvTenant":{"attributes":{"dn":f"uni/tn-{tenant}","name":f"{tenant}","rn":f"tn-{tenant}","status":"created"},"children":[]}}
    try:
        response = requests.request("POST", url, headers=header, json = payload, verify = False)
        c = response.text
        y = json.loads(c)
        if response.ok:
          print ("Success!! Got 200 OK to create new tenant: {}".format(tenant))
          print("Tenant created Successfully!!!")
          #logger.info ("Success!! Got 200 OK to vrf change request for BD {}".format(bd))
          return y
        else:
          print ("!!! cannot create new tenant: {}".format(tenant))
          #logger.info("!!! cannot change vrf for BD {}, check error".format(bd))
          return y
    except Exception as e:
        print ("error connecting APIC while creating tenant: {}".format(tenant))
        print (e)
        #logger.info("error connecting APIC while changing vrf for BD {}".format(bd))
        #logger.info(e)
        return {}







