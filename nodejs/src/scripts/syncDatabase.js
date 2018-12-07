'use strict';

let waterfall = require('async/waterfall');
let chalk = require('chalk');

const models = require('./../../database/models');

const ERROR_ICON = chalk.red('✖ ');
const SUCCESS_ICON = chalk.green('✔ ');
const ERROR_MESSAGE = chalk.red('🏁ERROR!\n');
const SUCCESS_MESSAGE = chalk.green('🏁SUCCESS!\n');

waterfall([
    next => {
        models.sequelize.sync({logging: false}).then(() => {
            console.log(SUCCESS_ICON + 'Synchronize database with the Sequelize models');
            next();

            return null;
        }).catch(next);
    },

    next => {
        models.sequelize.close().then(() => {
            console.log(SUCCESS_ICON + 'Close database connection');
            next();
        }).catch(next);
    }
], error => {
    if (error) {
        console.log(ERROR_ICON + error);
        console.log(ERROR_MESSAGE);
    } else {
        console.log(SUCCESS_MESSAGE);
    }
});
