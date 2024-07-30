const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array')

  const queueName = 'push_notification_code_3';

  for (const jobFormat of jobs ) {
    const job = queue.create(queueName, jobFormat);

    job.save((err) => {
      if (!err) console.log(`Notification job created: ${job.id}`);
    });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err.message}`);
    });

    job.on('progress', (progress) => {
      console.log(
        `Notification job ${job.id} ${progress}% complete`
      );
    });
  }
}

export default createPushNotificationsJobs;
