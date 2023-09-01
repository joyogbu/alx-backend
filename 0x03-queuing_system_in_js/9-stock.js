const express = require('express');
import redis from 'redis'
const listProducts = [{Id: 1, name: 'Suitcase 250', price: 50, stock: 4}, {Id: 2, name: 'Suitcase 450', price: 100, stock: 10}, {Id: 3, name: 'Suitcase 650', price: 350, stock: 2}, {Id: 4, name: 'Suitcase 1050', price: 550, stock: 5}];
function getItemById(id) {
	for (const prods of listProducts) {
		if (prods.Id == id) {
			return prods;
		}
	}
}
const server = express()
const port = 1245;
const client = redis.createClient();
server.get('/list_products', (request, response) => {
	response.json(listProducts)
})
server.get('/test/:id', (request, response) => {
        const items = getItemById(request.params.id)
        response.send(items);
});
function reserveStockById(itemId, stock) {
	//myItem = getItemById(itemId);
	client.set(itemId, stock);
}
async function getCurrentReservedStockById(itemId) {
	await client.get(itemId, function(err, reply) {
		return reply;
	});
}
server.get('/list_products/:itemId', function(request, response) {
	//if (!request.params.itemId) {
	const prod = client.get(request.params.id, (err, reply) => {
		if (err) {
			return response.send({status: 'Product not found'});
		}
	});

	/*client.exists(request.params.id, function(err, reply) {
		if (reply == 0) {
			return response.send({status: 'Product not found'});
		}
	});*/
	const stockId = request.params.itemId;
	const myItem = getItemById(stockId);
	const availableStock = getCurrentReservedStockById(stockId);
	response.send({itemId: stockId, itemName: myItem.name, price: myItem.price, initialAvailableQuantity: myItem.stock, currentQuantity: availableStock});
	//response.send('list')
});
server.get('/reserve_product/:itemId', function (request, response) {
	//myItem = getProductById(request.params.itemId)
	const item = getCurrentReservedStockById(request.params.itemId)
	if (item.currentQuantity < 1) {
		return response.send({"status":"Not enough stock available","itemId":1});
	}
	else {
		reserveStockById(request.params.itemId, 1)
		return response.send({"status":"Reservation confirmed","itemId":1});
	}
});

server.listen(port, () => {
	console.log(`express on ${port}`);
});
module.exports = server;
