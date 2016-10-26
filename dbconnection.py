import os
from subprocess import Popen, PIPE

def runSqlQuery(tableName):
    d = {}
    with open('datamigration.properties') as f:
        for line in f:
            if not line.strip():
                continue
            key, value = line.split('=')
            d[key] = value.strip()
            
    connectString = d["OWNER_USER"]+'/'+d["OWNER_PASSWORD"]+'@'+d["DATABASE_URL"]
    os.environ['ORACLE_HOME'] = "/u01/app/oracle/product/11.2.0/xe"
    session = Popen(['/u01/app/oracle/product/11.2.0/xe/bin/sqlplus', '-S', connectString], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    sqlCommand ='select count(*) from '+ tableName +';'
    session.stdin.write(sqlCommand)
    queryResult, errorMessage = session.communicate()
    return queryResult.split('\n')[3].strip()

print runSqlQuery('SUB_SUBSCRIBER')
