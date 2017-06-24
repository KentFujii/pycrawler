FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y wget libfontconfig
RUN mkdir -p /home/root/src && cd $_
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN tar jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN cd phantomjs-2.1.1-linux-x86_64/bin/ && cp phantomjs /usr/local/bin/
RUN apt-get install -y fonts-migmix
RUN echo '<?xml version="1.0"?>\n\
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">\n\
<fontconfig>\n\
  <match target="pattern">\n\
    <test qual="any" name="family">\n\
      <string>serif</string>\n\
    </test>\n\
    <edit name="family" mode="assign" binding="string">\n\
      <string>MigMix 2P</string>\n\
    </edit>\n\
  </match>\n\
</fontconfig>\n'\
>> /etc/fonts/local.conf
RUN mkdir /myapp
WORKDIR /myapp
ADD . /myapp
RUN pip3 install -r requirements.txt
