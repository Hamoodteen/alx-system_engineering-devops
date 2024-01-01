<h1>1-distributed_web_infrastructure</h1><hr>

<ol>
<ui> <h3> first question : </h3>
<li> firstable , I've added a copy of database to achieve replication , and to reduce SPOF . </li>
<li> I've configured load balancer to work with the least connection algorithm , finding the server that don't have a lot of connestions to be suitable . </li>
<li> working with active-passive setup , it works only with one server , the another in stand-by mode , and retieving from the primary database . </li>
<li> it copies the original database to another and use it when needed , and update it every time </li>
<li> the primary database handles writing operations and the replica handles reading and restore if the first fails or beeing updated . </li>
</ui>
<ui> <h3> second question : </h3>
<li> SPOF is in the load balancer , it just one taking from all hosts (if it failes , all requests will fail and gives error responce) . </li>
<li>
<ul> - because of no firewall , no rules to control traffic , it may be robot or malicious to attack website </ul>
<ul> - no HTTPS , no ssl or certicicate , foobar.com may be malicious website to attack host with malwares , or being unknow website </ul>
</li>

</ui>
</ol>