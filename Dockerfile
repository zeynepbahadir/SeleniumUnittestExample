# Use Python 3.13 as base image to match your environment
FROM python:3.13-slim

# Install Chrome and other dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    postgresql-client \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && chmod +x /usr/bin/chromedriver

# Set Chrome and ChromeDriver paths
ENV CHROME_BINARY_PATH=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Command to run the application
CMD ["python", "source/stepstone.py"]