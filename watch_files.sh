#!/bin/sh

FILES="lettermatrix.py test.py"


while true; do
  change=$(inotifywait -e close_write,moved_to,create .)
  change=${change#./ * }
  if [[ $FILES =~ $change ]]; then nosetests-2.7 test.py; fi
done
