rm -r ../venv
python3 -m venv ../venv
source ../venv/bin/active

pip3 install -r ../requirements.txt

docker rm -f $(docker ps -a)
docker build -t ncr_image1 ../db/.
docker run -dp 5432:5432 --name ncr_container1 ncr_image1

python3 ../src/quick_insert.py
cd ..
export FLASK_APP=server
flask run
