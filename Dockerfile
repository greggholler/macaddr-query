FROM python:slim

ADD requirements.txt /
RUN pip3 install -r /requirements.txt

ADD mac-address-looker-upper.py /

ENTRYPOINT [ "python3", "mac-address-looker-upper.py" ]

