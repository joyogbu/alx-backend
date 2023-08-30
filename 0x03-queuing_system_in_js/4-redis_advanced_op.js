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
async function setTheKeys(key, value) {
	await client.hset(key, value, redis.print);
	client.del('HolbertonSchools');
}

setTheKeys("HolbertonSchools", ['Portland', 50])
setTheKeys("HolbertonSchools", ["Seatle", 80])
setTheKeys("HolbertonSchools", ["New York", 20])
setTheKeys("HolbertonSchools", ["Bogota", 20])
setTheKeys("HolbertonSchools", ["Cali", 40])
setTheKeys("HolbertonSchools", ["Paris", 2])
client.hgetall('HolbertonSchools', (err, object) => {
	console.log(object);
});
