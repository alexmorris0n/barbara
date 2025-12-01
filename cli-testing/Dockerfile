# Barbara CLI Testing Service - Dockerfile for Fly.io
# This service needs both Node.js and Python to execute swaig-test

FROM node:20-slim

# Install Python 3 and pip (required for swaig-test)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      python3 \
      python3-pip \
      python3-venv \
      build-essential && \
    rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy package files for CLI testing service
COPY cli-testing/package*.json ./cli-testing/

# Install Node.js dependencies
WORKDIR /app/cli-testing
RUN npm install --production

# Allow pip to install system-wide in Debian-based image
ENV PIP_BREAK_SYSTEM_PACKAGES=1

# Go back to app root
WORKDIR /app

# Copy CLI testing service code
COPY cli-testing/ ./cli-testing/

# Copy Barbara agent code (needed for swaig-test)
COPY barbara/ ./barbara/

# Install Python dependencies for Barbara agent
COPY barbara/requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Create non-root user
RUN groupadd --gid 1001 nodejs && \
    useradd --uid 1001 --gid nodejs --shell /usr/sbin/nologin --create-home nodejs

# Change ownership
RUN chown -R nodejs:nodejs /app

# Switch to non-root user
USER nodejs

# Set working directory to cli-testing for server startup
WORKDIR /app/cli-testing

# Expose port
EXPOSE 8080

# Start application
CMD ["node", "server.js"]

