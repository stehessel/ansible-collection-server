#!/usr/bin/env bash

set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes

/usr/bin/docker container stop mealie-api
/usr/bin/docker cp mealie-api:/app/data {{ mealie__path }}/backup
/usr/bin/docker container start mealie-api
