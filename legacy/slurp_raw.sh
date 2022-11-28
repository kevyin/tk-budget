#!/usr/bin/env bash
set -e
set -u

export SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


#csvfile=$1

#cp ${csvfile} $SCRIPTDIR/new_raws/
RAWS=${SCRIPTDIR}/data/new_raws
mkdir -p ${RAWS}

find $RAWS/*csv -type f | parallel --gnu 'bean-extract ${SCRIPTDIR}/config.py {} > ${SCRIPTDIR}/beans_my/{/.}.beancount'

git add $RAWS ${SCRIPTDIR}/beans_my/
