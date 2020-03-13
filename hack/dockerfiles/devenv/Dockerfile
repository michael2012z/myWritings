FROM ubuntu:18.04

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV VNC_COL_DEPTH 24
ENV VNC_RESOLUTION 1280x1024
ENV VNC_PW vncpassword

RUN apt-get install -qy curl wget build-essential
RUN apt-get install -qy xfce4 xfce4-goodies tightvncserver twm expect
RUN apt-get install -qy emacs cscope xcscope-el
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN echo 'source $HOME/.cargo/env' >> $HOME/.bashrc

RUN apt-get install -qy firefox
RUN apt-get install -qy git meld tree

RUN curl https://raw.githubusercontent.com/michael2012z/myWritings/master/hack/dockerfiles/devenv/files/_bash_aliases -o /root/.bash_aliases
RUN curl https://raw.githubusercontent.com/michael2012z/myWritings/master/hack/dockerfiles/devenv/files/_bashrc_ext >> /root/.bashrc
RUN curl https://raw.githubusercontent.com/michael2012z/myWritings/master/hack/dockerfiles/devenv/files/_emacs -o /root/.emacs
RUN curl https://raw.githubusercontent.com/michael2012z/myWritings/master/hack/dockerfiles/devenv/files/_gitconfig -o /root/.gitconfig
RUN mkdir /root/.vnc && curl https://raw.githubusercontent.com/michael2012z/myWritings/master/hack/dockerfiles/devenv/files/_vnc_xstartup -o /root/.vnc/xstartup && chmod +x /root/.vnc/xstartup
RUN curl https://raw.githubusercontent.com/michael2012z/myWritings/master/hack/dockerfiles/devenv/files/_emacs_d.tar.gz -o /root/_emacs_d.tar.gz && cd /root && tar zxvf _emacs_d.tar.gz && rm -f _emacs_d.tar.gz
RUN curl https://raw.githubusercontent.com/michael2012z/myWritings/master/hack/dockerfiles/devenv/files/startvnc.sh -o /root/startvnc.sh && chmod +x /root/startvnc.sh
RUN mkdir /root/.ssh && curl https://raw.githubusercontent.com/michael2012z/myWritings/master/config/_ssh/id_rsa.txt -o /root/.ssh/id_rsa && chmod 400 /root/.ssh/id_rsa && curl https://raw.githubusercontent.com/michael2012z/myWritings/master/config/_ssh/id_rsa.pub.txt -o /root/.ssh/id_rsa.pub && chmod 444 /root/.ssh/id_rsa.pub
RUN curl https://raw.githubusercontent.com/michael2012z/myWritings/master/hack/dockerfiles/devenv/files/install_go.sh -o /root/install_go.sh && chmod +x /root/install_go.sh && /root/install_go.sh


ENTRYPOINT ["/root/startvnc.sh"]
