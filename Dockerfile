#import python image
FROM python:3.12-slim 

#copy local buiuld into container
WORKDIR /app
COPY /build .

#download dependencies
RUN pip install -r requirements.txt

#explicitely mention exposed port
EXPOSE 12326

#execute
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:12326", "app:app"]