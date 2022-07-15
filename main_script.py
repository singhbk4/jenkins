from dataDump import dataread
from ACI_Config import acilogin
from ACI_Config import acirefresh
from ACI_Config import ACItenantConfig
from ACI_Config import ACIvrfConfig
import warnings

data = dataread()  # dumping data from excel
warnings.filterwarnings("ignore")
header = acilogin()  # login in APIC

for value in data:
    # dumping data from excel into variables
    tenant = data[value]["tenant"]
    bd = data[value]["bd"]
    vrf = data[value]["vrf"]

    for tenant in tenant:
        l3outchk = True
        print("Creating Tenant")
        header = acirefresh(header)
        tenant = data[value]["tenant"]
        tenantCreate = ACItenantConfig(tenant, header)
        # print(tenantCreate)
        while True:
            if tenantCreate["totalCount"] != "0" and "already exist" in tenantCreate['imdata'][0]['error']['attributes']['text']:
                print(f"Tenant {tenant} already exist")
                break
            else:
                break
        break

    for vrf in vrf:
        l3outchk = True
        print("Creating VRF")
        header = acirefresh(header)
        tenant = data[value]["tenant"]
        vrf = data[value]["vrf"]
        vrfCreate = ACIvrfConfig(tenant,vrf,header)
        while True:
            if vrfCreate["totalCount"] != "0" and "already exist" in vrfCreate['imdata'][0]['error']['attributes']['text']:
                print(f"Tenant {vrf} already exist")
                break
            else:
                break
        break
