import { createClient } from 'redis';

const subscriber = createClient();

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

await subscriber.connect();

await subscriber.subscribe('ALXchannel', async (message) => {
  console.log(message);

  if (message === 'KILL_SERVER') {
    await subscriber.unsubscribe('ALXchannel');
    await subscriber.quit(); // Disconnects the client gracefully
  }
});
