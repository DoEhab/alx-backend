import pkg from 'redis';
import { promisify } from 'util';

const { createClient, print } = pkg;
const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.connect();

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}
const asyncGet = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const response = await asyncGet(schoolName);
    console.log(`Reply: ${response}`);
  } catch (err) {
    console.log(err);
  }
}

await displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
