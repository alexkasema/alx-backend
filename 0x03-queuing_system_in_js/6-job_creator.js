import { createQueue } from 'kue';

const queue = createQueue();

const queueName = 'push_notification_code';

const jobFormat = {
  phoneNumber: '1234567890',
  message: 'Task has been created',
}

const job = queue.create(queueName, jobFormat).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`)
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
