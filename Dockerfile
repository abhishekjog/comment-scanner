FROM debian:stretch-slim
RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
  curl \
  wget \
  git \
  build-essential \
  zip \
  jq \
  ca-certificates \
  bash
  
ADD main.sh /main.sh
RUN ["chmod", "+x", "/main.sh"]
ENTRYPOINT ["/main.sh"]
