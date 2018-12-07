FROM python:2.7.15-alpine3.8

# create and set the current directory
WORKDIR /data/mps

# copy all the project
COPY . .

# import dumb_init
ADD ./dumb-init_1.2.1_amd64 /usr/local/bin/dumb-init
RUN chmod +x /usr/local/bin/dumb-init

# install python modules
RUN pip install -r requirements.txt

# create group 'mps and user 'mps' && change owner of the project
RUN addgroup mps && \
    adduser -D -G mps mps && \
    chown -R mps:mps /data/mps

# sets command prompt look
ENV PS1="\[\e[0;33m\]\u\[\e[0;36m\]@\[\e[0;36m\]\h \[\e[0;37m\]\w \[\e[0;33m\]$ \[\e[0m\]"

# this does not actually publish the port;
# it only functions as a type of documentation between the person who builds the image
# and the person who runs the container
EXPOSE 7000

# changes user to mps
USER mps

# start the server
#CMD dumb-init python src/server.py
CMD ["python", "src/server.py"]
