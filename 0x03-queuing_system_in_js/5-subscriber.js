import { createClient } from 'redis';

const client = createClient();

const CHANNEL = 'holberton school channel';
const EXIT_MSG = 'KILL_SERVER';

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.subscribe(CHANNEL);

client.on('message', (channel, message) => {
  if (channel === CHANNEL) console.log(message);

  if (message === EXIT_MSG) {
    client.unsubscribe(CHANNEL);
    client.quit();
  }
});
