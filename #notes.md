#notes
input.txt is the raw text files that will be used
index.json is the indexed (prepared) content that the AI can understand
running build_index.py will populate the index.json with the same 20 questions from the content from input.txt
Then you can run answer_questions.py to ask questions at the target dataset.


#######
Database test in Azure
1- Database tested-----___ performace feel___slow or fast as compared to running it locally and other databases


#######
Database custom role creation code and output
```az cosmosdb sql role definition create --account-name ai-index --resource-group  AI-Index-RG-01 --body '{
    "RoleName": "PasswordlessReadWrite",
    "Type": "CustomRole",
    "AssignableScopes": ["/"],
    "Permissions": [{
        "DataActions": [
            "Microsoft.DocumentDB/databaseAccounts/readMetadata",
            "Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/items/*",
            "Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/*"
        ]
    }]
}'
{
  "assignableScopes": [
    "/subscriptions/f13ecc2a-bc95-40eb-b244-85bedf7febb1/resourceGroups/AI-Index-RG-01/providers/Microsoft.DocumentDB/databaseAccounts/ai-index"
  ],
  "id": "/subscriptions/f13ecc2a-bc95-40eb-b244-85bedf7febb1/resourceGroups/AI-Index-RG-01/providers/Microsoft.DocumentDB/databaseAccounts/ai-index/sqlRoleDefinitions/7684cc29-dd4b-4238-9ed5-8e22a14b4728",
  "name": "7684cc29-dd4b-4238-9ed5-8e22a14b4728",
  "permissions": [
    {
      "dataActions": [
        "Microsoft.DocumentDB/databaseAccounts/readMetadata",
        "Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/items/*",
        "Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers/*"
      ],
      "notDataActions": []
    }
  ],
  "resourceGroup": "AI-Index-RG-01",
  "roleName": "PasswordlessReadWrite",
  "type": "Microsoft.DocumentDB/databaseAccounts/sqlRoleDefinitions",
  "typePropertiesType": "CustomRole"
}
```

####
Assign new custom role to logged in user using user ID

```az cosmosdb sql role assignment create --account-name ai-index --resource-group  AI-Index-RG-01 --scope "/" --principal-id 32a17372-47c9-47f5-9bc8-061cc8da0319 --role-definition-id 7684cc29-dd4b-4238-9ed5-8e22a14b4728 ```

#### output

```{
  "id": "/subscriptions/f13ecc2a-bc95-40eb-b244-85bedf7febb1/resourceGroups/AI-Index-RG-01/providers/Microsoft.DocumentDB/databaseAccounts/ai-index/sqlRoleAssignments/d659e5dc-3c0c-44b1-b15a-49aa9b18d616",
  "name": "d659e5dc-3c0c-44b1-b15a-49aa9b18d616",
  "principalId": "32a17372-47c9-47f5-9bc8-061cc8da0319",
  "resourceGroup": "AI-Index-RG-01",
  "roleDefinitionId": "/subscriptions/f13ecc2a-bc95-40eb-b244-85bedf7febb1/resourceGroups/AI-Index-RG-01/providers/Microsoft.DocumentDB/databaseAccounts/ai-index/sqlRoleDefinitions/7684cc29-dd4b-4238-9ed5-8e22a14b4728",
  "scope": "/subscriptions/f13ecc2a-bc95-40eb-b244-85bedf7febb1/resourceGroups/AI-Index-RG-01/providers/Microsoft.DocumentDB/databaseAccounts/ai-index",
  "type": "Microsoft.DocumentDB/databaseAccounts/sqlRoleAssignments"
}```


#### Links
https://learn.microsoft.com/en-us/azure/azure-functions/openapi-apim-integrate-visual-studio
