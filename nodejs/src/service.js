'use strict';

const waterfall = require('async/waterfall');
const _ = require('lodash');

const models = require('./../database/models');

class Service {
    constructor() {}

    register(body, callback) {
        const params = _.pick(body, ['name', 'surname', 'email', 'password', 'passwordConfirm', 'role', 'bloodType', 'rh', 'hospitalId', 'transfusionCenterId']);

        waterfall([
            // validate params
            next => {
                if (_.isUndefined(params.name)) {
                    callback({ message: 'Missing `name` param.' });
                }

                if (_.isUndefined(params.surname)) {
                    callback({ message: 'Missing `surname` param.' });
                }

                if (_.isUndefined(params.email)) {
                    callback({ message: 'Missing `email` param.' });
                }

                if (_.isUndefined(params.password)) {
                    callback({ message: 'Missing `password` param.' });

                }

                if (_.isUndefined(params.passwordConfirm)) {
                    callback({ message: 'Missing `passwordConfirm` param.' });
                }

                if (_.isUndefined(params.role)) {
                    callback({ message: 'Missing `role` param.' });
                }

                if (!_.isString(params.name) || !params.name.length) {
                    callback({ message: 'Invalid `name` param.' });
                }

                if (!_.isString(params.surname) || !params.surname.length) {
                    callback({ message: 'Invalid `surname` param.' });
                }

                if (!_.isString(params.email) || !params.email.length) {
                    callback({ message: 'Invalid `email` param.' });
                }

                if (!_.isString(params.password) || !params.password.length) {
                    callback({ message: 'Invalid `password` param.' });
                }

                if (!_.isString(params.passwordConfirm) || !params.passwordConfirm.length) {
                    callback({ message: 'Invalid `passwordConfirm` param.' });
                }

                if (!_.isString(params.role) || !params.role.length || !['DONOR', 'EMPLOYEE', 'DOCTOR'].includes(params.role.toUpperCase())) {
                    callback({ message: 'Invalid `role` param.' });
                }

                if (params.passwordConfirm !== params.password) {
                    callback({ message: 'The `passwordConfirm` param value must be identical with the `password` param value' });
                }

                if (params.role.toUpperCase() === 'DONOR') {
                    if (_.isUndefined(params.bloodType)) {
                        callback({ message: 'Missing `bloodType` param.' });
                    }

                    if (_.isUndefined(params.rh)) {
                        callback({ message: 'Missing `rh` param.' });
                    }

                    if (!_.isString(params.bloodType) || !params.bloodType.length || !['0', 'A', 'B', 'AB'].includes(params.bloodType.toUpperCase())) {
                        callback({ message: 'Invalid `bloodType` param.' });
                    }

                    if (!_.isString(params.rh) || !params.rh.length || !['positive', 'negative'].includes(params.rh.toLowerCase())) {
                        callback({ message: 'Invalid `rh` param.' });
                    }
                } else if (params.role.toUpperCase() === 'EMPLOYEE') {
                    if (_.isUndefined(params.transfusionCenterId)) {
                        callback({ message: 'Missing `transfusionCenterId` param.' });
                    }

                    if (!_.isInteger(params.transfusionCenterId)) {
                        callback({ message: 'Invalid `transfusionCenterId` param.' });
                    }
                } else if (params.role.toUpperCase() === 'DOCTOR') {
                    if (_.isUndefined(params.hospitalId)) {
                        callback({ message: 'Missing `hospitalId` param.' });
                    }

                    if (!_.isInteger(params.hospitalId)) {
                        callback({ message: 'Invalid `hospitalId` param.' });
                    }
                }

                next();
            },

            // add the new user into the database
            () => {
                if (params.role === 'DONOR') {
                    models.donor
                        .create({
                            'name': params.name,
                            'surname': params.surname,
                            'mail': params.email,
                            'password': params.password,
                            'blood_type': params.bloodType,
                            'Rh': params.rh
                        })
                        .then(record => {
                            console.log(record);
                            callback(null, { id_donor: record.id_donor });

                            return null;
                        })
                        .catch(error => {
                            callback({ error });
                        })
                } else if (params.role === 'DOCTOR') {
                    models.doctor
                        .create({
                            'name': params.name,
                            'surname': params.surname,
                            'mail': params.email,
                            'password': params.password,
                            'id_hospital': params.hospitalId
                        })
                        .then(record => {
                            callback(null, { id_doctor: record.id_doctor });

                            return null;
                        })
                        .catch(error => {
                            callback({ error });
                        })
                } else if (params.role === 'EMPLOYEE') {
                    models.employee
                        .create({
                            'name': params.name,
                            'surname': params.surname,
                            'mail': params.email,
                            'password': params.password,
                            'id_center': params.transfusionCenterId
                        })
                        .then(record => {
                            callback(null, { id_employee: record.id_employee });

                            return null;
                        })
                        .catch(error => {
                            callback({ error });
                        })
                }
            }
        ])
    }

    bla(body, callback) {
        callback(null, "Bla from the NodeJS API!");
    }
}

module.exports = Service;
