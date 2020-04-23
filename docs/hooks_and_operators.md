#Hooks & Operators
The current version of mini-BRS contains Hooks and Operators designed for the ServiceNow platform. Following Operators and Hooks
are the part of current release and in future various other operators and hooks will be released to support cloud platforms.

##Hook's

*  servicenow_hook

##Operator's

1. **servicenow_to_sftp_transfer_operator :**
###Database Operators
   
   The `Database Operators` transfers the data from `ServiceNow` to a database. The current version of miniBRS supports three
   database operators.The database tranfser operators are `ServiceNowToMYSQLTransferOperator`, 
   `ServiceNowToMSSQLTransferOperator` and `ServiceNowToPostgresqlTransferOperator`.
   
   Use the  `ServiceNowToMYSQLTransferOperator` to transfer data to the MySql database.
 
```
       
#plugins/mbrs/operators/servicenow_to_mysql_transfer_operator.py
   
task = ServiceNowToMYSQLTransferOperator(task_id = 'your_task_id',
                                         dag = dag,
                                         snow_id = 'servicenow_default',
                                         config = 'config',
                                         storage_conn_id = 'mysql_default',
                                         table = table_name,
                                         execution_date = dag.params.get('execution_date')
                                        ) 
   
```
**Where** 

   * `task_id`: It is the unique id for the task so that the task (or operator) can be identified.
   * `dag`: It is the name of the dag instance to which the task belongs. In the current case to which `dag` the `task_id` belongs. 
   * `snow_id`: It is the `ServiceNow` connection id from which the data is being pulled.
   * `config`: It points to the configuration variable(config) stored in the `Airflow UI`.
   * `storage_conn_id`: It is a connection id of particular database storage that contains the credentials of a database so that we are able to create a connection with the database. And stores the parsed data into the database  
   * `table`: It contains the name of the table for which the data is pulled from the `ServiceNow`.
   * `execution_date`: It contains the execution date for the task with id `task_id`.

Similarly `ServiceNowToMSSQLTransferOperator`  and `ServiceNowToPostgresqlTransferOperator` takes the following form:

`ServiceNowToMSSQLTransferOperator:`
```
       
#plugins/mbrs/operators/servicenow_to_mssql_transfer_operator.py
  
task = ServiceNowToMSSQLTransferOperator(task_id = 'your_task_id',
                                         dag = dag,
                                         snow_id ='servicenow_default',
                                         config = 'config',
                                         storage_conn_id = 'mssql_default',
                                         table = table_name,
                                         execution_date = dag.params.get('execution_date')
                                        )
   
```

`ServiceNowToPostgresqlTransferOperator:`
```
       
#plugins/mbrs/operators/servicenow_to_postgresql_transfer_operator.py
   
task = ServiceNowToPostgresqlTransferOperator(task_id = 'send_data_to_submission',
                                              dag = dag,
                                              snow_id = 'servicenow_default',
                                              config = 'config',
                                              storage_conn_id = 'postgresql_default',
                                              table = table_name,
                                              execution_date = dag.params.get('execution_date')
                                             )
   
```

###Cloud Operators
    
   The `Cloud Operators` transfers the data from `ServiceNow` to a `Cloud storage`. The current version of miniBRS supports two cloud operators. The cloud transfer operators are `ServiceNowToS3TransferOperator` and `ServiceNowToDropboxTransferOperator`.

   Use the  `ServiceNowToS3TransferOperator` to transfer data to the `S3` cloud storage.
 
```
       
#plugins/mbrs/operators/servicenow_to_s3_transfer_operator.py
   
task = ServiceNowToS3TransferOperator(task_id = 'your_task_id',
                                      dag = dag,
                                      snow_id = 'servicenow_default',
                                      config = 'config',
                                      storage_conn_id = 's3_default',
                                      table = table_name,
                                      execution_date = dag.params.get('execution_date')
                                     ) 
   
```
**Where**

   * `task_id`: It is the unique id for the task so that the task (or operator) can be identified.
   * `dag`: It is the name of the dag instance to which the task belongs. In the current case to which `dag` the `task_id` belongs. 
   * `snow_id`: It is the `ServiceNow` connection id from which the data is being pulled.
   * `config`: It points to the configuration variable(config) stored in the `Airflow UI`.
   * `storage_conn_id`: It is a connection id of particular online storage that contains the credentials of online storage so that we are able to create a connection with the storage. And stores the file in it.  
   * `table`: It contains the name of the table for which the data is pulled from the `ServiceNow`.
   * `execution_date`: It contains the execution date for the task with id `task_id`.
   
Similarly `ServiceNowToDropboxTransferOperator` takes the following form:

`ServiceNowToDropboxTransferOperator:`
```
       
#plugins/mbrs/operators/servicenow_to_dropbox_transfer_operator.py
  
task = ServiceNowToDropboxTransferOperator(task_id = 'your_task_id',
                                           dag = dag,
                                           snow_id ='servicenow_default',
                                           config = 'config',
                                           storage_conn_id = 'dropbox_default',
                                           table = table_name,
                                           execution_date = dag.params.get('execution_date')
                                          )
   
```

###Network Operators
   The `Network Operators` transfers the data from the `ServiceNow` to a place where we have defined the storage.
   The current version of miniBRS supports only `ServiceNowToSFTPTransferOperator`.
   
   Use the  `ServiceNowToSFTPTransferOperator` to transfer data to the `SFTP` storage.
 
```
       
#plugins/mbrs/operators/servicenow_to_sftp_transfer_operator.py
   
task = ServiceNowToSFTPTransferOperator(task_id = 'your_task_id',
                                        dag = dag,
                                        snow_id = 'servicenow_default',
                                        config = 'config',
                                        storage_conn_id = 'sftp_default',
                                        table = table_name,
                                        execution_date = dag.params.get('execution_date')
                                       ) 
   
```

**Where**
   
   * `storage_conn_id`: It is a connection id of storage that contains the credentials of `SFTP` storage so that we are able to create a connection with it. And stores the files into the `SFTP` storage.
   * The rest parameters are the same as for the above operators.  
