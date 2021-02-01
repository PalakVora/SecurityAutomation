    *** Settings ***
    Library           CassandraCQLLibrary
    Library           Collections
    Suite Setup       Connect To Cassandra    127.0.0.1    9042
    Suite Teardown    Disconnect From Cassandra

    *** Test Cases ***
    Get Keyspaces
        Execute CQL    USE system
        ${result}    Execute CQL    SELECT * FROM schema_keyspaces;
        Log List    ${result}
        Log    ${result[1].keyspace_name}