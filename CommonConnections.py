import os
from contextlib import suppress

# ##basic testing of reading text files and such.  will be used for connections and common functions creation
user = os.getlogin()
sysUser511 = user
base_path = f"C:\\Users\\{user}\\OneDrive - Abbott\\LoginInfo\\"

with suppress(Exception):
    UIDp = base_path + "BOADB__UID.txt"
    file = open(UIDp, "r")
    UID = file.read()
    file.close()

    PWDp = base_path + "SandboxDB__PWD.txt"
    file = open(PWDp, "r")
    PWD = file.read()
    file.close()

    uidBOAp = base_path + "BOADB__UID.txt"
    file = open(uidBOAp, "r")
    uidBOA = file.read()
    file.close()

    pwdBOAp = base_path + "BOADB__PWD.txt"
    file = open(pwdBOAp, "r")
    pwdBOA = file.read()
    file.close()

    WalgreensUIDp = base_path + "Walgreens_UID.txt"
    file = open(WalgreensUIDp, "r")
    WalgreensUID = file.read()
    file.close()

    WalgreensPWDp = base_path + "Walgreens_PWD.txt"
    file = open(WalgreensPWDp, "r")
    WalgreensPWD = file.read()
    file.close()

    VendorCentralUIDp = base_path + "VendorCentral_UID.txt"
    file = open(VendorCentralUIDp, "r")
    VendorCentralUID = file.read()
    file.close()

    VendorCentralPWDp = base_path + "VendorCentral_PWD.txt"
    file = open(VendorCentralPWDp, "r")
    VendorCentralPWD = file.read()
    file.close()

    EdgeUIDp = base_path + "Edge_UID.txt"
    file = open(EdgeUIDp, "r")
    EdgeUID = file.read()
    file.close()

    EdgePWDp = base_path + "Edge_PWD.txt"
    file = open(EdgePWDp, "r")
    EdgePWD = file.read()
    file.close()

    EdgeAPI_Keyp = base_path + "EdgeAPI_Key.txt"
    file = open(EdgeAPI_Keyp, "r")
    EdgeAPI_Key = file.read()
    file.close()

    EdgeAPI_UserUUIDp = base_path + "EdgeAPI_UserUUID.txt"
    file = open(EdgeAPI_UserUUIDp, "r")
    EdgeAPI_UserUUID = file.read()
    file.close()

    EdgeAPI_ClientUUIDp = base_path + "EdgeAPI_ClientUUID.txt"
    file = open(EdgeAPI_ClientUUIDp, "r")
    EdgeAPI_ClientUUID = file.read()
    file.close()

    iSpotUIDp = base_path + "iSpot_UID.txt"
    file = open(iSpotUIDp, "r")
    iSpotUID = file.read()
    file.close()

    iSpotPWDp = base_path + "iSpot_PWD.txt"
    file = open(iSpotPWDp, "r")
    iSpotPWD = file.read()
    file.close()

    CDP_Storage_EndPoint_Keyp = base_path + "CDP_Storage_EndPoint_Key.txt"
    file = open(CDP_Storage_EndPoint_Keyp, "r")
    CDP_Storage_EndPoint_Key = file.read()
    file.close()

    CDP_Storage_Endpointp = base_path + "CDP_Storage_Endpoint.txt"
    file = open(CDP_Storage_Endpointp, "r")
    CDP_Storage_Endpoint = file.read()
    file.close()

# Data Team Contact Email String
DataTeam = f"rachel.addlespurger@abbott.com; daniel.shields@abbott.com; heather.motto@abbott.com; \
carly.goodman@abbott.com; brianna.thomas@abbott.com; manish.subedi@abbott.com; rekha.selvasekaran@abbott.com"

# ODBC Connection Strings to BOA Environments for Automation

odbcConnStrMIDASQLBOA = f"Driver={{ODBC Driver 17 for SQL Server}};\
Server=azp02ads.database.windows.net;\
database=azp05atp;\
Uid={uidBOA};\
Pwd={pwdBOA};\
Encrypt=yes;\
TrustServerCertificate=no;\
Connection Timeout=1000;\
Authentication=ActiveDirectoryPassword;"

odbcConnStrSynpase = f"Driver={{ODBC Driver 17 for SQL Server}};\
Server=anpd-mida-synapse-workspace.sql.azuresynapse.net;\
database=anpd_mida_sql_pool;\
Uid={uidBOA};\
Pwd={pwdBOA};\
Encrypt=yes;\
TrustServerCertificate=no;\
Connection Timeout=1000;\
Authentication=ActiveDirectoryPassword;"
