import express from 'express';
import { createClient } from 'redis';
import { createQueue } from 'kue';
import { promisify } from 'util';

const client = createClient();
const getAsyncFunc = promisify(client.get).bind(client);

let reservationEnabled;

const reserveSeat = (number) => {
  client.set('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
  const availableSeats = getAsyncFunc('available_seats');
  return availableSeats;
};

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
  reserveSeat(50);
  reservationEnabled = true;
});

// kue
const queue = createQueue();
const queueName = 'reserve_seat';

// express
const app = express();
const PORT = 1245;

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  return res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (reservationEnabled === false) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const jobFormat = {};

  const job = queue.create(queueName, jobFormat).save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

app.get('/process', async (req, res) => {
  queue.process(queueName, async (job, done) => {
    let availableSeats = await getCurrentAvailableSeats();

    if (availableSeats <= 0) {
      done(Error('Not enough seats available'));
    }

    availableSeats = Number(availableSeats) - 1;

    reserveSeat(availableSeats);

    if (availableSeats <= 0) {
      reservationEnabled = false;
    }

    done();
  });

  res.json({ status: 'Queue processing' });
});

app.listen(PORT, () => {
  console.log(`App listening on port: ${PORT}`);
});
