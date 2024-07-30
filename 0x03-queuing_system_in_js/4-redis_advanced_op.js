import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const KEY = 'HolbertonSchools';

const fields = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];

const values = [50, 80, 20, 20, 40, 2];

fields.forEach((field, index) => {
  client.hset(KEY, field, values[index], print);
});

client.hgetall(KEY, (err, value) => {
  console.log(value);
});
