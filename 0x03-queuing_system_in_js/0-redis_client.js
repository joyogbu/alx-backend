//const redis = require('redis')
import { createClient } from 'redis';
const client = createClient();
//(async () => { 
 //await redisclient.connect()
//})();
//redisclient.on('ready', () => {
	//console.log("Redis client connected to the server")
//})
client.on('error', (err) => {
	console.log("Redis client not connected to the server", err)
});
client.on('connect', () => {
	console.log('Redis client connected to the server');
});
