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
client.on('connect', () => {
	console.log('Redis client connected to the server');
});
const channel = 'holberton school channel';
client.subscribe(channel);
client.on('message', (channel, message) => {
	if (message === 'KILL_SERVER') {
		client.unsubscribe();
		client.quit();
	}
	console.log(message);
});
