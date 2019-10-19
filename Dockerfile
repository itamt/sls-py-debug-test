FROM python:3.7

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs

RUN npm install -g serverless

RUN pip install \
  pipenv \
  awscli \
  boto3 \
  pydevd

# aws credentials
RUN sls config credentials --provider aws --key $AWS_ACCESS_KEY_ID --secret $AWS_SECRET_ACCESS_KEY

# plugins
COPY ./serverless.yml /app/
WORKDIR /app
RUN sls plugin install --name serverless-python-requirements \
  && sls plugin install --name serverless-offline
