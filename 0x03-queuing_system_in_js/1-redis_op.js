import pkg from 'redis';
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

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, response) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(`Reply: ${response}` );
  });
}

displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
