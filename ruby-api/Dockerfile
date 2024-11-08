FROM       ruby:2.6
LABEL      maintainer="Sawood Alam <@ibnesayeed>"

ENV        LANG C.UTF-8
ENV        REDIS_URL="redis://localhost:6379"

WORKDIR    /app
COPY       Gemfile /app/
RUN        bundle install

COPY       linkextractor.rb /app/
RUN        chmod a+x linkextractor.rb

COPY       entrypoint.sh /app/
RUN        chmod +x /app/entrypoint.sh


ENTRYPOINT ["/app/entrypoint.sh"]
CMD        ["./linkextractor.rb", "-o", "0.0.0.0"]
