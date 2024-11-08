Here’s a step-by-step guide to set up and run your application with Docker, Jenkins, and Flask. I'll also explain which files to create manually and which will be generated automatically.

---

### Step 1: Set Up Your Project Directory and Files

1. **Create a Project Directory**:
   ```bash
   mkdir fapp2
   cd fapp2
   ```

2. **Create `app.py`** (your Flask application):
   ```python
   # app.py
   from flask import Flask
   app = Flask(__name__)

   @app.route('/')
   def run():
       return "sanjith"

   if __name__ == "__main__":
       app.run(host='0.0.0.0', port=5000)
   ```
   
   **Explanation**: This is your main Flask app file, which defines a simple endpoint and starts the server on port 5000.

3. **Create `requirements.txt`**:
   ```bash
   touch requirements.txt
   ```
   Open `requirements.txt` and add:
   ```
   Flask==2.0.1
   Werkzeug==2.0.1
   ```
   **Explanation**: This file lists the required Python dependencies. Docker will use this file to install dependencies when building the image.

4. **Create `Dockerfile`**:
   ```dockerfile
   # Dockerfile
   FROM python:3.10
   WORKDIR /app
   COPY . /app
   RUN pip install -r requirements.txt
   EXPOSE 5000
   CMD ["python3", "app.py"]
   ```

   **Explanation**: The Dockerfile defines the environment for the Flask app, installs dependencies, exposes port 5000, and specifies the command to start the application.

---

### Step 2: Build and Run the Docker Container Locally

1. **Build the Docker Image**:
   ```bash
   docker build -t fapp2 .
   ```
   - This command creates a Docker image named `fapp2` based on the Dockerfile.

2. **Run the Docker Container**:
   ```bash
   docker run -p 5000:5000 fapp2
   ```
   - This command runs the container and maps port 5000 on the container to port 5000 on your local machine.
   - **Access the app**: Open a browser and go to `http://localhost:5000` to see the message "sanjith".

---

### Step 3: Set Up Jenkins to Automate Builds

1. **Install Jenkins**:
   ```bash
   sudo apt update
   sudo apt install jenkins
   sudo apt install fontconfig openjdk-17-jre  # if Java isn’t installed
   sudo systemctl start jenkins
   sudo systemctl status jenkins
   ```
   - **Explanation**: This installs and starts Jenkins.

2. **Access Jenkins**:
   - Open a browser and go to `http://localhost:8080`.
   - For the initial admin password, use:
     ```bash
     sudo cat /var/lib/jenkins/secrets/initialAdminPassword
     ```
   - Paste the password into Jenkins, and follow the setup instructions to create an admin account.

3. **Set Up a New Jenkins Job**:
   - Click "New Item" and choose "Freestyle Project."
   - Name the job (e.g., `FlaskDockerApp`) and click "OK."
   - Configure the following:
     - **Source Code Management**:
       - Select "Git" and enter your GitHub repository URL.
       - Add credentials if needed.
     - **Build Triggers**:
       - Enable "Build periodically" and enter `* * * * *` to check every minute (or adjust as needed).
     - **Build Steps**:
       - Select "Execute Shell" and add commands to build and run the Docker container:
         ```bash
         docker build -t fapp2 .
         docker run -d -p 5000:5000 fapp2
         ```

4. **Save and Run the Job**:
   - Click "Save" and go to "Build Now" to manually trigger a build.
   - Jenkins will now automatically build and run your Docker container based on changes in your GitHub repository.

---

### Step 4: Configure SSH (Optional for Remote Deployment)

1. **Generate an SSH Key** (if not already generated):
   ```bash
   ssh-keygen
   ```
   - Follow prompts to save the key to the default location (usually `~/.ssh/id_rsa`).

2. **Copy the SSH Key to the Remote Server**:
   ```bash
   ssh-copy-id username@remote_server_ip
   ```
   - **Explanation**: This enables passwordless SSH access to the remote server, which can be used in Jenkins or scripts for deployment.

3. **Verify SSH Access**:
   ```bash
   ssh username@remote_server_ip
   ```
   - This should log you into the remote server without prompting for a password.

---

### Summary of Files Created Manually vs. Automatically

1. **Manual Files**:
   - `app.py`: Defines the Flask application.
   - `requirements.txt`: Lists dependencies.
   - `Dockerfile`: Specifies the Docker image setup.
   - **Jenkins Job** (via Jenkins UI): Configures automation steps.

2. **Automatically Created**:
   - Docker Image (`fapp2`) created by `docker build` command.
   - Docker Container (from `docker run` command).
   - Jenkins logs and build files (created by Jenkins during each build).

By following these steps, you’ll have a Flask app running in Docker, managed by Jenkins for continuous integration, and ready for optional deployment via SSH to a remote server.