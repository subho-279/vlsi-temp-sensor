# Use a lightweight base image
FROM debian:bullseye-slim

# Install ngspice and Python
RUN apt-get update && apt-get install -y \
    python3 python3-pip ngspice git && \
    apt-get clean

# Install Python dependencies
RUN pip3 install pandas matplotlib

# Set working directory
WORKDIR /app

# Copy everything into the container
COPY . .

# Default command: run ngspice simulation + plot script
CMD ngspice -b ptat_ctat_full.cir && python3 plot_sensor.py