import { createQueue } from 'kue';

const queue = createQueue();

const queueName = 'push_notification_code';

const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
}

queue.process(queueName, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});
