#!/bin/sh

if [ "$USE_CACHE" = "true" ]; then
  echo "Cache está ativo"
else
  echo "Cache não está ativo"
fi

# Execute o comando original do container
exec "$@"