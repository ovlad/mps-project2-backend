'use strict';

const express = require('express');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const _ = require('lodash');

// load env file
require('dotenv').config();

const Service = require('./service');

const service = new Service();
const app = express();
const PORT = 7000;

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json({limit: '10mb'}));

// request middleware token verification
function verifyToken(req, res, next) {
    const bearerHeader = req.headers['authorization'];

    if (_.isUndefined(bearerHeader)) {
        res.sendStatus(401);
    } else {
        const token = bearerHeader.split(' ')[1];

        jwt.verify(token, process.env.JWT_SECRET, error => {
            if (error) {
                res.sendStatus(401);
                console.log(error);
            } else {
                next();
            }
        });
    }
}

// app.get('/', (req, res) => res.sendStatus(405));
// app.get('/', (req, res) => res.send("Hello World! This is a greeting from the NodeJS API!"));

// POST /login
app.post('/login', (req, res) => {
    const body = req.body || {};

    // get params from body
    const email = body.email;
    const password = body.password;

    // take username information from db
    // ...
    const user = {
        email,
        password
    };

    jwt.sign({user}, process.env.JWT_SECRET, (error, token) => {
        if (error) {
            res.sendStatus(401);
            console.log(error);
        } else {
            res.json({
                token
            });
        }
    });
});

// POST /refresh
app.post('/refresh', (req, res) => {
    const body = req.body || {};

    // get params from body
    const token = body.token;

    jwt.verify(token, process.env.JWT_SECRET, (error, data) => {
        if (error) {
            res.sendStatus(401);
            console.log(error);
        } else {
            jwt.sign({user: data.user}, process.env.JWT_SECRET, (error, token) => {
                if (error) {
                    res.sendStatus(401);
                    console.log(error);
                } else {
                    res.json({
                        token
                    });
                }
            });
        }
    });
});

// POST /register
app.post('/register', verifyToken, (req, res) => {
    const body = req.body || {};

    service.register(body, (error, response) => {
        if (error) {
            res.json({error});
        } else {
            res.json(response)
        }
    });
});

// PUT /updateStatus
app.put('/updateStatus', verifyToken, (req, res) => {
    const body = req.body || {};

    service.updateStatus(body, (error, response) => {
        if (error) {
            res.json({error});
        } else {
            res.json(response)
        }
    });
});

// GET /donor
app.get('/donor', verifyToken, (req, res) => {
    const body = req.body || {};

    service.getDonors(body, (error, response) => {
        if (error) {
            res.json({error});
        } else {
            res.json(response)
        }
    });
});

// GET /donor/{donorId}
app.get('/donor/:donorId', verifyToken, (req, res) => {
    const body = {
        donorId: req.params.donorId
    };

    service.getDonor(body, (error, response) => {
        if (error) {
            res.json({error});
        } else {
            res.json(response)
        }
    });
});

// DELETE /donor/{donorId}
app.delete('/donor/:donorId', verifyToken, (req, res) => {
    const body = {
        donorId: req.params.donorId
    };

    service.deleteDonor(body, (error, response) => {
        if (error) {
            res.json({error});
        } else {
            res.json(response)
        }
    });
});

// GET /doctor
app.get('/doctor', verifyToken, (req, res) => {
    const body = req.body || {};

    service.getDoctors(body, (error, response) => {
        if (error) {
            res.json({error});
        } else {
            res.json(response)
        }
    });
});


// GET /doctor/{doctorId}
app.get('/doctor/:doctorId', verifyToken, (req, res) => {
    const body = {
        doctorId: req.params.doctorId
    };

    service.getDoctor(body, (error, response) => {
        if (error) {
            res.json({error});
        } else {
            res.json(response)
        }
    });
});

// DELETE /doctor/{doctorId}
app.delete('/doctor/:doctorId', verifyToken, (req, res) => {
    const body = {
        doctorId: req.params.doctorId
    };

    service.deleteDoctor(body, (error, response) => {
        if (error) {
            res.json({error});
        } else {
            res.json(response)
        }
    });
});

app.listen(PORT, () => console.log(`Example app listening on port ${PORT}!`));
