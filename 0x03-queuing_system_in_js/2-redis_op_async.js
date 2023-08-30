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
//set a key-value pair
function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}
const displaySchool = util.promisify(client.get).bind(client);
async function displaySchoolValue (schoolName) {
	try {
		const value = await displaySchool(schoolName);
		console.log(value);
	} catch(err) {
		console.log(err);
	}
}

displaySchoolValue('Holberton').then(() => {
	setNewSchool('HolbertonSanFrancisco', '100');
	displaySchoolValue('HolbertonSanFrancisco');
})
