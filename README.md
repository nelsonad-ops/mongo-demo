# px-mongo-demo
*Setup your k8s cluster for testing*<br>
git clone https://github.com/andrewh1978/px-deploy.git<br>
px-deploy create -n mongodemo -t px<br>
<br>
*Prep your local environment. The following instructions are for CentOS/RHEL-based environments*<br>
git clone https://github.com/nelsonad-ops/px-mongo-demo.git<br>
yum install python3 -y<br>
yum install python3-pip -y<br>
vi /etc/yum.repos.d/mongodb-org-6.0.repo<br>
<br>
[mongodb-org-6.0]<br>
name=MongoDB Repository<br>
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/6.0/$basearch/<br>
gpgcheck=1<br>
enabled=1<br>
gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc<br>
<br>
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
kubectl get pods -n mongo -o wide<br>
kubectl exec -it mongodb-replica-0 -n mongo -- mongo<br>
<p>rs.initiate(<br>
&nbsp&nbsp{<br>
&nbsp&nbsp&nbsp&nbsp_id: "rs0",<br>
&nbsp&nbsp&nbsp&nbspversion: 1,<br>
&nbsp&nbsp&nbsp&nbspmembers: [<br>
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp{ _id: 0, host : "replace-with-mongo-replica-0-ip:27017" },<br>
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp{ _id: 1, host : "replace-with-mongo-replica-1-ip:27017" },<br>
&nbsp&nbsp&nbsp&nbsp]<br>
&nbsp&nbsp}<br>
)<br>
</p>
<br>
*Validate with local mongo shell*<br>
mongosh "mongodb://your.ip.address.here:32000"<br>
show dbs<br>
<br>
*Prep your python runtime environment and customize your uri string in base.py*<br>
cd datagen<br>
vi modules/base.py<br>
pip3 install -r requirements.txt<br>
<br>
*Run your data generation script*<br>
python3 mongodb.py<br>
<br>
*Validate data available*<br>
mongosh "mongodb://your.ip.address.here:32000/?replicaSet=rs0"<br>
show dbs<br>
use company<br>
show collections<br>
db.employees.find()<br>
