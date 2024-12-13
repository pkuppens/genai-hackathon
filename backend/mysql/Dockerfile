# Use MySQL image based on Alpine Linux
FROM mysql:8.0-alpine

# Set environment variables for MySQL container configuration
# These variables can be overridden by providing different values at runtime
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=mypassword

# Download the SQL data file, gunzip, and apply it to the database
RUN wget -O /docker-entrypoint-initdb.d/large-demo-data-2-2-1.sql.gz https://openmrs.atlassian.net/wiki/download/attachments/26273323/large-demo-data-2-2-1.sql.gz?api=v2 \
    && gunzip /docker-entrypoint-initdb.d/large-demo-data-2-2-1.sql.gz

# Copy all files from the api directory and assume a main entry point in api/main.py
COPY ./backend/api /app/api

# Use CMD to call start.sh to initialize MySQL server and start the FastAPI server
CMD ["sh", "/app/start.sh"]
