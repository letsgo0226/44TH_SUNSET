FROM python:3.12-alpine
WORKDIR /app
COPY one-liner.sh .
ENV PORT=8080
EXPOSE 8080
CMD ["sh","one-liner.sh"]
