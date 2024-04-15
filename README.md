# generi

**List of programs**

1. Integer
2. Interface
3. Model

```
import subprocess

def setup_docker():
    # Install Docker
    install_docker_cmd = "brew install docker"
    subprocess.run(install_docker_cmd, shell=True)

    # Start Docker service
    start_docker_cmd = "open --background -a Docker"
    subprocess.run(start_docker_cmd, shell=True)

    # Wait for Docker to start
    input("Press Enter once Docker has started...")

def create_docker_container(image_name, container_name):
    # Build Docker image
    build_image_cmd = f"docker build -t {image_name} ."
    subprocess.run(build_image_cmd, shell=True)

    # Create and run Docker container
    create_container_cmd = f"docker run -it --name {container_name} {image_name}"
    subprocess.run(create_container_cmd, shell=True)

def main():
    # Set up Docker
    setup_docker()

    # Define Docker image and container names
    image_name = "my_docker_image"
    container_name = "my_container"

    # Create and run Docker container
    create_docker_container(image_name, container_name)

if __name__ == "__main__":
    main()
```
