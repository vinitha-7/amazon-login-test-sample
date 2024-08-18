# Pre-requisites
1. Install Python & PIP
2. Install Python IDE
3. Browserstack account
4. GitHub account with a repository created


# Steps to execute the test through CLI


## Download the sample project
Download or clone the sample project that integrates Selenium with BrowserStack.
Use the following command to clone the repository:
```
git clone -b main https://github.com/browserstack/python-selenium-browserstack
```
Use the following link to download the sample project:
```
https://github.com/browserstack/python-selenium-browserstack/archive/refs/heads/main.zip
```

## Open the project in a Python IDE
Open the project in your preferred Python-based IDE (such as PyCharm).

## Update test script
Update the existing scripts based on the business requirement, if needed.

## Update browserstack.yml
Edit the browserstack.yml file with the necessary configurations:
* Set your BrowserStack credentials (username and access key).
* Specify the platform, browser name, and version you want to test (e.g., Chrome on Windows 10).
* Enable parallel testing if needed.
* Set a project name and build name.
  
Here’s an example snippet:

```
userName: vinithasenthil_7KDNSI
accessKey: 7csdWMa9eY9LF3sP55HD
platforms:
  - os: Windows
    osVersion: 10
    browserName: Chrome
    browserVersion: 122.0
  - os: Windows
    osVersion: 10
    browserName: Edge
    browserVersion: latest
browserstackLocal: true
buildName: browserstack-build-1
projectName: BrowserStack Sample
```
## Navigate to the project root folder/ directory
Navigate to the project root folder/ directory using the following command:
```
cd root-folder-name
```
## Create a python virtual environment and Install dependencies
Set up a Python virtual environment (if you haven’t already):
```
python -m venv env
env\Scripts\activate
```
Install the required dependencies using pip:
```
pip3 install -r requirements.txt
```
## Execute the test
Run your test file from the root directory of the project using the command line:
```
browserstack-sdk python ./tests/amazon-login-test.py
```

## View test results
The test will be executed in the BrowserStack Automate console. Once the execution is completed, validate the BrowserStack Test Result dashboard for test execution videos and logs.

&nbsp;

# Steps to execute the test through Github Actions CI/CD pipline

## Initialize a local Git repository and integrate with a remote GitHub repository

Create a local Git repository and set the default branch to main
```
git init -b main
```
Create a feature branch and switch to the new feature branch to make any edits
```
git branch feature-test
git checkout feature-test
```
Add your updated project files to the feature branch
```
git add . or git add updated-file-name
```

Commit the staged project files
```
git commit -m "added test files"
```

Add the remote GitHub repository (replace REMOTE-URL with the actual URL)
```
git remote add origin REMOTE-URL
```
Use the following command to push the current branch and set the remote as upstream
```
git push --set-upstream origin feature-test
```
Note: If you are initializing and pushing the code for the first time in your new repository, you will be redirected for authentication. If authentication is successful, your changes will be pushed to your repository.

## Merge the latest changes from feature branch to main branch in remote Git repository
Go to the Pull Requests section and create a new pull request from feature branch to main branch by comparing the changes.
Select merge option to merge the changes to the main branch.

## Execute tests from the remote GitHub repository using GitHub Actions
Take the Commit SHA ID for the latest code push from the pull requests section.
In the Actions section, select the workflow and run it with the full Commit SHA ID.
The workflow will be triggered on GitHub Action runners according to your configuration, and the tests will be executed in the BrowserStack Automate console.


## Validate test results
Validate the BrowserStack test result dashboard for test execution videos and logs in the BrowserStack Automate console.

