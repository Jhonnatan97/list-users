# Script README

This script was developed to interact with AWS (Amazon Web Services) using the Boto3 library. It performs the following tasks:

## Prerequisites
- Python 3 installed
- Boto3 library installed (`pip install boto3`)
- AWS CLI configured with required credentials and profiles

## Settings
1. Install Python 3 if it is not already installed.
2. Install the Boto3 library by running the command `pip install boto3` in the terminal.

## Profile Configuration
1. Before running the script, make sure you've configured the AWS CLI with the required credentials and profiles. This script depends on the profiles defined in the AWS CLI configuration.
2. Open the script file and replace all occurrences of `'profile_name'` with the actual name of the profile you want to use for the AWS session.

## Running the Script
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is saved.
3. Run the script by running the `python # Script README

This script was developed to interact with AWS (Amazon Web Services) using the Boto3 library. It performs the following tasks:

## Prerequisites
- Python 3 installed
- Boto3 library installed (`pip install boto3`)
- AWS CLI configured with required credentials and profiles

## Settings
1. Install Python 3 if it is not already installed.
2. Install the Boto3 library by running the command `pip install boto3` in the terminal.

## Profile Configuration
1. Before running the script, make sure you've configured the AWS CLI with the required credentials and profiles. This script depends on the profiles defined in the AWS CLI configuration.
2. Open the script file and replace all occurrences of `'profile_name'` with the actual name of the profile you want to use for the AWS session.

## Running the Script
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is saved.
3. Run the script by running the `python list_all_users_with_id.py` command in the terminal, replacing `list_all_users_with_id.py` with the actual script file name.

## Script Overview

The script performs the following actions:

### 1. All Users on All Accounts
This section retrieves a list of all AWS accounts associated with the specified profile. It then iterates through each account and performs the following tasks:
- Identifies whether the account is suspended or active.
- Retrieves the name, ID and status of each account.
- Assumes a specific IAM role on the account.
- Retrieves a temporary session using the assumed role's credentials.
- Lists all IAM users in the account and prints their names and IDs.

### 2. List Users in an Account
This section retrieves a list of all IAM users in the current AWS account associated with the specified profile. It then lists the usernames of all users.

Note: The script includes commented code (`#`) that can be uncommented and modified to add additional functionality or customize the script's behavior as needed.

## Disclaimer
This script is provided as-is without any warranties. It is your responsibility to review and understand the code before running it in your environment. Use it at your own risk.

**Note:** The script assumes that you have already installed the necessary dependencies and correctly configured the AWS CLI.` command in the terminal, replacing `script_name.py` with the actual script file name.

## Script Overview

The script performs the following actions:

### 1. All Users on All Accounts
This section retrieves a list of all AWS accounts associated with the specified profile. It then iterates through each account and performs the following tasks:
- Identifies whether the account is suspended or active.
- Retrieves the name, ID and status of each account.
- Assumes a specific IAM role on the account.
- Retrieves a temporary session using the assumed role's credentials.
- Lists all IAM users in the account and prints their names and IDs.

### 2. List Users in an Account
This section retrieves a list of all IAM users in the current AWS account associated with the specified profile. It then lists the usernames of all users.

Note: The script includes commented code (`#`) that can be uncommented and modified to add additional functionality or customize the script's behavior as needed.

## Disclaimer
This script is provided as-is without any warranties. It is your responsibility to review and understand the code before running it in your environment. Use it at your own risk.

**Note:** The script assumes that you have already installed the necessary dependencies and correctly configured the AWS CLI.
