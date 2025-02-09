FROM python:3.9-slim

     # Install dependencies
     RUN apt-get update && apt-get install -y ffmpeg

     # Install Python packages
     COPY requirements.txt .
     RUN pip install --upgrade pip && pip install -r requirements.txt

     # Copy app files
     COPY . .

     # Expose port
     EXPOSE 5000

     # Run the app
     CMD ["./start.sh"]
