# SAYN Project Example: A Simple ETL

## Project Description

This is an example [SAYN](https://github.com/173TECH/sayn) project which shows how to implement a simple ETL with the framework.

This ETL extracts jokes from an API, translates them into Yodish (the language of Yoda, this is) with another API and then runs some SQL transformations on the extracted data. Both APIs are public and do not require an API key. However, they both have limited quotas (especially the Yodish translation API) so you should avoid re-running the extraction part of the project multiple times in a row (you can use the command `sayn run -x tag:extract` after the first `sayn run`).

This project includes the usage of the following SAYN features:

* Python task to extract data with APIs.
* Autosql tasks to automate SQL transformations.
* Usage of parameters to make the code dynamic.
* Usage of presets to define tasks.

By default, the project uses SQLite as a database. You can use [DB Browser for SQLite](https://sqlitebrowser.org/dl/) to navigate the data easily.

**To run the project, you will need to:**

* clone the repository with the command `git clone [https://github.com/173TECH/sayn_project_example_simple_etl.git`.
* rename the `settings_sample.yaml` file to `settings.yaml`.
* install the project dependencies by running the `pip install -r requirements.txt` command from the root of the project folder.
* run all SAYN commands from the root of the project folder.

## Running The Project With PostgreSQL

If desired, you can also run the project using a PostgreSQL database. For this, you simply need to:

* change the `warehouse` credential to use a PostgreSQL database connection.
* install `psycopg2` as a package.

## SAYN Quick Overview

SAYN uses 2 key files to control the project:
  - settings.yaml: individual settings which are not shared
  - project.yaml: project settings which are shared across all collaborators on the project

SAYN code is stored in 3 main folders:
  - tasks: where the SAYN tasks are defined. Each YAML file in this folder represents a task group.
  - sql: code for SQL tasks
  - python: code for python tasks

SAYN uses some key commands for run:
  - sayn run: run the whole project
    - -p flag to specify a profile when running sayn: e.g. sayn run -p prod
    - -t flag to specify tasks to run: e.g. sayn run -t task_name
    - -t group:group_name to specify a task group to run: e.g. sayn run -t group:group_name
  - sayn compile: compiles the code (similar flags apply)
  - sayn --help for full detail on commands

For more details on SAYN, you can see:
* the [documentation](https://173tech.github.io/sayn/)
* the [tutorials](https://173tech.github.io/sayn/tutorials/tutorial_part1/)
