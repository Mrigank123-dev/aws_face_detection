# Commands for AWS:

1. Login server:
    ```powershell
    ssh -i face_server_new_key.pem ubuntu@<ip_address>
    ```

1. Project Clone:
    ```bash
    git clone https://github.com/Mrigank123-dev/aws_face_detection.git
    ```

1. Create Virtual Environment, Activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

1. Update pip and install dependencies:
    ```bash
    pip install -U pip
    pip install -r requirements.txt
    ```

1. If any changes made in code:
    - Laptop: github extension
    - Laptop: `+` to add all the files
    - Laptop: Type commit message and press `Commit`
    - Laptop: Press `push` button
    - AWS:
        ```bash
        ssh -i face_server_new_key.pem ubuntu@<ip_address>
        ```
    - AWS server:
        ```bash
        cd aws_face_detection
        source venv/bin/activate
        git pull
        ```
    - Run the app:
        ```bash
        flask run --host 0.0.0.0
        ```
    - Check in browser:
        ```
        https://<ip_address>:5000
        ```

