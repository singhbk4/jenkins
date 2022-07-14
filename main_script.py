from dataDump import dataread
from ACI_Config import acilogin
from ACI_Config import acirefresh
from ACI_Config import ACItenantConfig
import warnings

data = dataread()  # dumping data from excel
warnings.filterwarnings("ignore")
header = acilogin()  # login in APIC

for value in data:
    # dumping data from excel into variables
    tenant = data[value]["tenant"]
    bd = data[value]["bd"]

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
            # else:
            #     print("Creating new Tenant, 2nd")
            #     header = acilogin()
            #     tenantCreate = ACItenantConfig(tenant, header)
        break

