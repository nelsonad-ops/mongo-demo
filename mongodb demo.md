mongodb demo.md

*Setup your k8s cluster for testing*<br>
git clone https://github.com/andrewh1978/px-deploy.git<br>
px-deploy create -n mongodemo -t px<br>
<br>
*Prep your local environment. The following instructions are for CentOS/RHEL-based environments*<br>
git clone https://github.com/nelsonad-ops/px-mongo-demo.git<br>
yum install python3 -y<br>
yum install python3-pip -y<br>
vi /etc/yum.repos.d/mongodb-org-6.0.repo<br>
~<br>
[mongodb-org-6.0]<br>
name=MongoDB Repository<br>
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/6.0/$basearch/<br>
gpgcheck=1<br>
enabled=1<br>
gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc<br>
~<br>
sudo yum install -y mongodb-mongosh<br>
<br>
*Customizations to apply*<br>
Your local ip address or hostname and whether it is available via nodeport/loadbalancer in services<br>
Number of test data records to generate in mongodb.py<br>
<br>
*Prep your k8s environment*<br>
cd px-mongo-demo<br>
kubectl create ns mongo<br>
kubectl apply -f k8s-setup/ -n mongo<br>
<br>
*Validate MongoDB is up and running*<br>
kubectl exec -it mongodb-replica-0 -n mongo -- mongo<br>
rs.initiate()<br>
<br>
*Validate with local mongo shell*<br>
mongosh "mongodb://your.ip.address.here:32000"<br>
show dbs<br>
<br>
*Prep your python runtime environment*<br>
cd datagen<br>
pip3 install -r requirements.txt<br>
python3 mongodb.py<br>
<br>
*Validate data available*<br>
mongosh "mongodb://your.ip.address.here:32000"<br>
-or-
mongosh "mongodb://192.168.101.101:32000/?readPreference=secondary"<br>
show dbs<br>
use company<br>
show collections<br>
db.employees.find()<br>
