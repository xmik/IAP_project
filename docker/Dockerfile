FROM python:3.7.2

RUN pip3.7 install django djangorestframework psycopg2 psycopg2-binary requests

COPY src /usr/src/app
COPY run.sh /usr/bin/iap-hq-backend-run.sh
RUN chmod +x /usr/bin/iap-hq-backend-run.sh

ENTRYPOINT ["bash"]
EXPOSE 8000
CMD ["-c", "iap-hq-backend-run.sh"]
