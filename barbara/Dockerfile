FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code - explicitly copy all necessary files
COPY barbara_agent.py .
COPY services/ ./services/
COPY tools/ ./tools/
COPY api/ ./api/

# Set PYTHONPATH to ensure imports work
ENV PYTHONPATH=/app

# Expose port
EXPOSE 3000

# Run the agent
CMD ["python", "barbara_agent.py"]


