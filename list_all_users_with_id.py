import boto3

boto3.setup_default_session (profile_name='profile_name')
session = boto3.Session (profile_name='profile_name')

organizations = session.client ('organizations')
iam = boto3.client ('iam')

account_suspended = []
account_active = []

accounts = []
accounts_prd = []
another_accounts = []

def all_users_all_accounts():
    accounts = []

    response = organizations.list_accounts ()
    accounts.extend (response['Accounts'])
    while 'NextToken' in response.keys ():
        response = organizations.list_accounts (NextToken=response['NextToken'])
        accounts.extend (response['Accounts'])
    print ('accounts found: ' + str (len (accounts)))


    for i in accounts:
        id_account = i['Id']
        status = i['Status']
        name = i['Name']
        if status == 'SUSPENDED':
            #Quando for comparar strings é bom normalizar antes (geralmente coloco pra minusculo) = Ficaria assim status.lower() == 'suspended'
            account_suspended.append ({"Name": name, "id_account": id_account, "Status": status})
        else:
            account_active.append ({"Name": name, "id_account": id_account, "Status": status})

    # for contas in account_active:
    #     account_prd = contas['Name']
    #     if '-prd' in account_prd:
    #         accounts_prd.append (account_prd)
    #     else:
    #         another_accounts.append (account_prd)

    for account in account_active:
        print ()
        id_account_name = str(account['Name'])
        id_account_id = str(account['id_account'])
        print ('Account:', account['Name'], 'Id:', account['id_account'])

        credentials = session.get_credentials ()
        sts = session.client ('sts')
        assume_role_response = sts.assume_role (
            RoleArn=f"arn:aws:iam:XXXXXXXXXXXX:{account['id_account']}:role/role_name",
            RoleSessionName="AssumeRoleSession1"
        )
        temp_session = boto3.Session (
            aws_access_key_id=assume_role_response['Credentials']['AccessKeyId'],
            aws_secret_access_key=assume_role_response['Credentials']['SecretAccessKey'],
            aws_session_token=assume_role_response['Credentials']['SessionToken']
        )
        iam = temp_session.client ('iam')

        response = iam.list_users ()
        users = response['Users']
        while 'Marker' in response.keys ():
            response = iam.list_users (Marker=response['Marker'])
            users.extend (response['Users'])
        print (f'Total usuários: {len (users)}')

        # Update the credentials for each user
        for user in users:
            username = user.get('UserName')
            userid = user.get('UserId')
            print('User:',username, 'id:', userid)

def list_users_one_account():
    users = []
    # Get all IAM users
    response = iam.list_users()
    users.extend(response['Users'])
    while 'Marker' in response.keys():
        response = iam.list_users(Marker=response['Marker'])
        users.extend(response['Users'])
        # print(users)
    print(f'Total usuários: {len(users)}')

    # list users
    for user in users:
        username = user.get('UserName')
        print(username)
    # print(f'Total usuários: {len(users)}')

all_users_all_accounts ()
