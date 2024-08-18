# Pre-requisites
1. Install Python & PIP
2. Install Python IDE
3. Browserstack account
4. GitHub account 


# Steps to execute the test through CLI


## Download the sample project
Download or clone the sample project that integrates Selenium with BrowserStack.
Use the following command to clone the repository:
```
git clone -b main https://github.com/browserstack/python-selenium-browserstack
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

Add your project files to the local Git repository
```
git add .
```

Commit the staged project files
```
git commit -m "added test files"
```

Add the remote GitHub repository (replace REMOTE-URL with the actual URL)
```
git remote add origin REMOTE-URL
```

Push the project files from the local Git repository to the remote GitHub repository
```
git push origin main
```

## Execute tests from the remote GitHub repository using GitHub Actions
Go to the Pull Request section and find the Commit SHA ID for the latest code push.
In the Actions section, select the workflow and run it with the full Commit SHA ID.
The workflow will be triggered on GitHub Action runners according to your configuration, and the tests will be executed in the BrowserStack Automate console.


## Validate test results
Validate the BrowserStack test result dashboard for test execution videos and logs in the BrowserStack Automate console.

