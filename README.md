Airflow + dbt + Snowflake

This project demonstrates how Airflow, dbt, warehouse (such Snowflake) works together to make a data pipeline.
I don't have a Snowflake account at this point, so not able to configure connection profile in jerrywang_dbt_project/profiles.yml (any db connection properties is defined in here)

docker-compose.yaml file is fetched from here:  https://airflow.apache.org/docs/apache-airflow/2.3.0/docker-compose.yaml
and updated to fit this project.

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