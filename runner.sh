if [ ! -d "./venv" ]; then
    echo "Creating python virtual env..."
    python3 -m venv venv
    echo "*/" > ./venv/.gitignore

    ./venv/bin/pip install -r ./requirements.txt
fi

echo "Running App..."
./venv/bin/python3 ./src/main.py