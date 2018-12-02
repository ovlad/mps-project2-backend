'use strict';

const express = require('express');
const app = express();
const port = 7000;

// app.get('/api', (req, res) => res.sendStatus(405));
app.get('/api', (req, res) => res.send("Hello World! This is a greeting from the NodeJS API!"));

app.listen(port, () => console.log(`Example app listening on port ${port}!`));
