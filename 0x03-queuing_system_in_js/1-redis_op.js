//import required package
import redis from 'redis';
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
//set a key-value pair
function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print)
		/*if (error) {
			console.log(error);
		}
		console.log('Key set', reply);*/
	//});
}
function displaySchoolValue(schoolName) {
	client.get(schoolName, (err, reply) => {
		if (err) {
			console.log(err);
		}
		console.log(reply);
	});
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco')
