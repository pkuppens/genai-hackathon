# Use MySQL image based on Debian Linux as the base image
FROM mysql:8.0-debian

# Set environment variables for MySQL container configuration
# These variables act as defaults and can be overridden at runtime by passing different values
# during container startup using the --env or --env-file option.
# Example to override:
#   docker run --env MYSQL_ROOT_PASSWORD=newpassword my-mysql-image
#   OR
#   docker run --env-file custom_env_file.env my-mysql-image

# The following environment variables are defaults for the MySQL image to configure the MySQL server
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=mypassword

# Install wget and clean up apt cache to reduce image size
RUN apt-get update && apt-get install -y wget dos2unix uvicorn \
    && rm -rf /var/lib/apt/lists/*

# Download the SQL data file, extract it, and place it in the init directory
# This SQL file will be executed when the container initializes the database
RUN wget -O /docker-entrypoint-initdb.d/large-demo-data-2-2-1.sql.gz https://openmrs.atlassian.net/wiki/download/attachments/26273323/large-demo-data-2-2-1.sql.gz?api=v2 \
    && gunzip /docker-entrypoint-initdb.d/large-demo-data-2-2-1.sql.gz

# Copy the API directory into the container
# Note: This expects the docker build command to be started from the "backend" directory
# Example build command:
#   cd backend
#   docker build -t my-mysql-image -f mysql/Dockerfile .
COPY ./api /app/api

WORKDIR /app

COPY start.sh /app/start.sh
RUN dos2unix /app/start.sh
RUN chmod +x /app/start.sh

# Expose MySQL default port for external connections
EXPOSE 3306

# Define the command to initialize MySQL and start the FastAPI server
# The "start.sh" script must handle both the MySQL server initialization
# and any API-related startup logic
CMD ["sh", "/app/start.sh"]
