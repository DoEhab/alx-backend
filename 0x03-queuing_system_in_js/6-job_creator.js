const kue = require('kue');

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a test notification',
};

const job = queue
  .create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
      sendNotification(jobData.phoneNumber, jobData.message);
    } else {
      console.error('Job creation failed:', err);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (errorMessage) => {
  console.log('Notification job failed');
});

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
