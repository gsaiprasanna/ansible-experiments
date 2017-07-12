import boto
import boto.ec2
import dateutil
from boto import ec2
from dateutil import parser
from datetime import timedelta, datetime
import datetime
 
connection=ec2.connect_to_region("us-east-1")
snapshot_filter = {
            "tag:expire": "True"
        } 
snapshots = connection.get_all_snapshots(filters=snapshot_filter)
deleteTime=datetime.datetime.now() - datetime.timedelta(days=5)  
 
for snapshot in snapshots:
     
    if parser.parse(snapshot.start_time).date() <= deleteTime.date():
        print " Deleting the snapshot %s  %s "  %(snapshot.id,snapshot.tags)
        connection.delete_snapshot(snapshot.id) 
    else:
        print "Sorry, we cannot delete snapshots based on \"tag:expire\" which are not older than 5 days"
