//import required package
import redis from 'redis';
import util from 'util'
//create a redis client
const client = redis.createClient();
//listen for errors
client.on('error', (err) => {
console.log("Redis client not connected to the server", err)
});
//connect to the redis server
client.on('ready', () => {
	console.log('Redis client connected to the server');
});
const kue = require('kue');
const queue = kue.createQueue();
const createPushNotificationsJobs = function createPushNotificationsJobs(jobs, queue) {
	if (jobs.constructor !== Array) {
		throw new Error('Jobs is not an array');
	}
	for (const myJob of jobs) {
		const job = queue.create('push_notification_code_3', myJob).save( function(err) {
			if (err) {
			  console.log(err);
			} else {
			  console.log(`Notification job created: ${job.id}`);
			}
		});
	
	job.on('complete', function(result) {
		console.log('Notification job completed');
	})
	job.on('failed', function(err) {
		console.log('Notification job failed');
	});
	job.on('progress', function(progress, data) {
		console.log(`Notification job ${job.id} ${progress} complete`);
	});
	}
}
module.exports = createPushNotificationsJobs;
