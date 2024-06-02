Airflow + dbt + Snowflake

This project demonstrates how Airflow, dbt, warehouse (such Snowflake) works together to make a data pipeline.
I don't have a Snowflake (licensed) account at this point, so not able to configure connection profile in jerrywang_dbt_project/profiles.yml (any db connection properties is defined in here)

docker-compose.yaml file is fetched from here:  https://airflow.apache.org/docs/apache-airflow/2.3.0/docker-compose.yaml
and updated to fit this project.
After executing docker compose up --build, open browser and 127.0.0.1:8080 to browse airflow webpage with login both username and password: airflow
<img width="1905" alt="Screenshot 2024-06-01 at 8 52 38 PM" src="https://github.com/SHSKGIT/Airflow_dbt_snowflake/assets/23388907/b50ce308-4aec-4245-ac6d-283397dea043">


The followings are workflow.


DBT:

As per jerrywang_dbt_project/dbt_project.yml, 
seeds are defined in jerrywang_dbt_project/seeds where CSV files will be loaded onto warehouse.
In this project, there are 3 CSV files.
models are defined in jerrywang_dbt_project/models where .sql fixtures are defined and will be executed in dags.
dbt commands:
<dbt init> to create a dbt project.
<dbt deps> to add or update an existing package configuration. (not done in this project)
<dbt seed> to load CSV files located in the seed-paths directory of dbt project into a data warehouse.


Airflow:

There are 2 dags defined in this project.
One is for loading CSV files into Snowflake, the other one is for doing data transformation and analysis (based on whatever BI needs)


Docker:
docker-compose build
docker-compose up


Go to Airflow website, create dbt_user and dbt_password under Admin > Variables.
There appear to be 2 dags on UI, make them enabled by clicking blue button,
Trigger dag init_dag to seed data into Snowflake,
I can't see in Snowflake, but there should be 3 tables appearing in Snowflake
Then trigger dag transformation_analysis_dag to transform and analyze data on Snowflake,
there should be 3 views under transform, and 1 view under analysis.


For BI data visualization:
I don't have a Looker (licensed) account.
Reference: https://cloud.google.com/looker/docs/db-config-snowflake

Basically, the processes are as follow:
create a Looker user on Snowflake.
In Looker, create connection to Snowflake.
Add groups/users in Looker, and assign Snowflake name and value.

Happy being a data engineer \\^.^/
