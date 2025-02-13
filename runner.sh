if [ ! -d "./venv" ]; then
    echo "Creating python virtual env..."
    python3 -m venv venv
    echo "*/" > ./venv/.gitignore

    ./venv/bin/pip install -r ./requirements.txt
fi

echo "Running App..."
<<<<<<< HEAD:runner.sh
./venv/bin/python3 ./src/main.py
=======
./venv/bin/python3 ./src/main.py
>>>>>>> 3618aabe5081547d23560e41155c3aa358e31d74:setup.sh
