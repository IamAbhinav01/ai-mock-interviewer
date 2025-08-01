# Use the official Jenkins LTS image as base
FROM jenkins/jenkins:lts

# Switch to root to install Docker
USER root

# Install Docker dependencies
RUN apt-get update -y && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    echo "deb [arch=amd64] https://download.docker.com/linux/debian bullseye stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update -y && \
    apt-get install -y docker-ce docker-ce-cli containerd.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add Jenkins user to the docker group
RUN groupadd -f docker && usermod -aG docker jenkins

# Create Docker data directory (for DinD, optional)
RUN mkdir -p /var/lib/docker
VOLUME /var/lib/docker

# Set back to Jenkins user
USER jenkins
