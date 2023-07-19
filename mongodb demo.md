mongodb demo.md

*Setup your k8s cluster for testing*
git clone https://github.com/andrewh1978/px-deploy.git
px-deploy create -n mongodemo -t px

*Prep your local environment. The following instructions are for CentOS/RHEL-based environments*
git clone https://github.com/nelsonad-ops/px-mongo-demo.git
yum install python3 -y
yum install python3-pip -y
vi /etc/yum.repos.d/mongodb-org-6.0.repo
~
[mongodb-org-6.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/6.0/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc
~
sudo yum install -y mongodb-mongosh

*Customizations to apply*
Your local ip address or hostname and whether it is available via nodeport/loadbalancer in services
Number of test data records to generate in mongodb.py

*Prep your k8s environment*
cd px-mongo-demo
kubectl create ns mongo
kubectl apply -f k8s-setup/ -n mongo

*Validate MongoDB is up and running*
kubectl exec -it mongodb-replica-0 -n mongo -- mongo

*Validate with local mongo shell*
mongosh "mongodb://your.ip.address.here:32000"
show dbs

*Prep your python runtime environment*
cd datagen
pip3 install -r requirements.txt
python3 mongodb.py

*Validate data available*
mongosh "mongodb://your.ip.address.here:32000"
show dbs
use company
show collections
db.employees.find()
