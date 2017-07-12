import sys

import boto.ec2
from datetime import datetime, timedelta
from boto import connect_to_region
try:
	days = int(sys.argv[1])
except IndexError:
	days = 0

delete_time = datetime.now() - timedelta(days=days)

filters = {
	'tag-key': 'expire'
}

print 'Deleting the snapshots older than {days} days'.format(days=days)

ec2 = connect_to_region('us-east-1')

snapshots = ec2.get_all_snapshots(filters=filters)

deletion_counter = 0
size_counter = 0

for snapshot in snapshots:
	start_time = datetime.strptime(
		snapshot.start_time,
		'%Y-%m-%dT%H:%M:%S.000Z'
	)

	if start_time < delete_time:
		print 'Deleting {id}'.format(id=snapshot.id)
		deletion_counter = deletion_counter + 1
		size_counter = size_counter + snapshot.volume_size
		# Just to make sure you're reading!
		snapshot.delete(dry_run=True)

print 'Deleted {number} snapshots totalling {size} GB'.format(
	number=deletion_counter,
	size=size_counter
)