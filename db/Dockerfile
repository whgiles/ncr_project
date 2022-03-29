FROM postgres:13.2

ENV POSTGRES_PASSWORD=ncr
ENV POSTGRES_USER=ncr
ENV POSTGRES_DB=ncr

COPY ./schema/ncr.sql /docker-entrypoint-initdb.d/
EXPOSE 5432