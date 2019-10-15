FROM python:3.6.4
ENV PYTHONUNBUFFERED 1
RUN sed -i '/jessie-updates/d' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install nano -y
RUN mkdir /apisocket/
ADD / Dog-Breed-Classification-DRF-API/
WORKDIR /Dog-Breed-Classification-DRF-API
RUN pip install -r requirements.txt
RUN chmod +x startServer.sh
RUN chmod 777 startServer.sh
EXPOSE 8000
CMD ["./startServer.sh"]
