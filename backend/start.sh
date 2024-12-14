#!/bin/sh

# Function to check if the SQL script exists, apply it if so, and rename/remove it to ensure idempotency
apply_sql_script() {
    SQL_SCRIPT="/docker-entrypoint-initdb.d/large-demo-data-2-2-1.sql"
    if [ -f "$SQL_SCRIPT" ]; then
        echo "Applying SQL script..."
        mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" "$MYSQL_DATABASE" < "$SQL_SCRIPT"
        mv "$SQL_SCRIPT" "${SQL_SCRIPT}.applied"
        echo "SQL script applied and renamed to ensure idempotency."
    else
        echo "No SQL script to apply."
    fi
}

# Start the MySQL server
docker-entrypoint.sh mysqld &

# Wait for MySQL server to be ready
echo "Waiting for MySQL server to be ready..."
until mysqladmin ping -h "127.0.0.1" --silent; do
    sleep 1
done

# Apply the SQL script if it exists
apply_sql_script

# Start the FastAPI application with error handling
# echo "Starting FastAPI application..."
# if ! uvicorn api.main:app --host 0.0.0.0 --port 8000; then
#     echo "Error: Failed to start FastAPI application"
# fi
