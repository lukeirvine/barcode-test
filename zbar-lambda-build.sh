#!/bin/bash

# Clear out old images
[ -d "lib" ] && rm -r lib

cat <<EOF > tmp_recipe.sh
# This is the actual container-side recipe
yum groupinstall -y "Development Tools"
cd /root
git clone https://github.com/mchehab/zbar.git
cd zbar
autoreconf -vfi
./configure --prefix=/usr --without-xshm --without-xv --without-jpeg --without-imagemagick --without-gtk --without-python --without-qt --disable-video
make
mkdir -p /build/lib
cp -a zbar/.libs/libzbar.so* /build/lib
EOF

# Run the recipe in an Amazon Linux 2 container
docker run --rm -it -v $(pwd):/build amazonlinux:2 bash /build/tmp_recipe.sh
rm tmp_recipe.sh
