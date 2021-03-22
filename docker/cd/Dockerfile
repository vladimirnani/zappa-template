FROM lambci/lambda:build-python3.8

ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python -m venv $VIRTUAL_ENV
RUN pip install --upgrade pip
RUN pip install awscli

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . ./var/task

WORKDIR /var/task