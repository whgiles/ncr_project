rm -r ./venv & wait
python3 -m venv ./venv & wait
source venv/bin/activate

pip3 install -r ./requirements.txt & wait

docker rm -f $(docker ps -a)
docker build -t ncr_image1 ./db/.


docker run -dp 5432:5432 --name ncr_container1 ncr_image1

python3 ./quick_insert.py & wait

export FLASK_APP=server
flask run
