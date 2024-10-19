# LAB-2754 Sample Portal

This Repo contains a sample web portal (Provisioning Portal) that allows you to perform certain administrative and/or user functions on Cisco Collaboration products. This Repo is accompanying Webex One LAB-2754

* master Branch contains the fully built-out Portal
* skeleton Branch contains a partially built-out Portal that is meant to be used while Following the [Webex One Lab Guide](https://apilab.webexone.com/)


## Steps to start up the Portal after Cloning

### Step 1

Make sure python3 is installed (```/usr/bin/env python3 --version```)\
See [pyenv](https://github.com/pyenv/pyenv/wiki)\
See [pyenv-installer](https://github.com/pyenv/pyenv-installer)\
You may also install/use a virtual environment\
See [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

### Step 2

Install all python requirements with:

```pip install -r requirements.txt```

### Step 3

Now you need to start the web service with ```./app.py``` in order to start the Flask development server.

### Step 4

The web server is ready once these messages appear:

```
 * Serving Flask app "flaskr" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 255-014-512
 ```

### Step 5

In your browser, access the page using `http://localhost:5000`

## VS Code Debug Run Setup ##

In your VSCode go to your Command Palette (Ctrl + Shift + P /  Cmd + Shift + P) and Type Debug: Open launch.json

Populate your your launch.json file with the following or append to your existing configurations list:

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: hello_world.py",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/examples/hello_world.py",
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Python: soap_axl.py",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/examples/soap_axl.py",
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Python: soap_sxml.py",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/examples/soap_sxml.py",
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Python: wxc_enable_user.py",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/examples/wxc_enable_user.py",
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Python: service_app.py",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/examples/service_app.py",
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Python: wxm_create_meeting.py",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/examples/wxm_create_meeting.py",
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Python: wbx_messages.py",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/examples/wbx_messages.py",
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Python: oauth.py",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/examples/oauth.py",
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Start LAB-2754 Portal",
            "type": "python",
            "request": "launch",
            "module": "flask",
            // https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
            "env": {
                "FLASK_APP": "app.py",
                "FLASK_ENV": "development",
                "FLASK_DEBUG": "0"
            },
            "args": [
                "run",
                "--host=0.0.0.0",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true
        }
    ]
}
