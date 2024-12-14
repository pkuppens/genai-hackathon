## Dockerfile for MySQL with OpenMRS data, based on conventions from the official MySQL image.

# 1. Use MySQL 8.0 base image on Debian
FROM mysql:8.0.40-debian

# 2. Set default environment variables for MySQL initialization
#    These can be overridden at runtime.
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=mypassword

# 3. Retrieve the SQL file and place it into the init directory
#    The official MySQL entrypoint runs all *.sql files here at startup.
USER root

RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN wget -q -O /docker-entrypoint-initdb.d/large-demo-data-2-2-1.sql.gz \
    "https://openmrs.atlassian.net/wiki/download/attachments/26273323/large-demo-data-2-2-1.sql.gz?api=v2" \
    && gunzip /docker-entrypoint-initdb.d/large-demo-data-2-2-1.sql.gz \
    && chown mysql:mysql /docker-entrypoint-initdb.d/large-demo-data-2-2-1.sql

# 4. Switch back to mysql user (optional, as the entrypoint might handle it)
USER mysql

# 5. Expose MySQL port
EXPOSE 3306

# 6. No need to redefine CMD. The base image already sets the CMD and entrypoint
#    to run `mysqld` and initialize the database from /docker-entrypoint-initdb.d/.
