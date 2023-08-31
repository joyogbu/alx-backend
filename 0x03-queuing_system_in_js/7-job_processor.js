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
const blacklist = ['4153518780', '4153518781'];
async function sendNotification(phoneNumber, message, job, done) {
	if (phoneNumber in blacklist){
		throw new Error(`Phone number ${phoneNumber} is blacklisted`);
	}
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};
queue.process('push_notification_code_2', 2, function(job, done) {
	sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

