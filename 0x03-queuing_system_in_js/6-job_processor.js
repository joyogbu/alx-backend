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
async function sendNotification(phoneNumber, message) {
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};
queue.process('push_notification_code', function(job, done) {
	sendNotification(job.data.phoneNumber, job.data.message, done);
});
