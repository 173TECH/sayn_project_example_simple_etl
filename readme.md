# SAYN Project Example: A Simple ETL

This is an example SAYN project. It shows you how to implement a simple ETL with SAYN.

This project extracts jokes from an API, translates them into Yodish (the language of Yoda, this is) with another API and then run some SQL transformations on the extracted data. Both APIs are public and do not require an API key. However, they both have limited quotas (especially the Yodish translation API) so you should avoid re-running the extraction part of the project multiple times in a row.

Through this includes the usage of the following SAYN features:

* Python task to extract data with APIs.
* Autosql tasks to automate SQL transformations.
* Usage of parameters to make the code dynamic.
* Usage of presets to define tasks.

**Please note that you will need to rename the `settings_sample.yaml` file to `settings.yaml` after cloning the repository. Otherwise the SAYN project will not run properly. You should be in the root folder of the repository when running the project.**

----
Quick SAYN overview:

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

For more details on SAYN, you can see the documentation here: https://173tech.github.io/sayn/
