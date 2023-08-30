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
let channel = 'holberton school channel';
async function publishMessage(message, time) {
	await setTimeout(() => {
		console.log(`About to send ${message}`)
		client.publish(channel, message);}, time);
}
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
