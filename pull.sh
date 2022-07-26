
if [ -d "test" ]; then
  cd test
  git pull
else
  git clone https://github.com/test/test
  cd test
fi

make clean
make