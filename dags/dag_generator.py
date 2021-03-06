#   mbrs
#   Copyright (c)Cloud Innovation Partners 2020.
#   Author : Shahbaz Ali

from airflow import DAG
from datetime import datetime
from plugins.mbrs.utils import generator

with DAG(
    dag_id='dag_generator',
    description='Generates DAG corresponding to a specific table',
    schedule_interval=None,
    start_date=datetime(2020, 11, 1),
    catchup=False,
    default_args={
        'owner': 'BRS',
    }
) as dag:

    if not generator.ini():
        generator.is_servicenow_default_connection_available()
        generator.is_rest_connection_available()
        generator.is_config_variable_set()
        generator.is_storage_defined()
        generator.is_recovery_variable_set()
        generator.create_dags()



