//import required package
import redis from 'redis';
import util from 'util'
const express = require('express');
const kue = require('kue');
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
function reserveSeat(number) {
	client.set('available_seats', number);
}
const getCurrentAvail = util.promisify(client.get).bind(client)
async function getCurrentAvailableSeats() {
	try {
		const seats = await getCurrentAvail('available_seats');
	} catch(error) {
		console.log(error);
	}
}
let reservationEnabled = true;
const queue = kue.createQueue();
const app = express();
const port = 1245;
app.listen(port, () => {
	reserveSeat('available_seat', 50);
	console.log(`Express started on ${port}`);
});
app.get('/available_seats', async function(requeat, response) {
	const noOfSeats = await getCurrentAvailableSeats();
	return response.json(`{numberOfAvailableSeats: ${noOfSeats}}`);
});
const objData = {available_seats: 1}
app.get('/reserve_seat', function (request, response) {
	if (reservationEnabled == false) {
		response.send({"status": "Reservation are blocked" });
	}

	const job = queue.create('reserve_seat', objData).save( function(err) {
		if (err) {
			response.send({"status": "Reservation failed"})
		} else {
			response.send({ "status": "Reservation in process" })
		}
	});
	job.on('complete', function(result) {
		console.log(`Seat reservation job ${job.id} completed`);
	})
	job.on('failed', function(err) {
		console.log(`Seat reservation job ${job.id} failed: err`);
	});
});
app.get('/process', function(request, response) {
	response.send({status: "Queue processing"})
	queue.process('reserve_seat', async function(job, done) {
		const currentSeats = getCurrentAvailableSeats()
		reserveSeat('available_seats', currentSeats - job.available_seats);
		if ((currentSeats - job.available_seats) == 0) {
			reservationEnabled = false;
		}
		if (!(currentSeats - job.available_seats) >= 0) {
			throw new Error('Not enough seats available')
		}
	});
});
