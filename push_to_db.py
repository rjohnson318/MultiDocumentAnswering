#Auth the client
RES_GROUP="AI-Index-RG-01"
ACCT_NAME="ai-index"

ACCOUNT_URI="https://ai-index.documents.azure.com:443/"   #$(az cosmosdb show --resource-group $RES_GROUP --name $ACCT_NAME --query documentEndpoint --output tsv)
ACCOUNT_KEY="6976vRmIKU0aqwkBIVQ9a3dfjN0a6yrhxWUR0y6n3MAUSGGS4VdtbdM1eYFp4c1ucbJ0eTNTPNtfACDbhioVTw=="   #$(az cosmosdb list-keys --resource-group $RES_GROUP --name $ACCT_NAME --query primaryMasterKey --output tsv)

#Creat the client
from azure.cosmos import CosmosClient
import os
import json

URL = ACCOUNT_URI
KEY = ACCOUNT_KEY
client = CosmosClient(URL, credential=KEY)
DATABASE_NAME = 'employee_handbook'
database = client.get_database_client(DATABASE_NAME)
CONTAINER_NAME = 'mainIndex'
container = database.get_container_client(CONTAINER_NAME)


# specify the path to your JSON file
json_file_path = "/home/rjohnson/Documents/Document_Q_A/MultiDocumentAnswering/index1.json"

# read the file
with open(json_file_path, "r") as json_file:
    json_data = json.load(json_file)

# Make sure the json_data is a list
if not isinstance(json_data, list):
    json_data = [json_data]

# insert the JSON data into the container
for item in json_data:
    container.upsert_item(item)