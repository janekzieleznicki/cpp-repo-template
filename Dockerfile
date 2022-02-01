FROM docker.io/clearlinux as builder

RUN swupd bundle-add os-core-search c-basic python3-basic && pip install conan

WORKDIR /tmp
COPY . .

RUN \
    conan create . docker/deploy --build=missing --profile .gcc-profile && \
    conan install Template/0.0.1@docker/deploy -g deploy --install-folder /tmp/install --build=missing --profile .gcc-profile


FROM docker.io/clearlinux

COPY --from=builder /usr/bin/Template /usr/bin/

CMD Template