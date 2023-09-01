const assert = require('assert');
const expect = require('chai').expect;
const kue = require('kue');
import createPushNotificationsJobs from './8-job.js';
const queue = kue.createQueue();
//queue.testMode.enter()
describe('createPushNotificationsJobs', function() {
	before(function() {
		queue.testMode.enter();
	});
	afterEach(function() {
		queue.testMode.clear();
	})
	after(function() {
		queue.testMode.exit()
	})
	it('display an error message if job is not an array', function() {
		const data = "test string"
		assert.throws(() => createPushNotificationsJobs(data, queue), Error, 'Jobs is not an array');
	});
	it('create two new jobs to the queue', async function () {
		const data2 = [{phoneNumber: '5253513880', message: 'This is the code 1460 to verify your account'}, {phoneNumber: '5253518780', message: 'This is the code 1290 to verify your account'}];
		assert.equal(createPushNotificationsJobs(data2, queue), 'Notification job created:' );
		await createPushNotificationsJobs(data2, queue);
		const jobs = queue.testMode.jobs
		assert.equal(queue.testMode.jobs.length, 2);
	});
});
