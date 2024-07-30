import { createQueue } from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 2345 to verify your account'
  }
];

describe('createPushNotificationsJobs', () => {
  const queue = createQueue();

  before(() => {
    queue.testMode.enter(true);
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('Display an error message if jobs is not an array', () => {
    expect(() => {
      createPushNotificationsJobs('Hello', queue);
    }).to.throw('Jobs is not an array');
  });

  it('Should not display an error in the case of an empty array', () => {
    const res = createPushNotificationsJobs([], queue);
    expect(res).to.equal(undefined);
  });

  it('Should create two new jobs and add to queue:', () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');

    expect(queue.testMode.jobs[0].data).to.eql({
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    });
  });
});
