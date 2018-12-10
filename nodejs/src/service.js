'use strict';

const waterfall = require('async/waterfall');
const _ = require('lodash');

const models = require('./../database/models');

class Service {
    constructor() {}

    login(body, callback) {
        const email = body.email;
        const password = body.password;

        waterfall([
            // check params
            next => {
                if (_.isUndefined(email)) {
                    callback({ message: 'Missing `email` param.' });
                }

                if (_.isUndefined(password)) {
                    callback({ message: 'Missing `password` param.' });
                }

                if (!_.isString(email) || !email.length) {
                    callback({ message: 'Invalid `email` param.' });
                }

                if (!_.isString(password) || !password.length) {
                    callback({ message: 'Invalid `password` param.' });
                }

                next();
            },

            // get user info from database
            next => {
                models.donor
                    .findOne({
                        where: {
                            'mail': email,
                            'password': password
                        }
                    })
                    .then(record => {
                        if (record) {
                            callback(null, {
                                id: record.id_donor,
                                role: 'DONOR',
                                name: record.name,
                                surname: record.surname,
                                email: record.mail,
                                password: record.password
                            });
                        } else {
                            next();
                        }
                    })
                    .catch(error => {
                        callback(error);
                    });
            },

            // get user info from database
            next => {
                models.doctor
                    .findOne({
                        where: {
                            'mail': email,
                            'password': password
                        }
                    })
                    .then(record => {
                        if (record) {
                            callback(null, {
                                id: record.id_doctor,
                                role: 'DOCTOR',
                                name: record.name,
                                surname: record.surname,
                                email: record.mail,
                                password: record.password,
                                isActive: record.is_active
                            });
                        } else {
                            next();
                        }
                    })
                    .catch(error => {
                        callback(error);
                    });
            },

            // get user info from database
            next => {
                models.employee
                    .findOne({
                        where: {
                            'mail': email,
                            'password': password
                        }
                    })
                    .then(record => {
                        if (record) {
                            callback(null, {
                                id: record.id_employee,
                                role: 'EMPLOYEE',
                                name: record.name,
                                surname: record.surname,
                                email: record.mail,
                                password: record.password,
                                isActive: record.is_active
                            });
                        } else {
                            next();
                        }
                    })
                    .catch(error => {
                        callback(error);
                    });
            },

            // get user info from database
            next => {
                models.admin
                    .findOne({
                        where: {
                            'mail': email,
                            'password': password
                        }
                    })
                    .then(record => {
                        if (record) {
                            callback(null, {
                                id: record.id_admin,
                                role: 'ADMIN',
                                name: record.name,
                                surname: record.surname,
                                email: record.mail,
                                password: record.password
                            });
                        } else {
                            next();
                        }
                    })
                    .catch(error => {
                        callback(error);
                    });
            },

            () => {
                callback({ message: 'Invalid email or password. No user found' })
            }
        ]);
    }

    register(body, callback) {
        const params = _.pick(body, ['name', 'surname', 'email', 'password', 'passwordConfirm', 'role', 'bloodType', 'rh', 'hospitalId', 'transfusionCenterId']);

        console.log(params);

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

                    // if (!_.isInteger(params.transfusionCenterId)) {
                    //     callback({ message: 'Invalid `transfusionCenterId` param.' });
                    // }

                    if (!_.isString(params.transfusionCenterId) || !params.transfusionCenterId.length) {
                        callback({ message: 'Invalid `transfusionCenterId` param.' });
                    }
                } else if (params.role.toUpperCase() === 'DOCTOR') {
                    if (_.isUndefined(params.hospitalId)) {
                        callback({ message: 'Missing `hospitalId` param.' });
                    }

                    // if (!_.isInteger(params.hospitalId)) {
                    //     callback({ message: 'Invalid `hospitalId` param.' });
                    // }

                    if (!_.isString(params.hospitalId) || !params.hospitalId.length) {
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
                            callback(null, { id_donor: record.id_donor });

                            return null;
                        })
                        .catch(error => {
                            callback(error);
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
                            callback(error);
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
                            callback(error);
                        })
                }
            }
        ])
    }

    updateStatus(body, callback) {
        const email = body.email;
        const isActive = body.isActive;

        waterfall([
            // check params
            next => {
                if (_.isUndefined(email)) {
                    callback({ message: 'Missing `email` param.' });
                }

                if (_.isUndefined(isActive)) {
                    callback({ message: 'Missing `isActive` param.' });
                }

                if (!_.isString(email) || !email.length) {
                    callback({ message: 'Invalid `email` param.' });
                }

                // if (!_.isBoolean(isActive)) {
                //     callback({ message: 'Invalid `isActive` param.' });
                // }

                if (!_.isString(isActive) || !isActive.length || !['true', 'false'].includes(isActive.toLowerCase())) {
                    callback({ message: 'Invalid `isActive` param.' });
                }

                next();
            },

            // update the doctor status if the email belongs to a doctor
            next => {
                models.doctor
                    .findOne({
                        where: {
                            'mail': email
                        }
                    })
                    .then(record => {
                        if (record) {
                            models.doctor
                                .update({
                                    'is_active': isActive
                                }, {
                                    where: {
                                        'mail': email
                                    }
                                })
                                .then(response => {
                                    if (response[0] === 1) {
                                        callback(null, { updated: true });
                                    } else {
                                        callback({ message: 'No data was updated' });
                                    }

                                    return null;
                                })
                                .catch(error => {
                                    callback(error);
                                });
                        } else {
                            next();
                        }

                        return null;
                    })
                    .catch(error => {
                        callback(error);
                    });
            },

            // update the employee status if the email belongs to a doctor
            next => {
                models.employee
                    .findOne({
                        where: {
                            'mail': email
                        }
                    })
                    .then(record => {
                        if (record) {
                            models.employee
                                .update({
                                    'is_active': isActive
                                },{
                                    fields: ['is_active'],
                                    where: {
                                        'mail': email
                                    }
                                })
                                .then(response => {
                                    if (response[0] === 1) {
                                        callback(null, { updated: true });
                                    } else {
                                        callback({ message: 'No data was updated' });
                                    }

                                    return null;
                                })
                                .catch(error => {
                                    callback(error);
                                });
                        } else {
                            next();
                        }

                        return null;
                    })
                    .catch(error => {
                        callback(error);
                    });
            },

            // callback with error
            () => {
                callback({ message: 'Invalid `email` param. The email does not belong to any doctor or employee' });
            }
        ]);
    }

    getDonors(body, callback) {
        const name = body.name;
        const surname = body.surname;
        const email = body.email;
        const password = body.password;
        const bloodType = body.bloodType;
        const rh = body.rh;

        let where = {};

        waterfall([
            // check params
            next => {
                if (!_.isUndefined(name) && !(_.isString(name) && name.length)) {
                    callback({ message: 'Invalid `name` param.' });
                }

                if (!_.isUndefined(surname) && !(_.isString(surname) && surname.length)) {
                    callback({ message: 'Invalid `surname` param.' });
                }

                if (!_.isUndefined(email) && !(_.isString(email) && email.length)) {
                    callback({ message: 'Invalid `email` param.' });
                }

                if (!_.isUndefined(password) && !(_.isString(password) && password.length)) {
                    callback({ message: 'Invalid `password` param.' });
                }

                if (!_.isUndefined(bloodType) && !(_.isString(bloodType) && bloodType.length && ['0', 'A', 'B', 'AB'].includes(bloodType.toUpperCase()))) {
                    callback({ message: 'Invalid `bloodType` param.' });
                }

                if (!_.isUndefined(rh) && !(_.isString(rh) && rh.length && ['positive', 'negative'].includes(rh.toLowerCase()))) {
                    callback({ message: 'Invalid `rh` param.' });
                }

                next();
            },

            // build where object
            next => {
                if (!_.isUndefined(name)) {
                    where.name = name;
                }

                if (!_.isUndefined(surname)) {
                    where.surname = surname;
                }

                if (!_.isUndefined(email)) {
                    where.mail = email;
                }

                if (!_.isUndefined(password)) {
                    where.password = password;
                }

                if (!_.isUndefined(bloodType)) {
                    where.blood_type = bloodType
                }

                if (!_.isUndefined(rh)) {
                    where.Rh = rh;
                }

                next();
            },

            // get donors
            () => {
                models.donor
                    .findAll({
                        where: where
                    })
                    .then(records => {
                        callback(null, records.map(record => {
                            record.dataValues.email = record.dataValues.mail;
                            delete record.dataValues.mail;
                            return record;
                        }));

                        return null;
                    })
                    .catch(error => {
                        callback(error);
                    });
            }
        ])
    }

    getDonor(body, callback) {
        const donorId = body.donorId;

        models.donor
            .findOne({
                where: {
                    'id_donor': donorId
                }
            })
            .then(record => {
                if (record) {
                    record.dataValues.email = record.dataValues.mail;
                    delete record.dataValues.mail;
                    callback(null, record);
                } else {
                    callback({ message: 'Invalid donor id ' + donorId });
                }

                return null;
            })
            .catch(error => {
                callback(error);
            });
    }

    deleteDonor(body, callback) {
        const donorId = body.donorId;

        models.donor
            .destroy({
                where: {
                    'id_donor': donorId
                }
            })
            .then(response => {
                if (response) {
                    callback(null, { deleted: true });
                } else {
                    callback({ message: 'No data was deleted' });
                }

                return null;
            })
            .catch(error => {
                callback(error);
            });
    }

    getDoctors(body, callback) {
        const name = body.name;
        const surname = body.surname;
        const email = body.email;
        const password = body.password;
        const isActive = body.isActive;
        const hospitalId = body.hospitalId;

        let where = {};

        waterfall([
            // check params
            next => {
                if (!_.isUndefined(name) && !(_.isString(name) && name.length)) {
                    callback({ message: 'Invalid `name` param.' });
                }

                if (!_.isUndefined(surname) && !(_.isString(surname) && surname.length)) {
                    callback({ message: 'Invalid `surname` param.' });
                }

                if (!_.isUndefined(email) && !(_.isString(email) && email.length)) {
                    callback({ message: 'Invalid `email` param.' });
                }

                if (!_.isUndefined(password) && !(_.isString(password) && password.length)) {
                    callback({ message: 'Invalid `password` param.' });
                }

                // if (!_.isUndefined(isActive) && !_.isBoolean(isActive)) {
                //     callback({ message: 'Invalid `isActive` param.' });
                // }

                if (!_.isUndefined(isActive) && !(_.isString(isActive) && isActive.length && ['true', 'false'].includes(isActive.toLowerCase()))) {
                    callback({ message: 'Invalid `isActive` param.' });
                }

                // if (!_.isUndefined(hospitalId) && !_.isInteger(hospitalId)) {
                //     callback({ message: 'Invalid `hospitalId` param.' });
                // }

                if (!_.isUndefined(hospitalId) && !(_.isString(hospitalId) && !hospitalId.length)) {
                    callback({ message: 'Invalid `hospitalId` param.' });
                }

                next();
            },

            // build where object
            next => {
                if (!_.isUndefined(name)) {
                    where.name = name;
                }

                if (!_.isUndefined(surname)) {
                    where.surname = surname;
                }

                if (!_.isUndefined(email)) {
                    where.mail = email;
                }

                if (!_.isUndefined(password)) {
                    where.password = password;
                }

                if (!_.isUndefined(isActive)) {
                    where.is_active = isActive
                }

                if (!_.isUndefined(hospitalId)) {
                    where.id_hospital = hospitalId;
                }

                next();
            },

            // get donors
            () => {
                models.doctor
                    .findAll({
                        where: where
                    })
                    .then(records => {
                        callback(null, records.map(record => {
                            record.dataValues.email = record.dataValues.mail;
                            record.dataValues.isActive = record.dataValues.is_active;
                            delete record.dataValues.mail;
                            delete record.dataValues.is_active;
                            return record;
                        }));

                        return null;
                    })
                    .catch(error => {
                        callback(error);
                    });
            }
        ])
    }

    getDoctor(body, callback) {
        const doctorId = body.doctorId;

        models.doctor
            .findOne({
                where: {
                    'id_doctor': doctorId
                }
            })
            .then(record => {
                if (record) {
                    record.dataValues.email = record.dataValues.mail;
                    record.dataValues.isActive = record.dataValues.is_active;
                    delete record.dataValues.mail;
                    delete record.dataValues.is_active;
                    callback(null, record);
                } else {
                    callback({message: 'Invalid doctor id ' + doctorId});
                }

                return null;
            })
            .catch(error => {
                callback(error);
            });
    }

    deleteDoctor(body, callback) {
        const doctorId = body.doctorId;

        models.doctor
            .destroy({
                where: {
                    'id_doctor': doctorId
                }
            })
            .then(response => {
                if (response) {
                    callback(null, { deleted: true });
                } else {
                    callback({ message: 'No data was deleted' });
                }

                return null;
            })
            .catch(error => {
                callback(error);
            });
    }
}

module.exports = Service;
