# Production Engineering - Portfolio Site

Welcome to the website created by Matthew Chang for the MLH Fellowship! This site is a fullstack application that utilizes Flask, Jinja, Python, and MySQL for displaying information and storing timeline posts that are retrievable and Nginx for secure connection protocols. Several Docker containers were then created and hosted on a DNS for deployment. To enhance the productivity and efficiency after each code change, multiple scripts were created in this repository and in [this repo](https://github.com/MatthewCCChang/DeploymentScript) so repetitive tasks can be handled quickly. Throughout the program, test-driven development was used and multiple unit tests were created for testing individual pages, database operations, and a health endpoint was created for testing the overall health of the application. After the completion of the scripts, CI/CD pipelines were also established to ensure quality code and employ security measures through Github Actions. Finally, Prometheus and Grafana were used to monitor network traffics and cadvisor for sending out alerts regarding services being down. 


## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

Uncomment line 10 in ```app/init.py``` so a temporary database is created for testing purposes

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
