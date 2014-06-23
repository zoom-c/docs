#!/bin/sh

SUBDIRS="slips trezor-devel trezor-faq trezor-user"

rm -rf _build/
mkdir _build

cp index.html _build/

for i in $SUBDIRS; do
  mkdir _build/$i/
  cd $i
  make html
  mv _build/html/* ../_build/$i/
  rm -rf _build/
  cd ..
done
