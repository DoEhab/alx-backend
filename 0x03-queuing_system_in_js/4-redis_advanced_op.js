import pkg from 'redis';

const { createClient, print } = pkg;

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

await client.connect();

client.hSet('ALX', 'Portland', 50, print);
client.hSet('ALX', 'Seattle', 80, print);
client.hSet('ALX', 'New York', 20, print);
client.hSet('ALX', 'Bogota', 20, print);
client.hSet('ALX', 'Cali', 40, print);
client.hSet('ALX', 'Paris', 2, print);

client.hGetAll('ALX', (err, reply) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('Reply:', reply);
});
