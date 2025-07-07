FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Create a non-root user and group
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
# Copy contents of app/ to /app in the image
COPY app/ /app/

# Ensure the app directory is owned by the appuser
# This might be needed if subsequent steps or the app itself needs to write to this directory
# For a read-only app, it might not be strictly necessary but is good practice.
RUN chown -R appuser:appgroup /app

# Expose the port the app runs on
EXPOSE 8000

# Switch to the non-root user
USER appuser

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]