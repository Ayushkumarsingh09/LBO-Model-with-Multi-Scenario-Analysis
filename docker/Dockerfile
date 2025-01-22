# Use official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the notebooks
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root"]
