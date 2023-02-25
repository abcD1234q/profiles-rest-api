FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file to the container
# COPY requirements.txt .

# # Install the dependencies
# RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set the entrypoint of the container
ENTRYPOINT [ "python" ]

# Set the default command to run when the container starts
CMD [ "python helloworld.py" ]